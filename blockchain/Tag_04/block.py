import time
from hashlib import sha256

difficulty = 3

class Block:

    def __init__(self, index, transactions, previous_hash, hash): # vorerst OHNE proof-of-work

        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash

        self.hash = hash.calculate_hash()

        self.time = time.time()

        self.nonce = 0 # vorerst OHNE proof-of-work, also Nonce aktuell IMMER bei 0 in unserer Demo

    def calculate_hash(self):
        computed_hash = ""

        while not computed_hash.startswith("0" * difficulty):
            self.nonce += 1
            string_to_hash = "{0} {1} {2} {3} {4}".format(
                self.index,
                self.transactions,
                self.time,
                self.previous_hash,
                self.nonce
            )

            computed_hash = sha256(string_to_hash.encode("utf-8")).hexdigest()

        return computed_hash
