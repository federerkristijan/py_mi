# Hier kommt alles zusammen
import random
import datetime # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

import daten_variablen

from node import Node
from account import Account
from block import Block
from transaktionen_musik import Transaction
from smart_contract_musik import SmartContract
from user_buyer import User
from music_artist import Artist
from hashlib import sha256


# BC erzeugen
blockchain = []

# Mempool erzeugen
mempool = []

# zugriff auf Smart Contract erlauben
smart_contract = SmartContract()

# Artist1 Tracks erzeugen

tracks1 = Tracks(daten_variablen.artist1["track1_id"],
        daten_variablen.artist1["track1_id"])

# Artist mit Tracks erzeugen
artist1 = Artist(
    daten_variablen.artist1["artist1_name"],
    daten_variablen.artist1["artist1_id"],
    daten_variablen.artist1["artist1_account"],

    )

print("Artist1:", artist1.__dict__)

# Buyer1 erzeugen
buyer1 = User(
    daten_variablen.buyer1["buyer1_id"],
    daten_variablen.buyer1["buyer1_account"],
)

print("Buyer1:", buyer1.__dict__)

publish_date = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%B-%Y-%H-%M")
print("Publish date:", publish_date)


# transaction1 erzeugen
transaction1 = Transaction(artist1, buyer1, publish_date)

print(transaction1.__dict__)
