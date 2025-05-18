class Curve:
    def __init__(self, name, p, a, b, G, N):
        self.name = name
        self.P = p      # Prime field
        self.a = a      # Curve coefficient a
        self.b = b      # Curve coefficient b
        self.G = G      # Generator point
        self.N = N      # Order of the generator point

# secp256k1 parameters
secp256k1 = Curve(
    name="secp256k1",
    p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    a=0,
    b=7,
    G=(
        55066263022277343669578718895168534326250603453777594175500187360389116729240,
        32670510020758816978083085130507043184471273380659243275938904335757337482424
    ),
    N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
)
