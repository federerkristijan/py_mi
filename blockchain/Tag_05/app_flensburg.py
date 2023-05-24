# Spielwiese für smart contracts - am Beispiel einer Flensburg-Blockchain
# Bsp.: Führerswchein-Entzug wenn wiederholt auffällig (zB über rot oder zu schnell)

# https://www.bussgeldkatalog.de/geschwindigkeit/

# Module
from node import Node
from account import Account
from block import Block

from transaction_flensburg import Transaction
from smart_contract_flensburg import SmartContract

from hashlib import sha256 # für die Verschlüsselung von Füherschein-ID

import random

# man könnte jetzt Nodes erzegen für ein P2P-Netwerk (Flensburg-Blockchain ist aber idR eine private Blockchain)
# daher KEIN PoW zwingend notwendig

# Blockchain erzeugen
blockchain = []

# Genesis-Block
blockchain.append(Block(0, [], "0000000000", "3fa8a90ec59766fb5abd788313751a858455ce3b9fd70e3955557be28075356c"))

# offene Transaktionen (Mempool)
transaktionen = []

# Zugriff auf Smart Contract erlauben
smart_contract = SmartContract()

# Petra fährt über rote Ampel
# Transaktions-Daten (werden vom Polizisten eingetragen): driving_license_id, violation_type, violation_date
# dabei die Führerschein-ID hier aus Datenschutzgründen verschlüsseln
driving_license_id = sha256("Petra123".encode("utf-8")).hexdigest()
print(driving_license_id)
violation_type = "rote Ampel"
violation_date = "24. Mai 2023 11:53"

transaktion1 = Transaction(driving_license_id, violation_type, violation_date) # eine noch offene Transaktion
# jetzt den smart contract an die offene Transaktion anwenden
smart_contract.apply(transaktion1, blockchain)

transaktion1 = Transaction(driving_license_id, violation_type, violation_date) # eine noch offene Transaktion
print(transaktion1.__dict__) # Transaktionsdaten VOR dem apply()
# jetzt den smart contract an die offene Transaktion anwenden
smart_contract.apply(transaktion1, blockchain)
print(transaktion1.__dict__) # Transaktionsdaten NACH dem apply()

transaktionen.append(transaktion1)

# neuen Block erzeugen
blockchain.append(Block(len(blockchain), transaktionen, blockchain[-1].hash, "211d0bb8cf4f5b5202c2a9b7996e483898644aa24714b1e10edd80a54ba4b560"))

# Mempool leeren
transaktionen = []

# weiterer Verstoß für Petra (fährt zu schnell)
driving_license_id = sha256("Petra123".encode("utf-8")).hexdigest()
violation_type = "50 km/h innerorts zu schnell"
violation_date = "24. Mai 2023 12:27"

transaktion1 = Transaction(driving_license_id, violation_type, violation_date) # eine noch offene Transaktion
print(transaktion1.__dict__) # Transaktionsdaten VOR dem apply()
# jetzt den smart contract an die offene Transaktion anwenden
smart_contract.apply(transaktion1, blockchain)
print(transaktion1.__dict__) # Transaktionsdaten NACH dem apply()
print()

# ein Verstoß von Bob (zu schnell)
driving_license_id = sha256("Bob123".encode("utf-8")).hexdigest()
violation_type = "70 km/h außerorts zu schnell"
violation_date = "24. Mai 2023 12:30"
transaktion2 = Transaction(driving_license_id, violation_type, violation_date)
print(transaktion2.__dict__) # Transaktionsdaten VOR dem apply()
# jetzt den smart contract an die offene Transaktion anwenden
smart_contract.apply(transaktion2, blockchain)
print(transaktion2.__dict__) # Transaktionsdaten NACH dem apply()

# Transaktionen in den Mempool befördern
transaktionen.append(transaktion1)
transaktionen.append(transaktion2)
# neuen Block erzeugen
blockchain.append(Block(len(blockchain), transaktionen, blockchain[-1].hash, "311e0bb8cf4f5b5202c2a9b7996e483898644aa24714b1e10edd80a54ba4b560"))
# Mempool leeren
transaktionen = []

# Blockchain auflisten
print("Anzahl der Blöcke:", len(blockchain))
print("Alle Blöcke mit jew. Transaktionen:")
for block in blockchain:
    print("Index:", block.index)
    print("Hash:", block.hash)
    print("Prev Hash:", block.previous_hash)
    print()
    print("Transaktionen:")
    for transaction in block.transactions:
        print(transaction.__dict__) # alle Eigenschaften und Werte des Objekts direkt einsehen
        print()
