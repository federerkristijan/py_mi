from flask import Flask, render_template, request

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
        # transaktion1 = Transaktion(sender, receiver, amount)

        # aktuelle Transaktion aus dem Formular in den Mempool übertragen
        transaktionen.append("{0} schickt {1} {2} Coins").format(sender, receiver, amount) # vorerst NURS als String-Information

        # print("POST Daten sind nicht da") # Ausgabe an den Client bzw. Browser
        # alle offenene Transaktion anzeigen
        return transaktionen

    else:
        return render_template("index.html")


@app.route("/mine", methods=["GET", "POST"])
def mine():
    pass

@app.route("/blockchain", methods=["GET", "POST"])
def blockchain():
    pass

app.run(debug=True)

# Übung am Nachmittag:
# Routes /mine und /blockchain definieren
# bei /mine die Liste blockchain[] mit Trasaktionen füllen (Liste aus Strings oder Transaktion-Objekte)
# bei /blockchain die Blockchain auslesen (per Konsole oder HTML)
# Gemeinsame Besprechung dann am Dienstag Vormittag (Montag Feiertag)
