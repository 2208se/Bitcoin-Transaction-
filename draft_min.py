from keys import generate_keypair
from address import pubkey_to_address
from transaction import Tx, TxIn, TxOut
from script import p2pkh_script, create_script_sig
from ecdsa_utils import sign
from signatureVerification import verify_signature
import hashlib
from base58 import b58decode_check



def address_to_pubkey_hash(addr: str) -> bytes:
    return b58decode_check(addr)[1:]  # Removes version byte





# Step 1: Generate key pair and address
priv, pub = generate_keypair()
address = pubkey_to_address(pub)
print("Bitcoin Address:", address)

# Dummy previous tx details (normally you'd get this from the blockchain)
prev_tx = bytes.fromhex('aabbccdd' * 8)  # 32 bytes
prev_index = 0
amount = 50000  # satoshis
recipient_pubkey_hash = address_to_pubkey_hash('1B5gx6jokhFtF6VSpMq1ZESaRQNAYzBfXW')


# Step 2: Create transaction
tx_in = TxIn(prev_tx, prev_index)
tx_out = TxOut(amount, p2pkh_script(recipient_pubkey_hash))
tx = Tx(1, [tx_in], [tx_out])

# Step 3: Sign transaction
z = int.from_bytes(hashlib.sha256(tx.serialize()).digest(), 'big')
signature = sign(priv, z)
pub_bytes = pub[0].to_bytes(32, 'big') + pub[1].to_bytes(32, 'big')
script_sig = create_script_sig(signature, pub_bytes)

# Step 4: Attach unlocking script
tx.tx_ins[0].script_sig = script_sig

# Final serialized transaction
tx_bytes = tx.serialize()
print("Raw Transaction:", tx_bytes.hex())

# Step 5: Simulate verification (scriptPubKey: check address + check signature)
# Simulating that the scriptPubKey requires a specific pubkey hash

expected_address = pubkey_to_address(pub)
is_valid = verify_signature(pub, z, signature, expected_address=expected_address)
print("Signature valid and address match?", is_valid)

# Sanity checks
assert tx.serialize(), "Transaction should serialize"
assert is_valid, "Signature should be valid and pubkey should match address"
