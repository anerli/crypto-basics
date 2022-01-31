'''
While RSA is still more frequently used today, ed25519 is a faster and more compact
(smaller keys) algorithm.

We can use ed25519 through the cryptography package for Python.

https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/
'''
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# Private key of user A
private_key = Ed25519PrivateKey.generate()

# User A signs this message
signature = private_key.sign(b"my authenticated message")

# User A's public key, available to anyone
public_key = private_key.public_key()

# Now anyone can verify that user A really signed this message!
public_key.verify(signature, b"my authenticated message")
# Raises InvalidSignature if verification fails