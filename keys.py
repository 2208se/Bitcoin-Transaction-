# keys.py

from secrets import randbelow
from ecdsa_utils import scalar_mult
from curves import secp256k1  # Import secp256k1 curve

def generate_keypair():
    priv = randbelow(secp256k1.N)  # Use secp256k1.N as the range for the private key y2 = x3 +7 (mod p)



    pub = scalar_mult(priv, secp256k1.G)  # Use secp256k1.G for the public key generation
    return priv, pub
