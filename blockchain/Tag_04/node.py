# Node bzw. Knoten ist ein Computer bzw. ein Netzwerk von Computern in einem Peer-to-Peer-Netzwerk

# https://www.btc-echo.de/academy/bibliothek/node/

# https://river.com/learn/what-is-a-bitcoin-node/

class Node: # hier in unserer Demo ist eine Node auch gleichzeitig ein Miner

    # zur Info: bei Minern ist die Hasrate auch wichtig, im Gegensatz zu üblichen Nodes
    # um wahrscheinlich (aber keine Garantie) den PoW als erstes zu meistern je höher die eigene Rechenleistung bzw. Hashrate
    # Hashrate sagt aus: wieviele Hash können in 1 Sekunde errechnet werden

    # address: IP-Adresse einer Node
    # account: Wallet einer Node

    def __init__(self, address, account):

        self.address = address
        self.account = account # v.a. wichtig für den Reward
