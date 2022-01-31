'''
SHA-256 is an algorithm for converting data to a hash.
This is a one-way operation that can be used to confirm that the hash of some sensitive data
matches what it should be, or for storing the hashes of passwords.
There is no randomness with this function, every input should always provide the same output.

Python's hashlib module from the standard library provides a method for this.

More info on SHA-256: https://www.n-able.com/blog/sha-256-encryption#:~:text=SHA%2D256%20is%20a%20patented,that%20is%20256%20bits%20long.&text=In%20hashing%2C%20by%20contrast%2C%20data,string%20through%20SHA%2D256%20hashing.
Documentation for hashlib: https://docs.python.org/3/library/hashlib.html
'''

import hashlib

# Initialize hashing object
m = hashlib.sha256()
# A 'b' in front of quotes in Python converts the string to byte data which is needed by the hash function.
m.update(b"This is my data!")

print("Hash in bytes: ", m.digest())
print("We can see we get bytes back: ", type(m.digest()))

print("Size of resulting hash, in bytes: ", m.digest_size)