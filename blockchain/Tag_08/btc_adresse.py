# Genereierung der Bitcoin-Adresse
# 1. Private Schlüssel
# - zufällig generierte 256-Bit-Zahl
# 2. Öffentlicher Schlüssel
# - wird aus dem privaten Schlüssel mithilfe mathematischer Berechnung (ECC) abgeleitet
# 3. Adresse
# - wird aus dem öffentlichen Schlüssel abgeleitet

import hashlib
import ecdsa # from random import randrange inklusive
import base58


def generate_private_key():
    private_key = ecdsa.util.randrange(pow(2,256))

    return private_key

def private_key_to_public_key(private_key):

    signing_key = ecdsa.SigningKey.from_secret_exponent(private_key, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    public_key = b'\x04' + verifying_key.to_string()
    return public_key


def public_key_to_address(public_key):
    # Hash public key
    public_key_hash = hashlib.sha256(public_key).digest()

    # Perform RIPEMD-160 hashing
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(public_key_hash)
    hashed_public_key = ripemd160.digest()

    # Add version byte (0x00)
    version_byte = b'\x00'
    hashed_public_key_with_version = version_byte + hashed_public_key

    # Perform double SHA-256 hashing
    sha256_hash = hashlib.sha256(hashed_public_key_with_version).digest()
    double_sha256_hash = hashlib.sha256(sha256_hash).digest()

    # Checksum (4 bytes)
    checksum = double_sha256_hash[:4]
    address_bytes = hashed_public_key_with_version + checksum

    # Encode durch Base58
    address = base58.b58encode(address_bytes)
    return address.decode('utf-8')

private_key = generate_private_key()

print(private_key)

public_key = private_key_to_public_key(private_key)

print(public_key.hex())

address = public_key_to_address(public_key)

print(address)
