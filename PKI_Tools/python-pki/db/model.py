import configparser
import random
import string
import sys

from cryptography.fernet import Fernet, InvalidToken

from getpass import getpass

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from OpenSSL import crypto

config = configparser.ConfigParser()
config.read('config.conf')


engine = create_engine(config['DB']['con_string'])
Base = declarative_base()

NEW_DB = False

if not engine.dialect.has_table(engine, 'certs'):
    # DB does no exist yet, create a new key
    FERNETKEY = Fernet.generate_key()
    NEW_DB = True
else:
    try:
        CHALLENGE, FERNETKEY = getpass("Please enter the secret: ").split(":")
    except ValueError:
        print("[!] Secret in wrong format!")
        sys.exit()
    FERNETKEY = FERNETKEY.encode('utf-8')


class CA(Base):
    __tablename__ = 'cas'
    cipher_suite = Fernet(FERNETKEY)

    id = Column(Integer, primary_key=True)
    desc = Column(String)
    cert = Column(String)
    key = Column(String)
    certs = relationship("CERT", back_populates="ca")

    def __init__(self, desc, cert, key):
        self.desc = desc
        self.cert = cert
        self.key = self.cipher_suite.encrypt(bytes(key, encoding='utf8'))

    def get_key(self):
        return self.cipher_suite.decrypt(self.key).decode('utf-8')

    def get_cert(self):
        return self.cert

    def get_pub(self):
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, self.cert)
        return crypto.dump_publickey(
            crypto.FILETYPE_PEM, cert.get_pubkey()).decode('utf-8')

    def __repr__(self):
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, self.cert)
        return "{}, {}, {}".format(self.id, self.desc, cert.get_subject().CN)


class CERT(Base):
    __tablename__ = 'certs'
    cipher_suite = Fernet(FERNETKEY)

    id = Column(Integer, primary_key=True)
    desc = Column(String)
    cert = Column(String)
    key = Column(String)
    ca_id = Column(Integer, ForeignKey('cas.id'))
    ca = relationship("CA", back_populates="certs")

    def __init__(self, desc, cert, key, ca):
        self.desc = desc
        self.cert = cert
        self.key = self.cipher_suite.encrypt(bytes(key, encoding='utf8'))
        self.ca = ca

    def get_key(self):
        return self.cipher_suite.decrypt(self.key).decode('utf-8')

    def get_cert(self):
        return self.cert

    def get_pub(self):
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, self.cert)
        return crypto.dump_publickey(
            crypto.FILETYPE_PEM, cert.get_pubkey()).decode('utf-8')

    def __repr__(self):
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, self.cert)
        return "{}, {}, {}, {}".format(
            self.id, self.desc, cert.get_subject().CN, self.ca.id
        )


class EncTest(Base):
    __tablename__ = 'enctest'
    cipher_suite = Fernet(FERNETKEY)

    testval = Column(String, primary_key=True)

    def __init__(self, testval):
        self.testval = self.cipher_suite.encrypt(
            bytes(testval, encoding='utf8')
        )

    def check(self, testval):
        try:
            decrypted = self.cipher_suite.decrypt(self.testval).decode('utf-8')
            if testval == decrypted:
                return True
            else:
                return False
        except InvalidToken:
            return False


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


if NEW_DB:
    challenge = ''.join(
        random.choice(string.ascii_lowercase) for i in range(15)
    )
    print("++++++++++++ Key ++++++++++++")
    print("{}:{}".format(challenge, FERNETKEY.decode('utf-8')))
    print("+ Please write this key down +")
    print("+++++++++++++++++++++++++++++")
    input("\nPress enter to continue..")

    test_val = EncTest(challenge)
    session.add(test_val)
    session.commit()
else:
    enctest = session.query(EncTest).one()
    if not enctest.check(CHALLENGE):
        print("Sorry, wrong secret!")
        sys.exit()
