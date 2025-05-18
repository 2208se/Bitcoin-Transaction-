# Bitcoin-Transaction-
This project is a simplified implementation of a Bitcoin transaction system in Python, covering the core cryptographic principles of Bitcoin, including key generation, transaction creation, signing, and verification. The focus is on educational clarity, making the complex mechanics of Bitcoin understandable and accessible.

Features:
Generates a secure private key and corresponding public key using Elliptic Curve Cryptography (secp256k1).

Derives a Bitcoin address from the public key using hashing (SHA-256 and RIPEMD-160).

Constructs a Bitcoin transaction with inputs (source UTXOs) and outputs (destination address + amount).

Signs the transaction using ECDSA (Elliptic Curve Digital Signature Algorithm).

Attaches the signature (ScriptSig) to the transaction.

Verifies the transaction using a process similar to Bitcoin’s ScriptPubKey and ScriptSig model.

**📁 Project Structure:**
bash
Copier
Modifier
simplified_bitcoin_transaction/
├── main.py              # Main script to create and verify a transaction
├── keys.py              # Key generation (private/public keys)
├── address.py           # Bitcoin address creation from public key
├── transaction.py       # Transaction creation and structure
├── ecdsa_utils_math.py  # Mathematical utilities (ECC operations)
└── README.md            # Project documentation (this file)


**⚡ Getting Started:**
1️⃣ Clone the Repository:
bash
Copier
Modifier
git clone https://github.com/yourusername/simplified_bitcoin_transaction.git
cd simplified_bitcoin_transaction
2️⃣ Install Required Libraries:
bash
Copier
Modifier
pip install base58 ecdsa
3️⃣ Run the Main Program:
bash
Copier
Modifier
python main.py




** How It Works:**
Generates a private key (256-bit random number).

Derives the public key using Elliptic Curve Cryptography (secp256k1).

Creates a Bitcoin address from the public key (SHA-256, RIPEMD-160, Base58).

Builds a transaction with:

An input (previous UTXO reference)

An output (recipient address + amount)

Signs the transaction using the private key (ECDSA).

Attaches the signature (ScriptSig) to the transaction.

Verifies the transaction using the public key and the signature.




**🔧 How It’s Built:**
Elliptic Curve Cryptography (secp256k1): Used for key generation (public/private).

SHA-256 + RIPEMD-160: Used for secure Bitcoin address creation.

ECDSA (Elliptic Curve Digital Signature Algorithm): Used for signing and verifying transactions.

Simplified ScriptSig and ScriptPubKey Model: Simulates Bitcoin’s locking and unlocking mechanism.



**🛡️ Security Note:**
This project is for educational purposes. It does not implement advanced security practices required for a production-level cryptocurrency system.

Never use the private keys generated here for real Bitcoin transactions.
