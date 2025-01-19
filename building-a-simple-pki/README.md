# Building a simple PKI infrastructure
We are assuming an organisation named Simple Inc, which has control over the domain simple.org. Let’s look at the steps involved in building the PKI infrastructure which includes Root CA, Signing CA and TLS certificate.

Clone the Simple PKI example files and change directory:

```
git clone https://bitbucket.org/stefanholek/pki-example-1
cd pki-example-1
```
<img width="888" alt="image7" src="https://user-images.githubusercontent.com/6368257/101059490-561c1b00-35b4-11eb-8aab-352f0a0444d3.png">

#### Create Root CA:

Create the directories to hold the CA resources, CRLs and certificates:

```
mkdir -p ca/root-ca/private ca/root-ca/db crl certs
chmod 700 ca/root-ca/private
```

Create the database:

```
cp /dev/null ca/root-ca/db/root-ca.db
cp /dev/null ca/root-ca/db/root-ca.db.attr
echo 01 > ca/root-ca/db/root-ca.crt.srl
echo 01 > ca/root-ca/db/root-ca.crl.srl
```

After this the directory structure should be as given in the screenshot below:

<img width="891" alt="image6" src="https://user-images.githubusercontent.com/6368257/101060131-0e49c380-35b5-11eb-9e16-5d05b4079989.png">

Create the root CA request:

Use the “openssl req -new” command as given below to create a private key and a certificate signing request for the root CA.

```
openssl req -new \
    -config etc/root-ca.conf \
    -out ca/root-ca.csr \
    -keyout ca/root-ca/private/root-ca.key
```

<img width="889" alt="image15" src="https://user-images.githubusercontent.com/6368257/101060561-8dd79280-35b5-11eb-9b6b-f101911e3a5b.png">

Create the root CA certificate:

Next we will use the “openssl ca” command to issue a self-signed root CA certificate based on the certificate signing request(CSR) created in the previous step. Once the command given below is executed, there will be a prompt for passphrase for the private key of the root CA. After entering the passphrase, the certificate details will be displayed and it can then be signed.

```
openssl ca -selfsign \
    -config etc/root-ca.conf \
    -in ca/root-ca.csr \
    -out ca/root-ca.crt \
    -extensions root_ca_ext
```

<img width="891" alt="image10" src="https://user-images.githubusercontent.com/6368257/101060985-04749000-35b6-11eb-9d20-7d1a339320e2.png">
<img width="891" alt="image8" src="https://user-images.githubusercontent.com/6368257/101061141-2c63f380-35b6-11eb-8f04-27e226d585dd.png">

#### Create Signing CA:

Create the directories to hold the signing CA resources:
```
mkdir -p ca/signing-ca/private ca/signing-ca/db
chmod 700 ca/signing-ca/private
```

Create the database for signing CA:
```
cp /dev/null ca/signing-ca/db/signing-ca.db
cp /dev/null ca/signing-ca/db/signing-ca.db.attr
echo 01 > ca/signing-ca/db/signing-ca.crt.srl
echo 01 > ca/signing-ca/db/signing-ca.crl.srl
```

<img width="947" alt="image4" src="https://user-images.githubusercontent.com/6368257/101061662-ba3fde80-35b6-11eb-8f4e-1b619e070450.png">
<img width="130" alt="image20" src="https://user-images.githubusercontent.com/6368257/101061750-d479bc80-35b6-11eb-9a7b-7d581779f737.png">

Create the signing CA request:

Use the “openssl req -new” command as given below to create a private key and a certificate signing request for the signing CA.

```
openssl req -new \
    -config etc/signing-ca.conf \
    -out ca/signing-ca.csr \
    -keyout ca/signing-ca/private/signing-ca.key
```

<img width="946" alt="image1" src="https://user-images.githubusercontent.com/6368257/101061994-1b67b200-35b7-11eb-9995-659cfc5fac39.png">
<img width="611" alt="image9" src="https://user-images.githubusercontent.com/6368257/101062132-44884280-35b7-11eb-9d78-d8e4e8dc32f9.png">
<img width="725" alt="image11" src="https://user-images.githubusercontent.com/6368257/101062205-5e298a00-35b7-11eb-8931-26929cec9b30.png">

Create the signing CA certificate:

Next we will use the “openssl ca” command to issue a signing CA certificate based on the certificate signing request(CSR) created in the previous step.

```
openssl ca \
    -config etc/root-ca.conf \
    -in ca/signing-ca.csr \
    -out ca/signing-ca.crt \
    -extensions signing_ca_ext
```

<img width="670" alt="image13" src="https://user-images.githubusercontent.com/6368257/101062419-a2b52580-35b7-11eb-91bc-6ae162e3f605.png">
<img width="248" alt="image16" src="https://user-images.githubusercontent.com/6368257/101062564-caa48900-35b7-11eb-9613-856e3db64f5a.png">

#### Create TLS server certificate:

To create the TLS server certificate first we need to create the TLS server request using the command below. This will create a private key and a certificate signing request for the TLS server certificate.

```
SAN=DNS:www.simple.org \
openssl req -new \
    -config etc/server.conf \
    -out certs/simple.org.csr \
    -keyout certs/simple.org.key
```

<img width="833" alt="image2" src="https://user-images.githubusercontent.com/6368257/101062936-3d156900-35b8-11eb-8282-51c9fc6cea6b.png">

Using the signing CA and the CSR created from the previous step, a server certificate can be issued with the following command.

```
openssl ca \
    -config etc/signing-ca.conf \
    -in certs/simple.org.csr \
    -out certs/simple.org.crt \
    -extensions server_ext
```

<img width="678" alt="image5" src="https://user-images.githubusercontent.com/6368257/101063129-7b128d00-35b8-11eb-867d-4293f3020349.png">
<img width="891" alt="image8" src="https://user-images.githubusercontent.com/6368257/101063202-8e255d00-35b8-11eb-839d-01c8b809f1f5.png">
<img width="946" alt="image19" src="https://user-images.githubusercontent.com/6368257/101063245-9e3d3c80-35b8-11eb-86ec-1f239c3e458a.png">

We can view the TLS certificate created in the certs folder:

<img width="622" alt="image17" src="https://user-images.githubusercontent.com/6368257/101063383-bc0aa180-35b8-11eb-8018-bfcb52c366bb.png">
<img width="748" alt="image12" src="https://user-images.githubusercontent.com/6368257/101063536-e8beb900-35b8-11eb-8048-42e272c69a5d.png">
<img width="730" alt="image18" src="https://user-images.githubusercontent.com/6368257/101063619-01c76a00-35b9-11eb-83c5-1a62ede8e639.png">
<img width="668" alt="image3" src="https://user-images.githubusercontent.com/6368257/101063694-199eee00-35b9-11eb-95ed-0334fb38ec2c.png">

#### Install TLS server certificate on Tomcat:

We will use the generated TLS certificate above to configure Tomcat to work with SSL. For that , we need to generate a keystore which has the complete certificate chain beginning from the root and up until the server. 

Prepare the keystore file and add the root and signing certificate:

```
keytool -import -alias root-ca -keystore certs/simple.jks -trustcacerts -file ca/root-ca.crt
keytool -import -alias signing-ca -keystore certs/simple.jks -trustcacerts -file ca/signing-ca.crt
```

<img width="1014" alt="Screen Shot 2020-12-07 at 12 53 47 PM" src="https://user-images.githubusercontent.com/6368257/101324780-c4046300-3890-11eb-882f-ca04a90173d5.png">

<img width="1011" alt="Screen Shot 2020-12-07 at 12 55 36 PM" src="https://user-images.githubusercontent.com/6368257/101324800-c961ad80-3890-11eb-89da-3c80d5f4ee02.png">

Generate the certificate-key pair for the server:

```
openssl pkcs12 -export -name "tomcat" -inkey certs/simple.org.key -in certs/simple.org.crt -out certs/simple.p12
```

<img width="1009" alt="Screen Shot 2020-12-07 at 12 56 48 PM" src="https://user-images.githubusercontent.com/6368257/101324821-cd8dcb00-3890-11eb-8124-15befa12ce64.png">

Import the certificate-key pair to the keystore:

```
keytool -importkeystore -srckeystore certs/simple.p12 -destkeystore certs/simple.jks -srcstoretype pkcs12 -alias tomcat
```

<img width="1013" alt="Screen Shot 2020-12-07 at 12 59 21 PM" src="https://user-images.githubusercontent.com/6368257/101324841-d7afc980-3890-11eb-814e-3a91ec28c7cf.png">

Once the keystore is ready, then in Tomcat, the SSL configuration needs to be made in “server.xml” which is located in the “conf” directory of the Tomcat installation.

```
<Connector protocol="org.apache.coyote.http11.Http11NioProtocol"
    sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation"
    port="8443" maxThreads="150" SSLEnabled="true" scheme="https"
    secure="true" keyAlias="tomcat"  keystoreFile="/home/babu/github/simple-pki/certs/simple.jks"
    keystorePass="changeit" clientAuth="false" sslProtocol="TLS" />
```
After the configuration change, restart Tomcat and navigate to https://localhost:8443/

![2woE9DG](https://user-images.githubusercontent.com/6368257/101324898-e8f8d600-3890-11eb-9c32-0bc3407c60ae.png)

### References:
https://pki-tutorial.readthedocs.io/en/latest/simple/

https://medium.com/@superseb/get-your-certificate-chain-right-4b117a9c0fce
