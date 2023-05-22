# Übngsaufgabe zum Thema PoW

# Module importieren
import time
from hashlib import sha256
from transaction import Transaction

# Beispiel zu time
# wieviele Sekunden sind vergangen seit dem 1.1.1970 (Unix-Timestamp)
# print(time.time()) # 1684747241.81151

# Difficulty festlegen
difficulty = 2



# Aufgabe 1: Klasse Block erzeugen
class Block():
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        computed_hash = ""

        while not computed_hash.startswith("0" * difficulty):
            self.nonce += 1
            string_to_hash = "{0} {1} {2} {3}".format(
                self.index,
                self.transactions,
                self.timestamp,
                self.previous_hash,
                self.nonce
            )
            # string_to_hash = self.transactions + str(self.nonce)
            computed_hash = sha256(string_to_hash.encode("utf-8")).hexdigest()

        return computed_hash

blockchain = []

# mempool (vor-blockchain)
transaktionen = []

genesis_block = Block(0, "Ich bin Genesis Block", time.time(), "0")

blockchain.append(genesis_block)

transaktion1 = "Ich bin ein String aber du kannst mich Transkation nennen."


transaktionen.append(transaktion1)

# block1 = Block(1, transaktion1, time.time(), previous_hash=genesis_block)

block1 = Block(len(blockchain), transaktion1, time.time(), blockchain[-1].hash)

blockchain.append(block1)

block2 = Block(len(blockchain), "Ich bin Blockie Block", time.time(), blockchain[-1].hash)

blockchain.append(block2)

transaktionen = []

print("Anzahl der Block in BC:", len(blockchain))


for block in blockchain:
    print("Nonce:", block.nonce)
    print(block.transactions)
    print("Hash:",block.hash)
    print("Prev_Hash:", block.previous_hash)

# folgende Eigenschaften per Konstruktor:
# - index (laufende Nummer für den Block, zB 0 für den Genesisblock)
# - transactions (Liste aus Transaktions-Daten, hier: Liste aus Strings für den jew. Block)
# - timestamp
# - previous_hash (Hash vom vorherigen Block, bei Genesis: "0" ähnlich wie Handelsblatt-Tool)

# zusätzlich (also OHNE Parameter im Konstruktor)
# - self.nonce mit default: 0
# - hash (der eigene Block-Hash auf Grundlage o.g. Eigenschaften dank PoW)
# zB self.hash = self.calculate_hash() - also mit String des Hashs als Rückgabewert

# Methode
# calculate_hash() - zum Berechnen eines gültigen Hashs in Rücksicht von Difficulty und self.nonce
# also der Proof-of-Work


# Blockchain erzeugen (hier nichts anderes als eine Liste von Block-Objekten)
# blockchain = []

# aktuell offene Transaktionen (sogenannter Mempool)
# transaktionen = []

# Aufgabe 2: einige Transaktionen erzeugen und einige Blöcke generieren

# Bsp.:
# Transaktion erzeugen
# transaktion1 = "Petra schickt Ingo 5 Coins"
# diese Transaktion in Mempool ablegen
# transaktionen.append(transaktion1)

# Block erzeugen
# genesis_block = Block(0, transaktionen, time.time(), "0") # index, transactions, timestamp, previous_hash
# neuen Block der Blockchain hinzufügen
# blockchain.append(genesis_block)
# wichtig: immer wenn ein Block erzeugt wurde und der Blockchain hinzugefügt wurde, Mempool leeren
# transaktionen = []

# Aufgabe 3: am Ende die komplette Blockchain per Schleife auflisten, also alle Blöcke der BC einsehen


# später mit mir gemeinsam einen Manupulations-Versuch an der BC vornehmen

# Zeit: insgesamt ca. 1 Stunde (Kaffeepause von 12:00 bis 12:15) - gemeinsame Besprechung ab 14:05
# bei Fragen bin ich in Raum 1
