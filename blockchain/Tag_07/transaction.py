import time

class Transaction:

    def __init__(self, sender, receiver, amount):

        self.sender = sender # Sender der Coins
        self.receiver = receiver # Empfänger der Coins
        self.amount = amount # Betrag

        # zusätzlich
        self.time = time.time() # wann wurde diese Transaktion durchgeführt
