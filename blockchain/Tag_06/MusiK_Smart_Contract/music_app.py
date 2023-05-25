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

# Artist mit Tracks erzeugen
# Artist1 - 5987a4112188ffba0f3e40e84be978b7b77f3119ee51a956e5ca5515fc53f623
# artist1_id = "5987a4112188ffba0f3e40e84be978b7b77f3119ee51a956e5ca5515fc53f623"
# # Track1 - 51db9efbd89e43e4071e56a0cfac31e63fcfd13bccce04db4f055c7857cb1aee
# track1_id = "edda259099c2f436903f05aad086f17d3490db1907a79c3f49823c277e45482d"
# track2_id = "67defc781e5429152f6433d52cd3969cec65d98dc73a07425b4c9321bd6a48d0"

# artist1_account = "a581d299155d4a63d27a222087ec4459bc4633397eb96e418b080ef249fc2734"

# artist1 = Artist(artist1_id, artist1_account, [track1_id, track2_id])
artist1 = Artist(
    daten_variablen.artist1["artist1_id"],
    daten_variablen.artist1["artist1_account"],
    [
        daten_variablen.artist1["track1_id"],
        daten_variablen.artist1["track1_id"]
    ]
    )

print(artist1)

publish_date = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%B-%Y-%H-%M")
print(publish_date)

# Buyer1 erzeugen
# buyer1 = User()

# transaction1 erzeugen
# transaction1 = Transaction(Artist, publish_date)
