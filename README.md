# Public Key Infrastructure (PKI):  Theory, Techniques, and Tools


An ongoing & curated collection of awesome software best practices and techniques, libraries and frameworks, E-books and videos, websites, blog posts, links to github Repositories, technical guidelines and important resources about Public Key Infrastructure (PKI) in Cybersecurity.
> Thanks to all contributors, you're awesome and wouldn't be possible without you! Our goal is to build a categorized community-driven collection of very well-known resources.


Public-key infrastructure (PKI) is what makes internet encryption and digital signatures work. When you visit your bank website you are told it is encrypted and verified. 

![image](https://github.com/user-attachments/assets/88e5468a-cbe4-48f6-9a29-3f0ae5a4c224)

## `Table of Contents`
- [Introduction](#Introduction)
  - [What is PKI](#what-is-pki)
  - [how does PKI Work](#)
  - [What is PKI used for](#)
  - [PKI Concepts](#)
    - [Process](#)
    - [Components](#)
    - [CA Types](#)
    - [Certificate Types](#)
    - [File Formats](#)
- [Resources](#resources)
  - [Root Certificate Programs](#)
  - [Articles & Other sources](#)
  - [Hardware Secure Modules (HSM) & Key management](#)
  - [Books](#)
  - [Research Papers](#)
  - [ Audio / Video](#)
  - [Open-Source Certificate Authority Software](#)

# `Introduction`

## `What is PKI?`
Before we talk about what exactly PKI is, we need to talk about public-key cryptography. Public-key cryptography is a type of cryptography that uses asymmetric encryption which is a type of encryption that uses multiple keys. Public-key cryptography has a private key, and a public key. Both keys can encrypt data, but the public key can only decrypt data encrypted by the private key. The public key can also not be easily derived from the private key.

![1](https://github.com/paulveillard/cybersecurity-pki/blob/main/img/1.png)

If two people exchange public keys with each other, they can talk to each other securely. They do this by encrypting messages with their own private key as well as the other person’s public key. There is one big question: how do these people exchange public keys securely? If they send them via an insecure channel, someone could intercept the keys, and substitute in their own, different keys. Each person would think they were talking directly with the other, when, in fact, they were both now talking to an attacker.

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/2.png?raw=true" alt="Sublime's custom image"/>
</p>




- Public-key cryptography can create secure channels of communication, but it requires an existing secure channel to exchange keys.
 > This is the problem that PKI aims to solve. PKI’s most basic purpose is to securely distribute and manage public keys.

- It does this using trusted third parties who verify the authenticity of public keys and then use their own private keys to digitally sign the public keys. That way, even if the key is not encrypted and has to be sent over cleartext, we will still be able to verify that the key is trusted by the third party.


## `How does PKI Work?`
PKI takes advantage of the fact that information encrypted with a private key can be decrypted by anyone with the corresponding public key. This is used to create digital certificates vouching for the authenticity of a given public key. The third-parties who verify the authenticity are known as certificate authorities, or CAs for short.

You may have noticed this doesn’t actually solve the problem of securely exchanging public keys… it just moves it! We still need some way to securely get the certificate authority’s public key. For this reason, there are hierarchies of certificate authorities, with root CAs at the top of the hierarchy.

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/3.png?raw=true" alt="Sublime's custom image"/>
</p>
When we install an operating system on a device, that operating system comes with the certificates for root CAs already installed on it. Our computer uses these certificates to determine which root CAs it can trust, and, from there, follows the chain of trust until it is able (or unable) to verify the authenticity of the public key for, say, a website.

This system isn’t perfect. There have been cases of computer manufacturers installing additional root CAs on computers without informing customers, for the purpose of distributing ads. There have also been instances of certificate authorities having their private keys compromised. For these reasons, PKI usually has additional security features.

**Certificate Revocation** is the ability for certificate authorities to revoke certificates, essentially saying “we no longer verify the legitimacy of this private key.” Certificates also expire after a set amount of time and must be renewed. Certificate pinning is when a computer or software remembers what certificate a given entity (usually a website) uses. Even if a CA is compromised and maliciously issues certificates for that entity, they won’t match the saved certificate and won’t be accepted.

## `What is PKI used for?`
Well, pretty much every website we use, for one thing! The github.com domain, for example, has a SSL certificate that proves it’s the real website and not an impostor. That certificate is signed by a certificate authority, and follows a chain of trust back to a certificate that’s on our computer somewhere. When we connect to codecademy.com via HTTPS, our browser requests Codecademy’s certificate and uses it to verify the legitimacy of the server before establishing a secure connection.

While we usually talk about PKI in the context of web security, it comes in handy any time we need a system to exchange public keys and verify their authenticity. PKI can be used for wireless network security, multi-factor authentication, file-sharing, remote connection protocols, email security, digitally signing documents, and more!

> PKI is an essential technology for modern security, serving as a foundation for modern web security. While PKI can seem intimidating at first, it isn’t as hard to understand once we see what problems it tries to solve, and know about the cryptographic principles that make it work. Not everyone needs to know the technical details of how PKI works, but it’s something that everyone in cybersecurity should have a basic knowledge of.


## `PKI Concepts`

**An X.509 PKI is a security architecture that uses well-established cryptographic mechanisms to support use-cases like email protection and web server authentication.** In this regard it is similar to other systems based on public-key cryptography, for example OpenPGP [RFC 4880]. In the realm of X.509 however, and thanks to its roots in a globe-spanning scheme devised by the telecom industry [X.400], these mechanisms come with a fair amount of administrative overhead.

> One thing to keep in mind is that X.509 is not an application, but a specification upon which applications like Secure Multipurpose Internet Mail Extensions (S/MIME) and Transport Layer Security (TLS) are based. The building blocks are very generic and derive most of their meaning from the relations that exist/are established between them. It’s called an infrastructure for a reason.

### PKI Process

#### 1 - A requestor generates a CSR and submits it to the CA.

#### 2 - The CA issues a certificate based on the CSR and returns it to the requestor.

#### 3 - Should the certificate at some point be revoked, the CA adds it to its CRL.



## `Root Certificate Programs`  

The organizations behind the browser and the operating system development maintain the most widely used collections of up-to-date certificate authority certificates.    
Root programs keep the list up-to-date and work together on the process standardization.  

[Chrome Root Program](https://www.chromium.org/Home/chromium-security/root-ca-policy/)  
[Mozilla's CA Certificate Program](https://wiki.mozilla.org/CA)  
[Apple Root Certificate Program](https://www.apple.com/certificateauthority/ca_program.html)  
[Microsoft Trusted Root Certificate Program](https://aka.ms/RootCert)  
[The Common CA Database (CCADB)](https://www.ccadb.org/) - managed by Mozilla, supported by Microsoft & Google  


## `Articles & Other sources`

[Everything you Never Wanted to Know about PKI but were Forced to Find Out (PDF)](https://www.cs.auckland.ac.nz/~pgut001/pubs/pkitutorial.pdf) - by Peter Gutmann  
[PKI: It’s Not Dead,Just Resting (PDF)](https://people.cs.vt.edu/~kafura/cs6204/Readings/Authentication/PKINotDead.pdf) - Peter Gutmann  
[X.509 Style Guide](https://www.cs.auckland.ac.nz/~pgut001/pubs/x509guide.txt) - by Peter Gutmann  
[SSL/TLS and PKI History](https://www.feistyduck.com/ssl-tls-and-pki-history/) - Feisty Duck  
[How to build your own public key infrastructure](https://blog.cloudflare.com/how-to-build-your-own-public-key-infrastructure/) - The Cloudflare Blog  
[Everything you should know about certificates and PKI but are too afraid to ask](https://smallstep.com/blog/everything-pki/) - Smallstep Labs blog  
[Path Building vs Path Verifying: The Chain of Pain](https://medium.com/@sleevi_/path-building-vs-path-verifying-the-chain-of-pain-9fbab861d7d6)  
[Certificate Transparency: a bird's-eye view](https://emilymstark.com/2020/07/20/certificate-transparency-a-birds-eye-view.html)  
[Key Management Cheat Sheet, OWASP](https://www.owasp.org/index.php/Key_Management_Cheat_Sheet)  
[Certificate Policy and Certification Practice Statement documents for ISRG / Let's Encrypt](https://github.com/letsencrypt/cp-cps)  
[Checklist on building an Offline Root & Intermediate Certificate Authority (CA)](https://security.stackexchange.com/questions/15532/checklist-on-building-an-offline-root-intermediate-certificate-authority-ca) - Stack Overflow  
[Certificate Authority with a YubiKey](https://developers.yubico.com/PIV/Guides/Certificate_authority.html)  
[Get started with the Nitrokey HSM or SmartCard-HSM](https://raymii.org/s/articles/Get_Started_With_The_Nitrokey_HSM.html)  
[PKI maturity model](https://pkic.org/pkimm/model/) - by PKI Consortium  
[PKI Posters](https://www.cem.me/pki) - Posters by Carl Mehner about the entire lifecycle of an SSL certificate

## `Hardware Secure Modules (HSM) & Key management`  

[Why I don't like smartcards, HSMs, YubiKeys, etc.](https://news.ycombinator.com/item?id=13031155) - Hacker News  
[The Untold Story of PKCS#11 HSM Vulnerabilities](https://cryptosense.com/blog/the-untold-story-of-pkcs11-hsm-vulnerabilities/) - Cryptosense  
[A survey of Hardware Crypto Devices (PDF)](https://cryptotronix.com/wp-content/uploads/2016/10/cryptowarez_nopause.pdf) - cryptotronix  
[Linux smart cards (OpenSC) - How-to](http://cedric.dufour.name/blah/IT/SmartCardsHowto.html) - Cédric Dufour blog  
[Key Management and use cases for HSMs](https://www.cryptomathic.com/news-events/blog/key-management-and-use-cases-for-hsms) - Cryptomathic  
[What is Key Management? a CISO Perspective](https://www.cryptomathic.com/news-events/blog/what-is-key-management-a-ciso-perspective) - Cryptomathic  
[The Definitive Guide to Encryption Key Management Fundamentals](https://info.townsendsecurity.com/definitive-guide-to-encryption-key-management-fundamentals) - Townsend Security  
[Example of an IANA DNSSEC signing ceremony](https://www.iana.org/dnssec/ceremonies/32) - not x509, but describes the procedure of a serious key ceremony  
[Security Concepts, Subsection 28.9: Key Management](https://www.subspacefield.org/security/security_concepts/#toc-Subsection-28.9) - blog of Travis  
[NIST Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines)  
[NIST Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program/Modules-In-Process/Modules-In-Process-List)  
[Commercial Cryptographic Key Management in 2018](https://www.malgregator.com/post/key-management/)  


## `Books`

[Bulletproof SSL and TLS: Understanding and Deploying SSL/TLS and PKI to Secure Servers and Web Applications](https://www.feistyduck.com/books/bulletproof-tls-and-pki/), Ivan Ristić

[Cryptography Engineering: Design Principles and Practical Applications](https://www.schneier.com/books/cryptography-engineering/), Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno

[Security Engineering, The Second Edition (2008) - Chapter 21: Network Attack and Defence](https://www.cl.cam.ac.uk/~rja14/book.html), Ross Anderson

[Encyclopedia of Cryptography and Security](https://www.researchgate.net/publication/230674947_Springer_Encyclopedia_of_Cryptography_and_Security), Henk C.A. van Tilborg  

[Architecture for Public-Key Infrastructure (APKI)](https://pubs.opengroup.org/onlinepubs/009219899/toc.pdf), The Open Group Guide, 1999  


## `Research Papers`  

[Is the Web Ready for OCSP Must-Staple? (PDF)](https://balakrishnanc.github.io/papers/chung-imc2018.pdf)  

[The First Ten Years of Public-Key Cryptography - Whitfield Diffie (PDF)](https://www.cs.virginia.edu/~evans/greatworks/diffie.pdf)  

[PKI considered harmful](https://iang.org/ssl/pki_considered_harmful.html)  

## `Audio / Video` 

Hackable Security Modules: reversing and exploiting a FIPS 140-2 lvl3 HSM firmware - [video](https://www.youtube.com/watch?v=X8xu_I9kn18), [PDF](https://recon.cx/2017/brussels/resources/slides/RECON-BRX-2017-reversinghsms2.pdf)  
PKI Bootcamp by Paul Turner - [Playlist](https://www.youtube.com/playlist?list=PLDp2gaPHHZK-mnKi3Zy_-hRjqLHh5PaAv)  
How to be a Certificate Authority, feat. Ryan Sleevi - [Security. Cryptography. Whatever. podcast](https://securitycryptographywhatever.buzzsprout.com/1822302/9146390-how-to-be-a-certificate-authority-feat-ryan-sleevi)  
Fundamental X.509 PKI in Theory and OpenSSL (Cyrill Gössi) - [Playlist](https://www.youtube.com/playlist?list=PLWjMI9CAmVU4AHEMlq_SUuIAgeCDOdrvO)

## `Open-Source Certificate Authority Software`  

| Software | pkcs11 support | ACME support | Notes |
|----------|----------------|--------------|-------|
| [Let's Encrypt Boulder](https://github.com/letsencrypt/boulder) | yes | yes | not much documentation, no commercial support |
| [step-ca](https://github.com/smallstep/certificates) | yes | yes | cloud-ready CA with the commercial support |
| [EJBCA](https://www.ejbca.org/) | yes | yes | $$$$ commercial support |
| [Dogtag Certificate System](https://github.com/dogtagpki/pki) | yes | yes | n/a |
| [HashiCorp Vault PKI backend](https://www.vaultproject.io/docs/secrets/pki) | no (only enterprise?) | no | API based CA |
| [CFSSL](https://github.com/cloudflare/cfssl) | no | no | PKI toolkit with an API |
| [easy-rsa](https://github.com/OpenVPN/easy-rsa) | no | no | easy-rsa - Simple shell based CA utility |
| [OpenSSL Certificate Authority](https://jamielinux.com/docs/openssl-certificate-authority/) | yes | no | shell based CA leveraging OpenSSL |
| [XCA](https://www.hohnstaedt.de/xca/) | yes | no | Certificate authority with a comprehensive GUI |


## `License`
MIT License & [cc](https://creativecommons.org/licenses/by/4.0/) license

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

To the extent possible under law, [Paul Veillard](https://github.com/paulveillard/) has waived all copyright and related or neighboring rights to this work.
