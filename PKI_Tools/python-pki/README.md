# python-pki
## How-To-Use
First and only one time run:

`python3 -m pip install -r requirements.txt`

and copy the `template/config.conf_dummy` to `./config.conf`. Adjust the values as needed.

Afterwards you can either start the console with:

`python3 python-pki.py`

or use the interactive version
`python3 python-pki.py -h`

## Description
This is an small python-tool for managing an CA with Client-Certificates for small environments.

## Console Functions
The interactive console provides the following functions:

Name | Description
--- | ---
help | Shows all available commands
genca | Adds an new CA
gencert | Adds an new Certificate, signed by an CA
getcas | Shows all stored CAs
getcerts | Shows all stored Certs
getcertsforca | Show all Cert for an CA
exportca | Exports an CA
exportcert | Exports an Cert
importca | Import an CA from file
importcert | Import an CERT from file
exit | Escape this hell

## Non-Interactive Functions
The non-interactive mode reads an json and outputs the CA and certificates to an output-dir.

Param | Description
--- | ---
--json | path to the json file
--out-dir | the output dir (can already exist or will be created)
--store-db | store the read ca and certs in the db

An example json can be found in the templates folder.

## Security
This tool provides a certain degree of security for the private keys of the CA and the Certs. The private key is encrypted in storage using Fernet (https://cryptography.io/en/latest/fernet/) with an key which is generated when an DB is first created (and can't be changed). All other fields are not encrypted - I prefer KISS and encryption is not always Simple and Stupid, so currently only the private keys are encrypted. If you think all fields should be encrypted, please file an issue or make a pull-request :)

## TODOs
This tool is usable, but far from finished. For all TODOs, please check the issues on https://github.com/sn0b4ll/python-pki/issues
