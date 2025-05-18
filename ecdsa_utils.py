from random import randrange
from curves import secp256k1 as curve  
from ecdsa_utils_math import inverse_mod, scalar_mult, point_add
# Inverse mod using extended Euclidean algorithm
def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_s % p

# Elliptic curve scalar multiplication
def scalar_mult(k, point):
    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend) if result else addend
        addend = point_add(addend, addend)
        k >>= 1

    return result

# Point addition on the curve
def point_add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p[0] == q[0] and p[1] != q[1]:
        return None

    if p == q:
        m = (3 * p[0]**2 + curve.a) * inverse_mod(2 * p[1], curve.P)
    else:
        m = (q[1] - p[1]) * inverse_mod(q[0] - p[0], curve.P)

    m %= curve.P
    x = (m**2 - p[0] - q[0]) % curve.P
    y = (m * (p[0] - x) - p[1]) % curve.P
    return (x, y)

# ECDSA sign function
def sign(priv_key, z):
    k = randrange(1, curve.N)
    R = scalar_mult(k, curve.G)
    r = R[0] % curve.N
    k_inv = inverse_mod(k, curve.N)
    s = (k_inv * (z + r * priv_key)) % curve.N
    return (r, s)
