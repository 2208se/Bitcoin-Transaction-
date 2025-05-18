def p2pkh_script(pubkey_hash):
    return (
        b'\x76'  # OP_DUP
        + b'\xa9'  # OP_HASH160
        + bytes([len(pubkey_hash)]) + pubkey_hash
        + b'\x88'  # OP_EQUALVERIFY
        + b'\xac'  # OP_CHECKSIG
    )



# script pubkey (locking script)= OP_DUP OP_HASH160 <recipient_pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG

# script sig (unlocking script) = <signature> <pubkey>
def create_script_sig(signature, pubkey):
    sig_bytes = signature[0].to_bytes(32, 'big') + signature[1].to_bytes(32, 'big')
    return (
        bytes([len(sig_bytes)]) + sig_bytes +
        bytes([len(pubkey)]) + pubkey
    )

