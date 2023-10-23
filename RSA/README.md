# RSA

Toy algorithm to encrypto and decrypt using the RSA method of large primes

Set p1 and p2 to large primes.  
Choose a public key.  
Set *encrypt* to 1 to encrypt and to 0 to decrypt.  

ord() is used to convert char to ints and have a range of 0 to 1114111.  
Ideally, the totient (p1-1)(p2-1) should be bigger than 1114111.  
But having the totient bigger than 150 should cover most used characters.  

Todo: convert to QR and immediately be able to read provided you know p1,p2 and pub