import time

class Block:

    def __init__(self, index, transactions, previous_hash, hash): # vorerst OHNE proof-of-work

        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash

        self.hash = hash

        self.time = time.time()

        self.nonce = 0 # vorerst OHNE proof-of-work, also Nonce aktuell IMMER bei 0 in unserer Demo
