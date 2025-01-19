import json
import random
import string
import sys
import os

from crypto.certificates import gen_ca_noninter, gen_cert, create_pkcs12


class Noninteractive:

    def __init__(self, args):

        if args.store_db:
            # Only import if db-storage is requested
            from db.model import session, CA, CERT

        print("[+] Reading JSON")
        f = open(args.json, 'r')
        try:
            ca_json = json.loads(f.read())
            f.close()
        except json.decoder.JSONDecodeError as e:
            print("[!] Your Json is broken!")
            print(e)
            f.close()
            sys.exit()
        print("[+] JSON ok")

        # Generate key and cert for CA
        print("[+] Generating CA")
        ca_cert, ca_key = gen_ca_noninter(
            countryName=ca_json['ca']['countryName'],
            stateOrProvinceName=ca_json['ca']['stateOrProvinceName'],
            localityName=ca_json['ca']['localityName'],
            organizationName=ca_json['ca']['organizationName'],
            organizationUnitName=ca_json['ca']['organizationUnitName'],
            commonName=ca_json['ca']['commonName'],
            emailAddress=ca_json['ca']['emailAddress'],
            serialNumber=ca_json['ca']['serialNumber'],
            validityStartInSeconds=ca_json['ca']['validityStartInSeconds'],
            validityEndInSeconds=ca_json['ca']['validityEndInSeconds']
        )

        path = args.out_path

        # TODO(--store-db not yet defined)
        # Export ca
        self._write_to_disk(
            path, "", ca_json['ca']['commonName'] + ".key", ca_key
        )
        self._write_to_disk(
            path, "", ca_json['ca']['commonName'] + ".crt", ca_cert
        )

        if args.store_db:
            ca = CA("Imported vis JSON", ca_cert, ca_key)
            session.add(ca)
            session.commit()

        # Generate certificates
        print("[+] Generating Certs")
        password = ''.join(
            random.choice(string.ascii_letters) for i in range(30)
        )
        print(
            "[*] The password for the pk12-files is: {}".format(password)
        )
        for cert_req in ca_json['ca']['certs']:
            # Generate Cert
            cert, key = gen_cert(
                ca_key=ca_key,
                ca_cert=ca_cert,
                commonName=cert_req['commonName']
            )

            # Export
            # Save crt
            subfix = ca_json['ca']['commonName']
            self._write_to_disk(
                path, subfix, cert_req['commonName'] + ".crt", cert
            )
            # Save Key
            self._write_to_disk(
                path, subfix, cert_req['commonName'] + ".key", key
            )

            # Save pk12
            pk12 = create_pkcs12(key, cert, password)
            self._write_to_disk(
                path, subfix, cert_req['commonName'] + ".p12", pk12
            )

            if args.store_db:
                cert = CERT("Imported vis JSON", cert, key, ca)
                session.add(cert)
                session.commit()

    def _write_to_disk(self, path, path_subfix, filename, data):
        '''Writes to disk what is passed as data'''
        path = "".join([path, '/', path_subfix, '/'])
        try:
            os.mkdir(path)
        except FileExistsError:
            # Just trying to create it, if it is already there so shall be it
            pass

        filename = "".join([path, filename])

        f = open(filename, 'wb')
        try:
            f.write(data.encode('utf-8'))
        except AttributeError:
            f.write(data)
        f.close()
