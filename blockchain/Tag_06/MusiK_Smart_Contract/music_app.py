# Hier kommt alles zusammen
import random
import datetime # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

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

# 1er Artist mit Tracks erzeugen
# Artist1 - 5987a4112188ffba0f3e40e84be978b7b77f3119ee51a956e5ca5515fc53f623
artist_id = "5987a4112188ffba0f3e40e84be978b7b77f3119ee51a956e5ca5515fc53f623"
# Track1 - 51db9efbd89e43e4071e56a0cfac31e63fcfd13bccce04db4f055c7857cb1aee
track_id = "51db9efbd89e43e4071e56a0cfac31e63fcfd13bccce04db4f055c7857cb1aee"
publish_date = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%B-%Y-%H-%M")
print(publish_date)

transaction1 = Transaction(artist_id, track_id, publish_date)
