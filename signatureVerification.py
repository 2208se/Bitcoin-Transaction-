from ecdsa_utils_math import inverse_mod, scalar_mult, point_add
from curves import secp256k1 as curve

def verify_signature(pubkey, z, signature):
    """
    Verifies the signature using ECDSA.

    :param pubkey: The public key to verify against.
    :param z: The hash of the transaction that was signed.
    :param signature: The (r, s) signature tuple to verify.
    :return: True if the signature is valid, False otherwise.
    """
    r, s = signature

    # Step 1: Check if r and s are within valid range
    if not (1 <= r < curve.N and 1 <= s < curve.N):
        return False

    # Step 2: Calculate the modular inverse of s
    s_inv = inverse_mod(s, curve.N)

    # Step 3: Calculate u1 and u2
    u1 = (z * s_inv) % curve.N
    u2 = (r * s_inv) % curve.N

    # Step 4: Calculate R = u1 * G + u2 * pubkey
    G = curve.G
    R = point_add(scalar_mult(u1, G), scalar_mult(u2, pubkey))

    # Step 5: If R is None or R.x does not match r, the signature is invalid
    if R is None or R[0] % curve.N != r:
        return False

    return True
