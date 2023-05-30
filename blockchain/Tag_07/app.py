from flask import Flask, render_template, request
from block import Block
from transaction import Transaction

from hashlib import sha256

app = Flask(__name__)

# Blockchain erstellen
blockchain = []

# Mempool
transaktionen = []

'''
1. https://gist.github.com/colonialars/49c2eb6eef97a4d0b29bd986f30f0b89
2. https://gist.github.com/colonialars/4300316909e2a2cba3e76de7d70e63ec
3. https://gist.github.com/colonialars/298172b7004acd9c6e726716ba496465
4. https://gist.github.com/colonialars/a9a4fe50f6c4dedd14346847fa9a76ae
'''

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

    # Hash vereinfacht ohne PoW mit laufender Nummer per Anzahl der Elemente als Eingabe für sha256
    hash = sha256(str(len(blockchain)).encode("utf-8")).hexdigest() # zB Hash für 0,1,2,3,...

    blockchain.append(Block(len(blockchain), transaktionen, previous_hash, hash))

    # Mempool leeren
    transaktionen = []

    return "Block mit Index {} wurde gemined.".format(len(blockchain) - 1)

# 2) Route/blockchain definieren zum Auflisten der gesamten BC
    '''
    render_template() übergibt die BC an das HTML-Template und dort wird dank Jinj2 der Platzhalter durch eine Schleife ersetzt
    '''
@app.route("/blockchain", methods=["GET", "POST"])
# Aufpassen auf den Nameskonlifkten
def show_blockchain():

    return render_template("blockchain.html", blockchain = blockchain)

app.run(debug=True)
