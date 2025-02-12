## PKI Architecture: Fundamentals of Designing a Private PKI System

## Table of Contents
- [1 - What Is PKI Architecture? A Definition of PKI Architecture](#)
- [2 - What Is PKI? A 2-Minute Review of a Few Key Concepts](#)
  - [How PKI Works](#)
- [3 - The #1 Rule of PKI: You Do Not Talk About Your Private Key](#)
- [4 - One-, Two and Three-Tier Trust Hierarchies in PKI Architecture](#)
- [5 - Three (3) Examples of PKI Architecture (Uses and Diagrams)](#)
- [6 - How to implement a hybrid PKI solution on AWS](#)


> We’ll break down everything you need to know about public key infrastructure architectures and what they look like with examples of different PKI architecture diagrams and visuals


Public key infrastructure, or PKI, is the (often unsung) hero of internet security. 
- It’s the underlying framework that makes secure internet communications a reality through the use of public key encryption. Today we’re going to talk specifically about **PKI architecture** — *the systems, servers, and other stuff* that you need (most of which is found behind the scenes) — to harness the power of PKI for your business.

PKI architecture exists in multiple forms depending on what you’re doing with PKI:

#### Publicly Trusted PKI. 
If you want your digital certificates to always be recognized and publicly trusted by clients and operating systems in public channels (i.e., on the internet), you’ll need to use digital certificates that are issued by a publicly trusted certificate authority. In this scenario, the PKI architecture is fully run by the certificate authority (i.e., you just put their certificates to work to secure public-facing resources), but we’ll still go over the basics if you’re curious.

##### Privately Trusted PKI. 
If you’re using PKI to secure internal assets or networks, then running a private CA might be the best option. In this scenario, you’ll need to make your own decisions about the PKI architecture — we’ll go over the basics of what you need to know in this article.


Public-key infrastructure (PKI) is what makes internet encryption and digital signatures work. When you visit your bank website you are told it is encrypted and verified. 

## How PKI Works

Most have heard the names of Verisign, Network Solutions, and GoDaddy. These companies along with many more are in the business of allowing the public to trust an organization's encryption keys and are referred to as Registration Authorities (RA)
 

If an organization, let’s say your bank, wants to encrypt their website that you use to manage your accounts they would first need to generate a private encryption key. The private key is something that should remain just that; private. With the private key one can extract a public key. While a public key can be created from a private key, the reverse should not be possible. 
 
 <p align="center">
  <img src="https://github.com/paulveillard/cybersecurity-pki/blob/main/img/pki-1.png?raw=true" alt="Sublime's custom image"/>
</p>

Now the fun part, any messages encrypted using this private key can be decrypted via the public key and vice versa. The bank now decides that they want a third party to verify the authenticity of their private/public key pair because without it their users get a warning in their web browser stating that the site shouldn’t be trusted. I am sure most of you have seen this error before:

The bank sends their public key to an RA and pays for them to digitally sign it with their Root Certificate Authority (CA). This CA is nothing more than another public/private key pair. Remember how I said that anything encrypted with a private key can be decrypted with the public key? At the time it may not have sounded like a good idea to have any message encrypted that can be decrypted by anyone. In this case, the RA is the only one with access to their private key and everyone has their public key (You literally do have it, every modern operating system maintains a copy of these trusted Root Certificates). The RA adds a message to the bank’s public key using their private key with the goal that your web browser should now be able to decrypt and view the message. If this is all successful, you do not see the nasty page like the image above and you can be assured that this site is using a certificate that the third party has verified..

So you now have your bank’s public key. This means you can encrypt a message with it and only the bank can see that message using their private key. The bank does the same thing to send you messages. When you initiate a connection with a web browser to a site that uses HTTPS, you also send your own public key to your bank. They will use that to encrypt messages and send back to you for you to decrypt using your private key. Since you do not need to supply any authenticity of who you are to the website, there is no problem with your public/private keys being generated dynamically.

Lastly, public/private key encryption is wildly inefficient due to the existence of the public key. In order for the public key to be securely derived from the private, we have to use very large key sizes. At the time of this article I recommend 4096-bit key size. 

So why do we use PKI if it is so inefficient?

This sort of encryption is also referred to as asymmetric encryption. Symmetric encryption is much more efficient, but has one flaw; both sides need to know what the private key is. The purpose of PKI is the means for two endpoints to securely decide on a symmetric key to use to continue communication; usually a 128-bit or 256-bit key.  

To summarize:

You type in your bank’s address in your web browser
Your web browser provides your bank with its public key.
Your bank responds with its public key
Your web browser checks it’s list of Root Certificates to try to decrypt the digital signature
If successful, both sides run through a series of algorithms and exchanges to derive the same symmetric key to be used for the rest of communication within this session.
At this point, your bank’s website finally appears in your browser and any communication henceforth will be encrypted using the symmetric key.

## Security Concerns

So what benefit does a company get when a root certificate authority is used to verify the public key a server presents to a client? The answer is more human than you would think. When a self-signed certificate is used, a user gets that nasty warning I discussed earlier. If this warning is disregarded and the user continues to the site, the communication between the server and client is still encrypted. 

However, If we train our users to ignore those security warnings about the inability to prove the authenticity of the server’s public key then our users will always ignore this error. In 99.999% of cases this is probably okay, but what can potentially happen is what is known as a Man-In-The-Middle(MITM) attack. 

Using the brief description of PKI above, imagine if there was a malicious user somewhere on the internet, or more likely somewhere locally, placed directly between your computer and the server. When the initial key exchange takes place the attacker can intercept your public key, and send you theirs instead of the server’s of which you are trying to talk to. His public key will most likely not be digitally signed with the same domain name as the site you are visiting, although if this was a targeted attack on a particular server it could be possible. 

Since the attacker likely wants to steal data, he will then proxy a connection to the server your originally wanted to go to, but instead of your public key going to the server it would be the attacker’s. This places the attackers computer directly between you and the server and will be able to capture and view any data sent between both machines. Well, that is if the user has been trained to simply ignore the warning they got from their web browser.
