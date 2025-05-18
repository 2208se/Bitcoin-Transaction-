import hashlib
import base58
import hashlib
import base58

def hash160_to_address(hash160: bytes) -> str:
    """
    Converts a 20-byte hash160 (RIPEMD-160 of SHA-256) to a Bitcoin address.
    """
    version = b'\x00'  # 0x00 for mainnet
    payload = version + hash160

    # Double SHA-256 for checksum
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    full_payload = payload + checksum

    # Base58 encoding
    address = base58.b58encode(full_payload).decode()
    return address

def pubkey_to_address(pubkey):
    # Step 1: Compress the public key
    prefix = b'\x02' if pubkey[1] % 2 == 0 else b'\x03'  # pubkey[1] = y coordinate
    pubkey_compressed = prefix + pubkey[1].to_bytes(32, 'big')

    # Step 2: SHA-256
    sha = hashlib.sha256(pubkey_compressed).digest()

    # Step 3: RIPEMD-160
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha)
    hashed_pubkey = ripemd.digest()

    # Step 4: Add network byte (0x00 for mainnet)
    versioned = b'\x00' + hashed_pubkey

    # Step 5: Add checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
    full = versioned + checksum

    # Step 6: Base58 encode
    address = base58.b58encode(full)
    return address.decode()
