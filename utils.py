import hashlib
import base58

def pubkey_to_address(pubkey):
    # Compress pubkey: only use y's parity + x
    prefix = b'\x02' if pubkey[1] % 2 == 0 else b'\x03'
    compressed = prefix + pubkey[0].to_bytes(32, 'big')

    # Step 2: SHA256
    sha = hashlib.sha256(compressed).digest()

    # Step 3: RIPEMD-160
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha)
    hashed = ripemd.digest()

    # Step 4: Add version byte (0x00 for mainnet)
    versioned = b'\x00' + hashed

    # Step 5: Checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]

    # Step 6: Base58 encoding
    full = versioned + checksum
    address = base58.b58encode(full).decode()

    return address
