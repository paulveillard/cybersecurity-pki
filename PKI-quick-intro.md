
# PKI for busy people

Public-key infrastructure (PKI) is an umbrella term for everything that has to do with keys and certificates.

This is a quick overview of the important stuff.

## Public-key cryptography

Public-key cryptography involves a key pair: a *public key* and a *private key*. Each entity has their own. The public key can be shared around, the private key is secret.

They allow doing two things:

1. *Encrypt* a message with the public key, *decrypt* it with the private key.
1. *Sign* a message with the private key, *verify* it with the public key.

Some common algorithms are [RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) (used for both) and [EdDSA](https://en.wikipedia.org/wiki/EdDSA) (only for signatures).

In practice, public-key cryptography can be slow. That’s why nearly all protocols (such as [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) or [SSH](https://en.wikipedia.org/wiki/Secure_Shell)) only use it for authentication. Much faster symmetric-key algorithms (such as [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)) are then used for encryption. This requires a shared secret, which is usually agreed upon using some flavor of [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

## Hashing

Hashing algorithms (such as [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)) are one-way functions that take any input and compute a unique fixed-size output. The output is called a *hash* (or sometimes *digest*).

## Signatures

Signatures authenticate messages. Roughly:

* A signature is calculated from a message and a private key.
* With only the message and a public key, anyone can verify whether the signature was calculated using its corresponding private key.

Signing the whole message is pretty inefficient, so its hash is signed instead. That’s why you’ll see signature algorithms with descriptions like “ECDSA with SHA-256.”

## Certificates

A certificate is a name and public key bound by a signature. It identifies the owner of a public key.

The signee is called a certificate authority (CA). The CA is often some company, like GeoTrust or Let’s Encrypt. With internal PKI, it can be any entity that nodes have been configured to trust.

A CA’s certificate can be signed by another CA, and so on. The last certificate in the chain is called a *root certificate*. Root certificates are trusted and stored locally. They’re usually shipped along browsers and the OS.

### Formats

Most often when people talk about certificates, they’re referring to [X.509](https://en.wikipedia.org/wiki/X.509). It’s a flexible format for representing certificates. X.509 is used by TLS, which is used by a *lot* of things, like HTTPS and Kubernetes.

X.509 certificates are written in [ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One). The ASN.1 is usually serialized into [DER](https://en.wikipedia.org/wiki/X.690#DER_encoding). Since binary data can be a pain to transmit, it’s often further encoded into [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail). PEM is essentially [Base64](https://en.wikipedia.org/wiki/Base64)-encoded DER.

### Verification

Certificate verification consists of making sure the certificate chain is valid and leads to a trusted root certificate.

Of course, it assumes we trust the CAs, safe in the knowledge that they conform to sane security practices and only issue certificates to verified entities.

### Bundling

Since verification requires the complete chain, certificates are often distributed as a bundle. In the case of TLS, the chain is sent during the [handshake](https://tools.ietf.org/html/rfc8446#section-4.4.2).

Usually PEM files are just concatenated into one.

Certificates can also be bundled using [PKCS #12](https://en.wikipedia.org/wiki/PKCS_12) (also known as PFX) or [CMS](https://tools.ietf.org/html/rfc5652) (formerly [PKCS #7](https://tools.ietf.org/html/rfc2315)). The main difference is PKCS #12 can store private keys.

### Issuance

When applying for a certificate:

1. The client sends a [certificate signing request](https://en.wikipedia.org/wiki/Certificate_signing_request) (CSR) to the CA. It includes the client’s public key and a bunch of [distinguished name attributes](https://tools.ietf.org/html/rfc3739#section-3.1.2) (such as country and domain name).
1. If everything looks good, the CA generates a certificate from the CSR.

In the simplest case, the CA only performs Domain Validation (DV). It’s usually fast and automated, like checking for some specific DNS record.

For more thorough vetting, there’s also Organization Validation (OV) and Extended Validation (EV). OV implies DV *and* verifying ownership of the legal entity. EV is the slowest and most rigorous of all, based on [CA/Browser Forum guidelines](https://cabforum.org/extended-validation/). EV certificates are usually displayed prominently (for example, on Safari the URL will be green).

For internal PKI, you can do whatever works best. You could send certificates to the nodes manually, or automate client CSRs and signing.

### Revocation

There’s basically two ways to revoke certificates: [certificate revocation lists](https://en.wikipedia.org/wiki/Certificate_revocation_list) (CRLs) and [OCSP](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol). A CRL is a big list of certificates revoked by the CA. OCSP is a protocol that allows inquiring about a specific certificate.

## Summary

* With someone’s public key, we can verify their signatures and send them encrypted messages.
* With our private key, we can sign messages and decrypt messages sent to us.
* Certificates identify public key owners.
* We trust a certificate because we trust the CA that signed it.
* We trust the CA because Apple/Google/Microsoft/whoever added the CA’s certificate on our host trusts them.
