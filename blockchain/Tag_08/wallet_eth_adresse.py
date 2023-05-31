#Blockchain mit Generierung der ETH-Adresse
# ETH:
# 1. Private Key: 256-Bit-Zahl (random)
# 2. Public Key: wird aus dem Private Key abgeleitet (elliptische Kurve SECP256k1)
# 3. ETH-Adresse: wird aus dem Public Key abgeleitet (Hashfunktion: Keccak-256-Algo -> hashlib.sha3_256

import hashlib
import ecdsa
import base58

class Wallet:
    def __init__(self):
        self.private_key = ecdsa.util.randrange(pow(2,256))
        self.public_key = self.private_key_to_public_key()
        self.addresse = self.public_key_to_address()
        self.balance = 0
        self.transactions = []

    def private_key_to_public_key(self):
        signing_key = ecdsa.SigningKey.from_secret_exponent(self.private_key, curve=ecdsa.SECP256k1)
        verifying_key = signing_key.get_verifying_key()
        public_key = b'\x04' + verifying_key.to_string()
        return public_key


    def public_key_to_address(self):
        # Hash public key
        public_key_hash = hashlib.sha3_256(self.public_key).digest() # sha3_256 in ETH!
        address = '0x' + hashlib.new('ripemd160', public_key_hash).hexdigest()
        return address

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

    def display_blockchain(self):
        for block in self.chain:
            print("Transations:")
            for transaction in block.transactions:
                print(f"Sender: {transaction.sender}")
                print(f"Receiver: {transaction.receiver}")
                print(f"Amount: {transaction.amount}")
            print("Previoous Hash:", block.previous_hash)
            print()


wallet1 = Wallet()
wallet2 = Wallet()
wallet3 = Wallet()

print("Wallet 1 Private Key: ", hex(wallet1.private_key))
print("Wallet 1 Public Key: ", wallet1.public_key.hex())
print("Wallet 1 Address: ", wallet1.addresse)

print("Wallet 2 Private Key: ", hex(wallet1.private_key))
print("Wallet 2 Public Key: ", wallet1.public_key.hex())
print("Wallet 2 Address: ", wallet1.addresse)

print("Wallet 3 Private Key: ", hex(wallet1.private_key))
print("Wallet 3 Public Key: ", wallet1.public_key.hex())
print("Wallet 3 Address: ", wallet1.addresse)

# neue BC-Instanz
blockchain = Blockchain()

# transactions simulieren
transaction1 = Transaction(wallet1.addresse, wallet2.addresse, 10)
transaction2 = Transaction(wallet2.addresse, wallet3.addresse, 5)
blockchain.add_transaction(transaction1)
blockchain.add_transaction(transaction2)

# neuen block minen
blockchain.mine_block()

# BC display
blockchain.display_blockchain()
