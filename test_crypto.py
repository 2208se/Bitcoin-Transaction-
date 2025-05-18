import unittest
from keys import generate_keypair
from address import pubkey_to_address
from transaction import Tx, TxIn, TxOut
from script import p2pkh_script, create_script_sig
from ecdsa_utils import sign
from signatureVerification import verify_signature
import hashlib

#) is a structured and automated way to validate the functionality of the Bitcoin transaction implementation. 
class TestBitcoinTransactionFlow(unittest.TestCase):
    def test_full_transaction_flow(self):
        # Step 1: Key Generation
        priv, pub = generate_keypair()
        self.assertIsInstance(priv, int)
        self.assertIsInstance(pub, tuple)
        self.assertEqual(len(pub), 2)
#Ensure that cryptographic keys (private and public) are generated correctly.




        # Step 2: Address Creation
        address = pubkey_to_address(pub)
        self.assertIsInstance(address, str)
        self.assertTrue(address.startswith('1'))  # legacy P2PKH format
        self.assertGreaterEqual(len(address), 26)  # base58 addresses vary in length
# Validate the creation of a Bitcoin address (P2PKH format).
        # Step 3: Create dummy TxIn
        prev_tx = bytes.fromhex('aabbccdd' * 8)  # 32 bytes
        prev_index = 0
        tx_in = TxIn(prev_tx, prev_index)

        # Step 4: Create TxOut with P2PKH script
        amount = 50000  # satoshis
        recipient_pubkey_hash = bytes.fromhex('f1d2d2f924e986ac86fdf7b36c94bcdf32beec15')
        tx_out = TxOut(amount, p2pkh_script(recipient_pubkey_hash))

        # Step 5: Construct Transaction
        tx = Tx(1, [tx_in], [tx_out])
        serialized = tx.serialize()
        self.assertIsInstance(serialized, bytes)
# Simulate a complete Bitcoin transaction 
        # Step 6: Sign the transaction hash
        z = int.from_bytes(hashlib.sha256(serialized).digest(), 'big')
        signature = sign(priv, z)
        self.assertIsInstance(signature, tuple)
        self.assertEqual(len(signature), 2)

        # Step 7: Build scriptSig and inject into TxIn
        pubkey_bytes = pub[0].to_bytes(32, 'big') + pub[1].to_bytes(32, 'big')
        script_sig = create_script_sig(signature, pubkey_bytes)
        tx.tx_ins[0].script_sig = script_sig

        # Step 8: Verify signature
        self.assertTrue(verify_signature(pub, z, signature))


if __name__ == '__main__':
    unittest.main()
