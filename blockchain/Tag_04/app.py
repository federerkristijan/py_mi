# Spielwiese für Mining per Nodes (Simulation) und User und Wallets

# Module
from node import Node
from account import Account
from user import User
from block import Block
from transaction import Transaction

import random # für die Simulation einer zufälligen Node bzw. Miner die den PoW gewonnen hätte

# 3 Nodes erzeugen für unser P2P-Netzwerk
# HIntergrund. BTC-Adress per Python generieren zB: https://medium.com/coinmonks/bitcoin-address-generation-on-python-e267df5ff3a3
nodes = [
    Node("127.0.0.1:8000", Account("fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62")), # statisch als SHA-256 für den Wert "Node1"
    Node("127.0.0.1:8001", Account("1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc")),
    Node("127.0.0.1:8002", Account("7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4"))
]

# Nodes auflisten
print("Nodes")
for node in nodes:
    print("Wallet-Addresse:", node.account.id)
    print("Coins:", node.account.coins)
    print()

# 2 User anlegen (Petra, Bob)
users = [
    User("Petra", Account("d2bfbb716eec9e29eda06f8a0f6b2b2a522f1eaab71f2228f33aad493ce2eebd"), "12345"), # Wallet-Adresse: Hash von "Petra"
    User("Bob", Account("cd9fb1e148ccd8442e5aa74904cc73bf6fb54d1d54d333bd596aa9bb4bb4e961"), "54321")
]

# Users auflisten
print("Users:")
for user in users:
    print("Name:", user.name)
    print("Wallet-Adresse:", user.account.id)
    print("Coins:", user.account.coins)
    print()

# Blockchain erzeugen
blockchain = []
# Hinweis: hier in Demo ohne PoW daher auch keine Difficulty festgelegt

# Blöcke erzeugen bzw. Transaktionen hinzufügen + Reward an den jew. Miner
# Ziel: eine zufällige Node gewinnt das Rennen bzw. die Lotterie und erzeugt einen validen Hash bzw. neuen Block
# hier den Genesis-Block (dabei einen Reward iHv 100 Coins in unserer Simulation hier)
# index, transactions, previous_hash, hash

# vorab eine zufällige Node ermitteln für den Reward
random_node = random.choice(nodes)
blockchain.append(Block(0, [], "0000000000", "3fa8a90ec59766fb5abd788313751a858455ce3b9fd70e3955557be28075356c")) # Hash aus "Block0"
# hier werden neue Coins geschürft
print("Reward für:", random_node.address)
# TODO: Reward auszahlen an die jew. Node
