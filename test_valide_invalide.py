import unittest
from ecdsa_utils import sign
from signatureVerification import verify_signature
from keys import generate_keypair
import hashlib

# testing if the signature verification works correctly
# This test suite will check both valid and invalid signatures
class TestCrypto(unittest.TestCase):

    def test_valid_signature(self):
        priv, pub = generate_keypair()
        # Create a dummy transaction
        tx = b"dummy_transaction_data"
        z = int.from_bytes(hashlib.sha256(tx).digest(), 'big')
        
        # Sign the transaction
        signature = sign(priv, z)
        
        # Verify the valid signature
        is_valid = verify_signature(pub, z, signature)
        print("Valid signature verification result:", is_valid)
        self.assertTrue(is_valid)

    def test_invalid_signature(self):
        priv, pub = generate_keypair()
        # Create a dummy transaction
        tx = b"dummy_transaction_data"
        z = int.from_bytes(hashlib.sha256(tx).digest(), 'big')
        
        # Sign the transaction
        signature = sign(priv, z)
        
        # Tampering with the signature (modify one of the signature values)
        tampered_signature = (signature[0], signature[1] + 1)  # Modify 's'
        print("Original Signature:", signature)
        print("Tampered Signature:", tampered_signature)
        
        # Verify the tampered signature (should be invalid)
        is_valid = verify_signature(pub, z, tampered_signature)
        print("Tampered signature verification result:", is_valid)
        self.assertFalse(is_valid)


if __name__ == "__main__":
    unittest.main()
