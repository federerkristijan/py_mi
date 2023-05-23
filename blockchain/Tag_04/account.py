# Info: Account dient hier als Wallet

# Wallets sind digitale Geldbörsen und haben Zugriff auf die Blockchain,
# um festzustellen wie hoch das jew. Guthaben ist
# Einsatz des privaten Schlüssels (läuft im Hintergrund ab)
# dadurch Authentifizierung mit der Blockchain (quasi der Nachweis als Eigentümer der Wallet)
# und somit eine Referenz auf die Coins in der BC um diese verschicken zu können

# zudem als öffentliche Adresse, um Coins auch jederzeit erhalten zu können

# versch. Wallet-Tpyen:
"""
- Software-Wallets (zB Jaxx, Meta-Mask)
- Hardware-Wallets (zB USB-Sticks)
- Web-Wallets (also über Handelsplattformen wie zB Coinbase, Kraken)
- Paper-Wallets (Schlüssel aufgeschrieben)
- Mobile-Wallets (Smartphone/Tablet per App)
- Brain-Wallet (selbst merken, also NICHT zu empfehlen)
"""

class Account:

    # id: Wallet-Adresse (öffentliche Adresse, bei BTC und ETH eine andere Form als SHA-256, beginnen oft mit 1 oder 3)
    # coins: Guthaben bzw. die Balance
    # Hinweis: Live wäre das NUR eine Referenz auf die Coins, hier in Demo aber fest implementiert
    # als wären die Coins direkt in der Wallet bzw. Geldbörse
    # Referenz schaut also in die komplette BC per Schleife und ermittelt die Balance dank Ein- und Ausgängen von Transaktionen

    def __init__(self, id):

        self.id = id
        self.coins = 0

        # Fazit: real haben wir die Coins NICHT in der Wallet selbst (werden also NICHT bewegt), sondern nur eine Referenz
