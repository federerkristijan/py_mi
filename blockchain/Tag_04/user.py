# Ziel: neben den Nodes (bzw. Miner) auch User, die sich gegenseitig Coins schicken können
# Voraussetzung: User müssen ggfs. im Vorfeld ihre Fiat-Währung gegen Coins eintauschen (zB per Handelsplattform)


class User:

    # name: (nur für unsere Demo, weil User real ja anonym bleiben sollen)
    # account: Wallet-Adresse
    # private_key: der private Schlüssel für Zugriff auf die Wallet

    def __init__(self, name, account, private_key):

        self.name = name
        self.account = account
        
        self.private_key = private_key
