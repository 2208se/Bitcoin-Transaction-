import struct
import hashlib

def int_to_little_endian(n, length):
    return n.to_bytes(length, 'little')

def little_endian_to_int(b):
    return int.from_bytes(b, 'little')

def encode_varint(i):
    if i < 0xfd:
        return bytes([i])
    elif i < 0x10000:
        return b'\xfd' + int_to_little_endian(i, 2)
    elif i < 0x100000000:
        return b'\xfe' + int_to_little_endian(i, 4)
    elif i < 0x10000000000000000:
        return b'\xff' + int_to_little_endian(i, 8)
    else:
        raise ValueError(f'integer too large: {i}')

class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=b'', sequence=0xffffffff):
        self.prev_tx = prev_tx  # bytes
        self.prev_index = prev_index  # int
        self.script_sig = script_sig  # bytes
        self.sequence = sequence

    def serialize(self):
        result = self.prev_tx[::-1]  # little endian
        result += int_to_little_endian(self.prev_index, 4)
        result += encode_varint(len(self.script_sig))
        result += self.script_sig
        result += int_to_little_endian(self.sequence, 4)
        return result

class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey

    def serialize(self):
        result = int_to_little_endian(self.amount, 8)
        result += encode_varint(len(self.script_pubkey))
        result += self.script_pubkey
        return result

class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime=0):
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.locktime = locktime

    def serialize(self):
        result = int_to_little_endian(self.version, 4)
        result += encode_varint(len(self.tx_ins))
        for tx_in in self.tx_ins:
            result += tx_in.serialize()
        result += encode_varint(len(self.tx_outs))
        for tx_out in self.tx_outs:
            result += tx_out.serialize()
        result += int_to_little_endian(self.locktime, 4)
        return result
