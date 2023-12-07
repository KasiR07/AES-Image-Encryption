# Abstarct
Nowadays the use of devices such as computers, mobile and many other devices for communication as well as for data storage and transmission has increased. As a result, there is an increase in the number of users. Along with these users, there is also an increase in the number of unauthorized users who are trying to access the data by unfair means. This raises the problem of data security. Images are sent over an insecure transmission channel from different sources, some image data contains secret data, some images itself are highly confidential hence, securing them from any attack is essentially required.

# Introduction
Advanced encryption standard (AES) is one of the widely used symmetric encryption algorithms. It is an encryption standard adopted by the US government .Every password manager uses an algorithm for encryption and decryption. The algorithm has to be carefully chosen to satisfy the application needs. AES uses 128 bit block size at once and uses a key of length 128,192 or 256 bits to attain security. Images are sent over an insecure transmission channel from different sources, some image data contains secret data, some images itself are highly confidential hence, securing them from any attack is essentially required. Here, we will be working on encrypting images with the AES algorithm to enhance security over non-secure networks .

# System Design
We will implement this project in python, including the frontend. The app will ask for an image that has to be encrypted with the key. Once it's encrypted it can be sent to the client which can be unlocked by them. The image encrypted will have less loss in quality. There are two modules in this paper, i.e., Encryption and Decryption. First, we will look into the AES algorithm for encrypting and decrypting the image:

![image](https://github.com/KasiR07/AES-Image-Encryption/assets/108777263/cc8277b3-4fb0-46c9-8bf8-30544f41ab49)

the AES algorithm while encryption, takes the in the plaintext, which in this case will be the byte array of the image that will be encrypted and a key. Following that are the rounds of encryption where there are different functions and the blocks are transformed. A similar process is done in the decryption phase where the cipher text is taken along with the key to perform the decryption process where the functions in the blocks are inverse.
