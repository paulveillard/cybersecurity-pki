## PKI Architecture: Fundamentals of Designing a Private PKI System

## Table of Contents
- [1 - What Is PKI? A 2-Minute Review of a Few Key Concepts](#)
  - [1.1 - First, How Does PKI Work](#)
  - [1.2 - Publicly trusted and Privately trusted PKI](#)
  - [1.3 - Why choose a publicly trusted PKI?](#)
  - [1.4 - Why choose a privately trusted PKI?](#)
- [2 - What Is PKI Architecture? A Definition of PKI Architecture](#)
- [3 - The #1 Rule of PKI: You Do Not Talk About Your Private Key](#)
- [4 - One-, Two and Three-Tier Trust Hierarchies in PKI Architecture](#)
- [5 - Three (3) Examples of PKI Architecture (Uses and Diagrams)](#)
  - [PKI Architecture #1: Public CA](#)
  - [PKI Architecture #2: Private CA (Internal CA)](#)
  - [PKI Architecture #3: Managed PKI (mPKI or PKI-as-a-Service)](#)
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


## `5 - Three (3) Examples of PKI Architecture (Uses and Diagrams)`
PKI uses and applications vary from one business to the next. This section will explore each of these PKI architectures more in-depth and provide a diagram of each as a visual representation.

### `5.1 - PKI Architecture #1: Public CA`

When most people think of PKI architecture, their minds automatically go to public CAs. This includes companies like DigiCert, Sectigo, Entrust, and hundreds of others globally. However, the overwhelming majority of certificates are issued by a half dozen or so leading CAs.

Public certificate authorities are publicly trusted because they adhere to specific industry rules and requirements. As such, they’re able to issue certificates that are also publicly trusted by operating systems, browsers, and mobile devices.

The way it all works is like this:

- You (the PKI admin) request your public CA certificates for your website, endpoint devices, etc. from the public CA.
- All of the “magic” happens within the CA’s environment — they use their resources and personnel to validate your domain and/or organizational details.
- Once the public CA verifies your organizational information, they issue publicly trusted certificates that meet industry standards and requirements.
- Once the public CA issues the certificates, you must use your internal resources/personnel and follow internal policies to deploy the certificates across your public network.
  
Here’s a quick graphic that gives you a basic visual of what this process looks like:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/pki-architecture-when-using-public-ca.png?raw=true" alt="Sublime's custom image"/>
</p>

But what does a public CA’s PKI architecture actually look like? The CAs don’t like to disclose all the details of their architectures, but the following basic flowchart should give you a pretty basic idea of what it entails and how you interact with it:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/public-certificate-authority.png?raw=true" alt="Sublime's custom image"/>
</p>

An illustration of public key infrastructure and where you as a PKI administrator and your public CA of choice fit into the process. Everything that is highlighted in the blue dotted lines occurs behind the scenes so you don’t see it happening.
Just keep in mind that within that “Public CA’s Secure Facility” bubble, that the PKI architecture itself is typically a two-tier CA model, although some certificate authorities opt for three-tier — the latter is just less common.

While publicly trusted certificates are important and serve many uses, they can’t meet all of your organization’s security needs. After all, you have private network devices and apps you also need to secure, right? This is why many enterprises and organizations opt to create something known as a private PKI or a private CA.

### `5.2 - PKI Architecture #2: Private CA (Internal CA)`

**Private PKI, private CA, internal PKI, or internal CA** — these are all different terms that describe the same thing. So, whatever you want to call it, private PKI boils down to having the PKI structure in place to secure your websites, services, devices, and other IT resources on your network.

Want to issue private user authentication certificates that will be trusted within your network? Check. How about securing your virtual private network (VPN) access? Also check. IoT devices? Employee ID cards? Containerized environments? Check, check, check. At the risk of sounding like a late-night infomercial host, private PKI can be virtually everything you want it to be — you know, at least as far as securing your internal network and IT infrastructure goes.

So, what does a private PKI architecture look like? Here’s a basic overview of what all of that entails:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/private-pki-architecture.png?raw=true" alt="Sublime's custom image"/>
</p>

#### You Can Set Up a Private CA Using Microsoft CA and AWS ####

Running your own private CA checks many of the boxes that companies care about when it comes to IT and security and user management, and it gives you the greatest control of your PKI. You could use a resource like Microsoft CA, or what’s technically known as Active Directory Certificate Services (ADCS), to set up and manage your private PKI.

You can host your PKI on-prem or use a cloud-hosting provider such as Amazon Web Services (AWS) to host your Microsoft CA deployment, deploying your root and subordinate private CAs on Windows servers and using AWS Cloud HSM to sign your certs and store your private keys. This means you don’t have to go to the trouble and expense of setting up your own HSMs on-prem.

Let’s take a quick peek at how it looks when you set up your private PKI via AWS:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/hybrid-pki-solution-aws.png?raw=true" alt="Sublime's custom image"/>
</p>

An overview of a hybrid PKI solution via AWS. Image source for this PKI architecture diagram: Amazon Web Services.

For a closer look at the virtual private cloud (VPC) that is highlighted with the green box in the lower-right quadrant of the image and how that would look if you decided to go the cloud or hybrid PKI route, check out the following graphic:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/microsoft-pki-aws-architecture-diagram-1024x546.png?raw=true" alt="Sublime's custom image"/>
</p>

A screenshot of AWS’s Microsoft PKI diagram. Image source for this PKI architecture diagram: [Amazon Web Services](https://aws.amazon.com/blogs/security/how-to-implement-a-hybrid-pki-solution-on-aws/).

It’s important to note that the above PKI architectural graphic is really part of a quick start guide that doesn’t include recommended components such as an HSM. A true private PKI is more complicated, but this should at least help provide a basic idea of the architecture.

It’s important to note that the above PKI architectural graphic is really part of a quick start guide that doesn’t include recommended components such as an HSM. A true private PKI is more complicated, but this should at least help provide a basic idea of the architecture.

#### The Challenges of Setting Up Your Own Private PKI

But there is one huge caveat about running a private PKI: you have to have the budget, infrastructure, time, money, and skilled people to dedicate to it. As you can imagine, setting up and managing a private PKI costs way more than an infomercial’s magic price of $19.99. Properly managing your PKI takes a lot of time, labor, and resources for organizations of all sizes.

- Understaffing is a huge issue — data from Keyfactor and the Ponemon Institute’s State of Machine Identity Management Report 2021 shows that only 45% of companies say they have staff dedicated to managing their PKI.
- Many in-house teams don’t know how to securely manage a certificate authority because they don’t necessarily handle those responsibilities in their day-to-day jobs.
For these reasons (among others), many organizations that want to have their own PKIs wind up hiring managed PKI providers to handle setting one up and managing it for them.


### `5.3 - PKI Architecture #3: Managed PKI (mPKI or PKI-as-a-Service)`
Remember the 2009 phrase “There’s an App for That”? Well, the same can be said for the security services that you can outsource to experienced third-party providers, including the day-to-day management of your organization’s public key infrastructure. This is where a managed PKI service provider can make your work life a whole lot easier.

Several reputable CAs and PKI vendors offer what’s known within the industry as “PKI-as-a-service.” An mPKI provider is a third party that handles everything from setting up and rolling out your organization’s private CA to supporting it in the long run. They use their internal resources to facilitate this process.

Because this is what they eat, sleep, and breathe PKI all day, every day, they’re intimately familiar with all of the ins-and-outs of PKI that your team is unlikely to know or think about. They’re also very familiar with many of the issues you might face when setting up your PKI — and they have processes, procedures and policies in place to help mitigate them. 

But what does this look like in terms of PKI architecture? We’re glad you asked. Let’s take the basic private PKI architecture graphic we shared earlier and update it to reflect changes relating to managed PKI:

<p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/mpki-pki-architecture.png?raw=true" alt="Sublime's custom image"/>
</p>

> A basic illustrative PKI architecture diagram that showcases which responsibilities are areas your organization is responsible for versus your chosen mPKI provider.
> 
As your organization’s PKI administrator, as you can see, many of the typical responsibilities and monotonous tasks no longer fall squarely on your shoulders when you work with an mPKI provider. Instead, there are only select things that you’ll be partially or fully responsible for implementing and managing — your mPKI partner handles the rest. This means you don’t have to worry about having to know everything yourself or hiring someone to fill specific skills gaps. You can just lean on the mPKI professionals to take care of most things for you.

However, you still have full control over the things that matter to your organization, such as certificate profiles and validation requirements.

#### No Matter What Type of PKI Architecture You Have, You Need to Manage Your Certificates and Keys Carefully…

Now, there’s a really important sidenote we have to at least mention here: the effectiveness of your PKI depends on how well you manage your certificate and key lifecycle. The lifecycle encompasses everything from creating and managing certificates (and their corresponding keys) to those certificates’ reissuances or (infrequent) revocations.

This responsibility is a deciding factor in your organization’s security and compliance capabilities. As such, staying on top of your PKI’s certificate and key lifecycles is crucial in many ways. If even just one certificate expires on a public-facing system, or if a single private key gets compromised, you’ll be in for a world of hurt — you just might not know it right away…

Let’s consider what happened to Equifax back in 2017. Unbeknownst to Equifax’s IT security team, one of their digital certificates expired and they didn’t realize it until many months later. This led to a data breach that went undetected for two-and-a-half months and, ultimately, resulted in massive fines and settlement payments that the company is expected to pay.

Thankfully, there are some steps you can take to avoid many of these PKI management-related issues.

#### 5.3.1 Use an HSM to Securely Store Your CA Private Keys


These are the secure storage devices that help your organization keep your private keys safe. You can use an offline hardware security module (HSM) to store your root CA keys and an online HSM to store your intermediate CA keys for private PKI. But if you don’t want to go through the hassle of buying and setting up HSMs to use within your environment, a better option might be to use a managed PKI platform that’s built using HSMs.

#### 5.3.2 Use a PKI Management Tool to Manage Your Certificates and Keys

If you only have a handful of certificates and keys to track and manage, you can likely get away with using a spreadsheet to manage your PKI. But considering that another report from Keyfactor and the Ponemon Institute shows that organizations have an average of 88,750 certificates and keys in use on their networks, it’s impossible for full-time PKI admins to keep track of them all using manual means. This is why companies often use certificate management platforms to help them stay on top of their certificates, so nothing falls through the cracks.

