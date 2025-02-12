## PKI Architecture: Fundamentals of Designing a Private PKI System

## Table of Contents
- [1 - What Is PKI? A 2-Minute Review of a Few Key Concepts](#)
  - [1.1 - First, How Does PKI Work](#)
  - [1.2 - Publicly trusted and Privately trusted PKI](#)
  - [1.3 - Why choose a publicly trusted PKI?](#)
  - [1.4 - Why choose a privately trusted PKI?](#)
- [2 - What Is PKI Architecture? A Definition of PKI Architecture](#)
  - 
- [3 - The #1 Rule of PKI: You Do Not Talk About Your Private Key](#)
- [4 - One-, Two and Three-Tier Trust Hierarchies in PKI Architecture](#)
- [5 - Three (3) Examples of PKI Architecture (Uses and Diagrams)](#)
- [6 - How to implement a hybrid PKI solution on AWS](#)


> We’ll break down everything you need to know about public key infrastructure architectures and what they look like with examples of different PKI architecture diagrams and visuals

## `1 - What is Public Key Infrastruture (PKI)?`

Public key infrastructure, or PKI, is the (often unsung) hero of internet security. 

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/public-vs-private-comparison-0.png?raw=true" alt="Sublime's custom image"/>
</p>

- It’s the underlying framework that makes secure internet communications a reality through the use of public key encryption.

  

Fundamentally, a PKI has two functions:

- to manage a collection of public[02] and private keys, and
- to bind each key with the identity of an individual entity such as a person, or organization.

> Binding is established through the issuance of electronic identity documents, called digital certificates [03]. Certificates are cryptographically signed with a private key so that client software (such as browsers) can use the corresponding public key to verify a certificate’s authenticity (i.e. it was signed by the correct private key) and integrity (i.e. it was not modified in any way).



### `1.1 - First, How Does PKI Work`

> Public key infrastructure is a key part of your everyday life in the cyber world. It secures everything from the login credentials in your browser to the sensitive data you share via email — here’s a breakdown of how PKI works:

 <p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/how-pki-works-overview.png?raw=true" alt="Sublime's custom image"/>
</p>


 <p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/pki-1.png?raw=true" alt="Sublime's custom image"/>
</p>

- Public key infrastructure is intrinsic to cyber security. It’s the crust to your pie and the wind to your sail; basically, PKI is one of the things that makes cyber security work.

- Public key infrastructure, or PKI, is often talked about as a type of cyber security technology or framework — but it’s more than that. You likely know that the term relates to encryption, but do you actually know what it does or how PKI works?

There are two things PKI does to secure communications:

- **Authentication** — This ensures that the other party is the legitimate server/individual that you’re trying to communicate with.

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/authentication.png?raw=true" alt="Sublime's custom image"/>
</p>

- **Encryption** — This makes sure that no other parties can read your communications.

  <p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/encryption.png?raw=true" alt="Sublime's custom image"/>
</p>

To better understand how PKI works, we first need to make this whole process all a more understandable. So, let’s consider the SSL certificate that this website is using as an example. See the padlock icon in your browser? That means this website is using an SSL certificate, which is based on PKI. SSL uses PKI to do two things:

Your browser authenticates that it’s connected to the correct server that’s owned by example.com.

  <p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/pki-padlock.png?raw=true" alt="Sublime's custom image"/>
</p>


All of the data that passes between your browser and our web server is encrypted.

**In a more technical sense, PKI is a combination of cryptographic technologies, policies and procedures that you use to secure data in the digital world and to authenticate yourself. The term also relates to the issuance, use, storage, distribution, management, and revocation of digital certificates and keys — also known as the certificate lifecycle — as well as the entities that issue them.**

In a roundabout way, what all of this means is that public key encryption is a two-key (asymmetric) cryptosystem that protects everything you do and the information you send and receive online. From the ecommerce transactions on your website to the emails that you send within your organization that contain sensitive information, the data is secure thanks to PKI

> The main function of PKI is to distribute public keys to the right devices, software, and users who need them. This means that PKI is all about ensuring that your sensitive data doesn’t fall into the wrong hands.


### `1.2 - Publicly trusted and Privately trusted PKI`

While both PKI configurations provide the same function, their distinction is quite straightforward.

- Public PKIs are automatically trusted by client software,
- while private PKIs must be manually trusted by the user (or, in corporate and IoT environments, deployed to all devices by the domain administrator) before any certificates issued by that PKI can be validated.

An organization that maintains a publicly trusted PKI is called a Certificate Authority (CA). To become publicly trusted, a CA must be audited against standards such as the CA/B Forum’s Baseline Requirements [04] and be accepted into public trust stores like the Microsoft Trusted Root Store Program.

Although private PKI implementations can be just as secure as their public counterparts, they are not trusted by default because they are not provably compliant with these requirements and accepted into trust programs.

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/public-vs-private-pki-comparison.png?raw=true" alt="Sublime's custom image"/>
</p>

#### Publicly Trusted PKI. 
If you want your digital certificates to always be recognized and publicly trusted by clients and operating systems in public channels (i.e., on the internet), you’ll need to use digital certificates that are issued by a publicly trusted certificate authority. In this scenario, the PKI architecture is fully run by the certificate authority (i.e., you just put their certificates to work to secure public-facing resources), but we’ll still go over the basics if you’re curious.

##### Privately Trusted PKI. 
If you’re using PKI to secure internal assets or networks, then running a private CA might be the best option. In this scenario, you’ll need to make your own decisions about the PKI architecture — we’ll go over the basics of what you need to know in this article.


> Public-key infrastructure (PKI) is what makes internet encryption and digital signatures work. When you visit your bank website you are told it is encrypted and verified. 


### `1.3 - Why choose a publicly trusted PKI?`
- Being publicly trusted means that publicly trusted root certificates (associating the identity of a CA with their official public keys) are already distributed in most clients. Browsers, operating systems, and other client software are shipped with a built-in list of such trusted public keys that are used to validate certificates they encounter. 
- (Responsible vendors can also be expected to update these lists when updating their software.) In contrast, privately trusted root certificates (needed for a private PKI) must be manually installed in a client before certificates from such private PKIs can be validated.

> As a consequence, if you are trying to protect a publicly accessible web site or other on-line resource, a certificate issued from a publicly trusted PKI (i.e., a CA) is the way to go, since requiring each visitor to manually install a private PKI’s root certificate into their browser is not practical (and the consistent security warnings likely to result will negatively affect your site’s reputation).

### `1.4 - Why choose a privately trusted PKI?`

- Public PKIs must strictly follow regulations and undergo regular audits, while a privately trusted PKI may forgo auditing requirements and deviate from standards in any way its operator sees fit. Although this can mean that they do not follow the best practices as rigorously, it also allows customers using a private PKI more freedom regarding their certificate policies and operations.

> One example: the Baseline Requirements prohibit publicly trusted CAs to issue certificates for internal domains (e.g. example.local). A private PKI can, if desired, issue certificates for any domain as needed, including such local domains.

Publicly trusted certificates must also always include specific information in a manner strictly defined by their controlling regulations and formatted in a certificate profile mapping to the accepted X.509 standard for public certificates. However, some customers may require a custom certificate profile, specifically tailored to their organization’s anticipated uses and security concerns. A private PKI can issue certificates using a specialized certificate profile.

Apart from the certificate itself, private PKI allows for full control of the identity and credentials verification procedures as well. A customer’s own access control systems (such as single sign-ons or LDAP directories) can be integrated with the private PKI service to easily provide certificates to parties already trusted by the operator. In contrast, a publicly trusted PKI must perform strict manual and automated checks and validation against qualified databases before issuing any certificate

## `2 - What is PKI Architecture?`
-  Today we’re going to talk specifically about **PKI architecture** — *the systems, servers, and other stuff* that you need (most of which is found behind the scenes) — to harness the power of PKI for your business.

### `2.1 - 6 Key Components of Public Key Infrastructure (PKI)`

To better understand how PKI works, you first need to know what’s involved in it. Of course, there are several critical components within the public key infrastructure — and we’ll dive into each of these topics more in depth a little later in the article:

 #### `2.1.1 - X.509 digital certificates`
These types of certificates include a key, information about the identity of the owner (of the certificate and keys), and the digital signature of the certificate authority. These types of certificates include:
  - SSL/TLS website security certificates,
  - S/MIME (client authentication) certificates,
  - Code signing certificates, and
  - Document signing certificates.

    
#### `2.1.2 - Digital signatures`
 Digital signatures are what guarantees that a message, file, or data hasn’t been altered in any way. It uses an encrypted hash of a message to ensure the integrity of your data by making it so that nobody can modify the message without the recipient finding out.

#### `2.1.3 - Public and private key pairs (asymmetric and symmetric)`
 PKI works because of the key pairs that encrypt and decrypt data. In asymmetric encryption, there’s a public key that’s shared with everyone and a matching private key that’s kept secret. In symmetric encryption, there is one key that both parties use to communicate.

#### `2.1.4 - Certificate authorities (CAs)`
Certificate authorities are what make the whole PKI system trustworthy. CAs verify parties and issue certificates. Without CAs, PKI simply wouldn’t work because anybody could just issue certificates to themselves saying that they’re Amazon.com, Bill Gates, or whomever they feel like impersonating.

#### `2.1.5 - Chain of trust`
The chain of trust is a series of certificates (root, intermediate, and leaf certificates) that links back to the issuing CA who signed off on it.

 #### `2.1.6 - Proper certificate management tools, policies, processes, and procedures`
 This includes the use of a certificate management tools such as a certificate manager.

### `2.2 - The 3 Main Elements of Public Key Infrastructure (PKI)`


#### `2.2.1 - Digital certificates` 
- These are small digital files that enable identity and encryption for a variety of use cases on the internet. Each certificate contains a wealth of identifying information about the organization or entity it’s issued to (depending on the validation level it’s issued with) but has a finite lifespan. Common digital certificate categories include:
  - SSL/TLS certificates — These certificates are what make the secure padlock icons appear in your website visitors’ browsers and the “not secure” warnings disappear. SSL/TLS certificates come with three validation level options — domain validation (DV), organization validation (OV), and extended validation (EV).
  - Code signing certificates —These digital certificates help you secure your supply chain for software updates and offer users assurance that your software is legitimate and hasn’t been tampered with. Code signing certificates come with one of two validation levels — standard or extended validation — and the latter makes Windows Defender SmartScreen warnings disappear because they make your software automatically trusted by Windows operating systems and browsers!
  - Document signing certificates — These digital certificates use cryptographic functions (hashing) and digital signatures allow you to prove to users that your document is legitimate and hasn’t been altered since you signed it.
  - Email signing certificates — These digital certificates, also known as S/MIME certificates, provide end-to-end encryption by encrypting your email content and attachments prior to them leaving your inbox. Email signing certificates also provide digital identity by allowing you to digitally sign your messages so that your recipients can verify that the information hasn’t been altered and that it was actually you who sent it.
  - Client authentication certificates — These digital certificates enable passwordless authentication on your internal network. What this means is that authorized users can log in securely and verify their identities without having to remember or type in a cumbersome password and complete multi-factor authentication.


#### `2.2.2 - Public-private cryptographic key pairs`
These are the cryptographic tools you need to encrypt (public key) and decrypt (private key) information over the internet.
- Public key — This key encrypts data to prevent unauthorized access.
- Private key — This key decrypts data and is kept secret by the owner of the associated certificate.


#### `2.2.3 - Certification authorities` 
One of the key components of any PKI architecture is a certification authority, or what’s more commonly called a certificate authority or CA. An organization can rely on one or more CAs within its PKI. When people think of a CA, they traditionally think of it in the sense of a root CA or an issuing CA. However, there are also intermediate CAs as well. Here’s a quick description of each to help you differentiate between the three of them:

- Root CAs: A root CA depends on a root certificate, which must added to the trust store on every device that will be using the certificates you plan to issue for it to be trusted. Both public and private CAs have root CAs and certificates. Because all certificates tie back to these root certificates, CAs do everything within their power to keep their corresponding private keys secure. This typically involves storing root CA private keys offline in secure environments and by using hardware security modules (HSMs).
- Intermediate CAs: This type of CA serves as one or more links in the certificate chain and is digitally signed/issued by the root CA. They’re responsible for issuing endpoint certificates (like SSL/TLS certificates that you use to secure websites) to your organization. Essentially, intermediate CAs serve as the middleman between endpoint certificates and the root certificates they eventually chain back to.
- Issuing CAs: Sometimes, intermediate CAs and issuing CAs are one in the same and sometimes they’re separate. The difference depends on your CA hierarchy and how many tiers you have in your PKI architecture. (Read on to understand what we mean when we talk about PKI architecture tiers…)

PKI architecture exists in multiple forms depending on what you’re doing with PKI:






