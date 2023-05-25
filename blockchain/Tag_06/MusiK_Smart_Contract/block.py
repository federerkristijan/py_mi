import time
from hashlib import sha256

difficulty = 3

class Block:

    def __init__(self, index, transactions, previous_hash):

        self.index = index
        self.transactions = transactions
        #self.merkle_root = GesamtHash von allen Transactions
        self.previous_hash = previous_hash

        self.nonce = 0

        self.time = time.time()

        self.hash = self.calculate_hash()


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
