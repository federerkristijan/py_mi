from flask import Flask, render_template, request
from block import Block
from transaction import Transaction

from hashlib import sha256

app = Flask(__name__)

# Blockchain erstellen
blockchain = []

# Mempool
transaktionen = []

# @app.route("/")
# def home():
#     user = "Peter321"
#     return render_template("index.html", username=user)

# Routing
@app.route("/transaktion", methods=["GET", "POST"]) # wichtig: hier Methoden erwähnen
def transaktion():

    # Check, ob POST-Daten vorliegen
    if request.method == "POST":

        print("POST Daten sind da") # Ausgabe in der Konsole

        # Daten verarbeiten
        # Sender von Anfrag an Server abgreifen
        sender = request.form["sender"] # index.html name="sender"

        receiver = request.form["receiver"]

        amount = request.form["amount"]

        # Testausgabe in der Konsole
        print(sender, receiver, amount)

        # irgendwann mals das Ziel:
        transaktion1 = Transaction(sender, receiver, amount)

        # aktuelle Transaktion aus dem Formular in den Mempool übertragen
        transaktionen.append(transaktion1)

        # print("POST Daten sind nicht da") # Ausgabe an den Client bzw. Browser
        # alle offenene Transaktion anzeigen
        return transaktion1.__dict__

    else:
        return render_template("index.html")

# 1) Route /mine zum Minen eines Blocks (wichtig: Mempool leeren)
@app.route("/mine")
def mine(): # wichtig: hier Methoden erwähnen
    global blockchain
    global transaktionen

    print("Mine")
    print("Mempool:", transaktionen)

    # ggfs. Previous Hash für Genesis-Block zuweisen
    if len(blockchain) == 0:
        previous_hash = "0000000000"
    else:
        previous_hash = blockchain[-1].hash

    # Hash vereinfacht ohne PoW mit laufender Nummer per Anzahl der Elemente als EIngabe für sha256
    hash = sha256(str(len(blockchain)).encode("utf-8")).hexdigest() # zB Hash für 0,1,2,3,...

    blockchain.append(Block(len(blockchain), transaktionen, previous_hash, hash))

    # Mempool leeren
    transaktionen = []

@app.route("/blockchain", methods=["GET", "POST"])
def blockchain():
    pass

app.run(debug=True)

# Übung am Nachmittag:
# Routes /mine und /blockchain definieren
# bei /mine die Liste blockchain[] mit Trasaktionen füllen (Liste aus Strings oder Transaktion-Objekte)
# bei /blockchain die Blockchain auslesen (per Konsole oder HTML)
# Gemeinsame Besprechung dann am Dienstag Vormittag (Montag Feiertag)
