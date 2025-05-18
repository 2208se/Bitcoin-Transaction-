# main.py
from keys import generate_keypair
from address import pubkey_to_address, hash160_to_address
from transaction import Tx, TxIn, TxOut
from script import p2pkh_script, create_script_sig
from ecdsa_utils import sign
from signatureVerification import verify_signature
import hashlib

# Step 1: Generate key pair and address (Sender)
priv, pub = generate_keypair()
sender_address = pubkey_to_address(pub)
print("Sender's Bitcoin Address:", sender_address)

# Dummy previous tx details (normally you'd get this from the blockchain)
prev_tx = bytes.fromhex('aabbccdd' * 8)  # also 32 bytes
prev_index = 0
amount = 50000  # satoshis

# Step 2: Define recipient address
recipient_pubkey_hash = bytes.fromhex('f1d2d2f924e986ac86fdf7b36c94bcdf32beec15')
recipient_address = hash160_to_address(recipient_pubkey_hash)
print("Recipient's Bitcoin Address:", recipient_address)

# Step 3: Create transaction
tx_in = TxIn(prev_tx, prev_index)
tx_out = TxOut(amount, p2pkh_script(recipient_pubkey_hash))
tx = Tx(1, [tx_in], [tx_out])

# Step 4: Sign transaction
z = int.from_bytes(hashlib.sha256(tx.serialize()).digest(), 'big')
signature = sign(priv, z)
script_sig = create_script_sig(signature, pub[0].to_bytes(32, 'big') + pub[1].to_bytes(32, 'big'))

# Step 5: Plug scriptSig into input
tx.tx_ins[0].script_sig = script_sig

# Final tx bytes
tx_bytes = tx.serialize()
print("\nRaw Transaction:", tx_bytes.hex())

# Step 6: Verify the signature
is_valid = verify_signature(pub, z, signature)
print("\nSignature valid?", is_valid)

# Step 7: Verify sender's address matches the public key
computed_address = pubkey_to_address(pub)
address_match = (computed_address == sender_address)
print("Sender's Address match? ", address_match)


if address_match and is_valid:
    print("\nTransaction is valid and signed by the sender. Transaction passed successfully!")


assert tx.serialize(), "Transaction should serialize"
assert is_valid, "Signature should be valid"
assert address_match, "Sender's address should match the public key"
