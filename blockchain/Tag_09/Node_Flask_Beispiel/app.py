from flask import Flask

import random

app = Flask(__name__)

# Zufallszahl erzeugen für jede einzelne "Node"
# Wenn ein Server startet (oder eine Node) -> wird eine jeweilige Randomzahl erzeugt

zufallszahl = random.randint(0,100)
print("Randomzahl: ", zufallszahl)

@app.route("/")
def home():
    return f"<p>Zufallszahl: {zufallszahl}</p>"
