'''
Here's a simple example showing how a stored hash is sufficient to verify a password,
rathing that having to store the actual password text.
'''
import hashlib

password = input("Enter a password: ")

# Hash the password
hashed = hashlib.sha256(password.encode()).digest()
# .encode() converts the string to bytes

# Don't need to store the actual password
# (Irrelevant here, just proving a point that we don't need this)
del password

confirm_password = input("What is your password? ")

confirm_hashed = hashlib.sha256(confirm_password.encode()).digest()

if (hashed == confirm_hashed):
    print("Correct!")
else:
    print("Incorrect!")
    