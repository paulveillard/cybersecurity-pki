# Public Key Infrastructure (PKI):  Theory, Techniques, and Tools


An ongoing & curated collection of awesome software best practices and techniques, libraries and frameworks, E-books and videos, websites, blog posts, links to github Repositories, technical guidelines and important resources about Public Key Infrastructure (PKI) in Cybersecurity.
> Thanks to all contributors, you're awesome and wouldn't be possible without you! Our goal is to build a categorized community-driven collection of very well-known resources.


Public-key infrastructure (PKI) is what makes internet encryption and digital signatures work. When you visit your bank website you are told it is encrypted and verified. 

![image](https://github.com/user-attachments/assets/88e5468a-cbe4-48f6-9a29-3f0ae5a4c224)

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


## `Table of Contents`
- [Introduction](#Introduction)
  - [What is PKI](#)
  - [how does PKI Work](#)
  - [What is PKI used for](#)
- [Resources](#resources)
