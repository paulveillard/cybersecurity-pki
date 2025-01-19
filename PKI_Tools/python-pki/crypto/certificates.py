import configparser
import random
import sys

from OpenSSL import crypto

config = configparser.ConfigParser()
config.read('config.conf')

cert_conf = config['CERTIFICATES']


def gen_ca_interactive(sing_ca=None):
    # https://stackoverflow.com/questions/27164354/create-a-self-signed-x509-certificate-in-python
    # can look at generated file using openssl:
    # openssl x509 -inform pem -in selfsigned.crt -noout -text

    # Get Input from user
    emailAddress = input("EmailAddress: ")
    commonName = input("CommonName: ")

    while True:
        countryName = (
            input(
                "Country-Code (emtpy for conf: {}): ".format(
                    cert_conf['country']
                )
            ) or cert_conf['country']
        )
        if len(countryName) > 2:
            # This is not a restriction made by me, but enforced
            # by pyOpenSsl
            print("Country-Code must be 2 chars in length.")
        else:
            break

    localityName = (
        input(
            "LocalityName (emtpy for conf: {}): ".format(
                cert_conf['location']
            )
        ) or cert_conf['location']
    )
    stateOrProvinceName = (
        input(
            "StateOrProvinceName (emtpy for conf: {}): ".format(
                cert_conf['region']
            )
        ) or cert_conf['region']
    )
    organizationName = (
        input(
            "OrganizationName (emtpy for conf: {}): ".format(
                cert_conf['company']
            )
        ) or cert_conf['company']
    )
    organizationUnitName = (
        input(
            "OrganizationUnitName (emtpy for conf: {}): ".format(
                cert_conf['unit']
            )
        ) or cert_conf['unit']
    )
    serialNumber = random.randint(0, sys.maxsize)
    validityStartInSeconds = 0
    validityEndInSeconds = 10*365*24*60*60

    return gen_ca_noninter(
        countryName,
        stateOrProvinceName,
        localityName,
        organizationName,
        organizationUnitName,
        commonName,
        emailAddress,
        serialNumber,
        validityStartInSeconds,
        validityEndInSeconds
    )


def gen_ca_noninter(
    countryName,
    stateOrProvinceName,
    localityName,
    organizationName,
    organizationUnitName,
    commonName,
    emailAddress,
    serialNumber,
    validityStartInSeconds,
    validityEndInSeconds
):
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName  # noqa: E741
    cert.get_subject().OU = organizationUnitName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(validityStartInSeconds)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')

    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8")
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8")
    return cert, key


def gen_cert(ca=None, ca_key=None, ca_cert=None, commonName=None):
    '''Create an CERT signed by an given CA'''

    # Generate a CSR
    # http://docs.ganeti.org/ganeti/2.14/html/design-x509-ca.html
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 4096)

    req = crypto.X509Req()
    if commonName is None:
        commonName = input("CommonName: ")
    req.get_subject().CN = commonName
    req.set_pubkey(key)
    req.sign(key, "sha512")

    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode("utf-8")

    # Load cert and key if an ca is supplied
    if ca is not None:
        ca_cert = ca.get_cert()
        ca_key = ca.get_key()

    ca_cert = crypto.load_certificate(
        crypto.FILETYPE_PEM, bytes(ca_cert, 'utf-8')
    )
    ca_key = crypto.load_privatekey(
        crypto.FILETYPE_PEM, bytes(ca_key, 'utf-8')
    )

    # Generate Cert
    cert = crypto.X509()
    cert.set_subject(req.get_subject())
    cert.set_serial_number(random.randint(0, sys.maxsize))
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(1*365*24*60*60)
    cert.set_issuer(ca_cert.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(ca_key, "sha512")  # Sign with CA

    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8")

    return cert, key


def create_pkcs12(key, cert, password):
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    key = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    # pfx = crypto.PKCS12Type()
    pfx = crypto.PKCS12()
    pfx.set_privatekey(key)
    pfx.set_certificate(cert)
    pfxdata = pfx.export(password)
    return pfxdata


def validate_format_certificate(data):
    '''Checks if given (byte) data is a valid cert'''
    try:
        crypto.load_certificate(crypto.FILETYPE_PEM, data)
        return True
    except Exception:
        return False


def validate_format_privatekey(data):
    '''Checks if given (byte) data is a valid privkey'''
    try:
        crypto.load_privatekey(crypto.FILETYPE_PEM, data)
        return True
    except Exception:
        return False
