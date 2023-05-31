# Genereierung der Bitcoin-Adresse
# 1. Private Schlüssel
# - zufällig generierte 256-Bit-Zahl
# 2. Öffentlicher Schlüssel
# - wird aus dem privaten Schlüssel mithilfe mathematischer Berechnung (ECC) abgeleitet
# 3. Adresse
# - wird aus dem öffentlichen Schlüssel abgeleitet

import hashlib
import ecdsa
import base58

