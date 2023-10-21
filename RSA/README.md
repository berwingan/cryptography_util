#RSA

Toy algorithm to encrypto and decrypto using the RSA methods of large primes

Set p1 and p2 to large primes.
Choose a public key.
Set encrypt to 1 to encrypt and to 0 to decrypt.

ord() is used to convert char to ints and have a range of 0 to 1114111
Ideally, the totient (p1-1)(p2-1) should be bigger than 1114111.
But having the totient bigger than 150 should cover most used characters.