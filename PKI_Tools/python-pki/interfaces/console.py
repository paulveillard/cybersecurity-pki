#!/usr/bin/env python3
import os.path

from crypto.certificates import gen_ca_interactive, gen_cert, create_pkcs12
from crypto.certificates import validate_format_certificate
from crypto.certificates import validate_format_privatekey
from cmd import Cmd
from getpass import getpass
from db.model import session, CA, CERT
from texttable import Texttable


class Console(Cmd):
    def _get_san_input_int(self, message, bound):
        while True:
            try:
                val = input(message)
                int_val = int(val)
                if int_val < 1 or int_val > bound:
                    raise Exception()
                return int_val
            except Exception:
                print("Please verify.")
            else:
                break

    def _print_cas(self):
        '''Print existing CAs'''
        t = Texttable()
        ca_list = session.query(CA).all()
        for ca in ca_list:
            t.add_rows([['ID', 'Desc', 'CommonName'], str(ca).split(", ")])
        print(t.draw())
        return len(ca_list)

    def _print_certs(self):
        '''Print existing certs'''
        t = Texttable()
        cert_list = session.query(CERT).all()
        for cert in cert_list:
            t.add_rows(
                [['ID', 'Desc', 'CommonName', 'CA-ID'], str(cert).split(", ")]
            )
        print(t.draw())
        return len(cert_list)

    def do_exit(self, inp):
        '''Exit'''
        print("For Feedback, please visit the github-page :)")
        return True

    def do_genca(self, inp):
        '''Create a new CA'''
        cert, key = gen_ca_interactive()
        desc = input("Please enter an description: ")
        ca = CA(desc, cert, key)
        session.add(ca)
        session.commit()

    def do_gencert(self, inp):
        '''Add an CERT to an CA'''
        # Print existing CAs
        self._print_cas()

        # Get ca_id to export by user
        ca_id = input("CA to use for signing: ")

        # Extract from the DB
        ca = session.query(CA).filter(CA.id == ca_id).one()

        # Generate CERT, create an DB-Obj and add to session
        cert, key = gen_cert(ca=ca)
        desc = input("Please enter an description: ")
        cert = CERT(desc, cert, key, ca)
        session.add(cert)
        session.commit()

    def do_getcas(self, inp):
        '''Get all CAs'''
        self._print_cas()

    def do_getcerts(self, inp):
        '''Get certs'''
        t = Texttable()
        for cert in session.query(CERT).all():
            t.add_rows(
                [['ID', 'Desc', 'CommonName', 'CA-ID'], str(cert).split(", ")]
            )
        print(t.draw())

    def do_getcertsforca(self, inp):
        '''Get all certs for an ca'''
        # Print existing CAs
        self._print_cas()

        # Let the user select the CA
        ca_id = input("Choose an CA by ID: ")

        # Print all CERTs for CA
        t = Texttable()
        for cert in session.query(CERT).filter(CERT.ca_id == ca_id).all():
            t.add_rows(
                [['ID', 'Desc', 'CommonName', 'CA-ID'], str(cert).split(", ")]
            )
        print(t.draw())

    def _get_cert_info_as_string(self, cert, what_to_export):
        '''Export whatever is selected'''
        if what_to_export == 1:
            return cert.get_key()
        elif what_to_export == 2:
            return cert.get_cert()
        elif what_to_export == 3:
            return cert.get_pub()
        elif what_to_export == 4:
            key = cert.get_key()
            cert = cert.get_cert()
            password = getpass()
            return create_pkcs12(key, cert, password)
        else:
            raise Exception("Value out of range.")

    def _export_val(self, val):
        # Ask user for target
        t = Texttable()
        t.add_rows(
            [
                ['ID', 'Target'],
                ['1', 'File'],
                ['2', 'Console']
            ]
        )
        print(t.draw())

        target = self._get_san_input_int("Choose target: ", 2)

        if target == 1:
            # Export to file
            filename = input("Choose filename: ")

            f = open(filename, 'wb')
            # Hacky, but PKCS12 comes as bytes while the others do not :/
            try:
                f.write(val.encode('utf-8'))
            except AttributeError:
                f.write(val)
            f.close()
            print("Data was saved to {}".format(filename))
        elif target == 2:
            # Export to console
            print(val)
        else:
            raise Exception("Waaaait, what?")

    def do_exportca(self, inp):
        '''Export an key or cert of the ca'''
        num_cas = self._print_cas()
        ca_id = self._get_san_input_int("Choose an CA to export: ", num_cas)
        ca = session.query(CA).filter(CA.id == ca_id).one()

        # Ask user what to export
        t = Texttable()
        t.add_rows(
            [
                ['ID', 'Target'],
                ['1', 'private key (PEM)'],
                ['2', 'certificate (CRT)'],
                ['3', 'public key (PEM)']
            ]
        )
        print(t.draw())
        what_to_export = self._get_san_input_int("What to export :", 3)
        val = self._get_cert_info_as_string(ca, what_to_export)

        self._export_val(val)

    def do_exportcert(self, inp):
        '''Export an key or cert of an client-cert'''
        num_certs = self._print_certs()
        cert_id = self._get_san_input_int(
            "Choose an certificate to export: ",
            num_certs
        )
        cert = session.query(CERT).filter(CERT.id == cert_id).one()

        # Ask user what to export
        t = Texttable()
        t.add_rows(
            [
                ['ID', 'Target'],
                ['1', 'private key (PEM)'],
                ['2', 'certificate (CRT)'],
                ['3', 'public key (PEM)'],
                ['4', 'packed and pw-protected (PKCS12)'],
            ]
        )
        print(t.draw())

        what_to_export = self._get_san_input_int("What to export :", 4)
        val = self._get_cert_info_as_string(cert, what_to_export)

        self._export_val(val)

    def do_importcertforca(self, inp):
        '''Import an certificate for an existing CA'''
        pass

    def _load_key_and_cert_from_file(self):
        '''Asks for paths and loads key and cert'''
        # TODO(Option for PK12)
        path_key = input(
            "Please enter the path to the private key-file: "
        ).strip()
        path_cert = input(
            "Please enter the path to the cert-file: "
        ).strip()

        # Check if path is valid
        if (
            (not os.path.isfile(path_key)) or (not os.path.isfile(path_cert))
                ):
            print("[!] One of the provided paths does not point to an file.")
            return

        # Read both files
        f = open(path_key, 'rb')
        key = f.read()
        f.close()

        f = open(path_cert, 'rb')
        cert = f.read()
        f.close()

        # If valid, create and commit the DB-Object
        if (validate_format_privatekey(key)
                and validate_format_certificate(cert)):
            return key.decode('utf-8'), cert.decode('utf-8')
        else:
            raise Exception(
                "[!] One of the files is not in an correct PEM-Format"
            )

    def do_importca(self, inp):
        '''Import an CA'''
        # Get the key and cert from file
        key, cert = self._load_key_and_cert_from_file()

        # Enrich with description
        desc = input("Please enter an description: ")

        # Creat DB-Object and commit
        ca = CA(desc, cert, key)
        session.add(ca)
        session.commit()

    def do_importcert(self, inp):
        '''Import an Cert'''

        # Get ca_id to export by user and extract from db
        self._print_cas()
        ca_id = input("CA to use for signing: ")
        ca = session.query(CA).filter(CA.id == ca_id).one()

        # Get the key and cert from file
        key, cert = self._load_key_and_cert_from_file()

        # Creat DB-Object and commit
        desc = input("Please enter an description: ")
        cert = CERT(desc, cert, key, ca)
        session.add(cert)
        session.commit()
