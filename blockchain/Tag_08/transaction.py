import hashlib
import ecdsa
import base58

class Wallet:
    def __init__(self):
        self.private_key = ecdsa.util.randrange(pow(2,256))
        self.public_key
        self.addresse
        self.balance = 0
        self.transactions = []

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

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self. receiver = receiver
        self.amount = amount

class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_string = "".join(str(transaction.__dict__) for transaction in self.transactions)
        data = str(self.previous_hash) + transaction_string
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([], "0")

    def add_transaction(self, transaction):
        self.chain[-1].transactions.append(transaction)

    def mine_block(self):
        transactions = self.chain[-1].transactions
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)
