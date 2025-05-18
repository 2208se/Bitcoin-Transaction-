# ecdsa_utils_math.py

from curves import secp256k1 as curve

def inverse_mod(a, p):
    """Compute the modular inverse of a modulo p."""
    return pow(a, -1, p)

def scalar_mult(k, P):
    """Multiply point P on the elliptic curve by scalar k."""
    result = (0, 0)  # Initialize the result as the identity point
    addend = P
    
    while k:
        if k & 1:
            result = point_add( result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    
    return result

def point_add(P, Q):
    """Add two points P and Q on the elliptic curve."""
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    
    # Using the secp256k1 curve equation for point addition
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2 and y1 == y2:
        # Point doubling
        m = (3 * x1 * x1) * inverse_mod(2 * y1, curve.P) % curve.P
    else:
        # Point addition
        m = (y2 - y1) * inverse_mod(x2 - x1, curve.P) % curve.P
    
    x3 = (m * m - x1 - x2) % curve.P
    y3 = (m * (x1 - x3) - y1) % curve.P
    
    return (x3, y3)
