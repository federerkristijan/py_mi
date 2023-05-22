# Spielwiese für Hashfunktionen + Proof-of-work

#https://www.blocktrainer.de/blocktrainer-1x1/was-ist-ein-hash/
#https://de.wikipedia.org/wiki/Kryptographische_Hashfunktion
#https://de.wikipedia.org/wiki/SHA-2

# Mensch: Fingerabdruck (zur Identifizierung)
# digitale Welt: digitaler Fingerabdruck (Hashfunktion)
# (zu einer bestimmten Eingabe einen eindeutigen Hashwert)

# folgende Eigenschaften:

#Ein Hash sollte deterministisch sein – Eine Nachricht sollte immer den gleichen Hashwert ergeben.
#Ein Hash sollte effizient sein – Die Eingabe kann über die Hash-Funktion schnell zu einer Ausgabe verarbeitet werden.
#Ein Hash sollte einseitig sein – Die Ursprungsnachricht darf aus dem Hashwert nicht ableitbar sein.
#Ein Hash sollte kollisionssicher sein – Zwei verschiedene Nachrichten dürfen nicht den gleichen Hashwert ergeben.
#Kleine Änderungen der Nachricht sollten zu großen Veränderungen des entsprechenden Hashwertes führen.

# Hashfunktion: kleine Computerprogramme
# Ziel: unabhängig von Größe oder Länge der Eingabe (zB Text, Video, Bild, Ton)
# erhalten wir eine feste Länge zurück (idealerweise für Sortierung oder Vergleich)

# https://hashgenerator.de/
# Hallo Welt: 2d2da19605a34e037dbe82173f98a992a530a5fdd53dad882f570d4ba204ef30
# Hallo welt: a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57

# Modul hashlib importieren und Funktion sha256 einlesen
from hashlib import sha256

# Testfall: Ziel per String "Hallo Welt" den Hash: 2d2da19605a34e037dbe82173f98a992a530a5fdd53dad882f570d4ba204ef30
computed_hash = sha256("Hallo Welt".encode("utf-8")).hexdigest() # Umwandlung in ein lesbares Format: 64 Zeichen
print(computed_hash) # 2d2da19605a34e037dbe82173f98a992a530a5fdd53dad882f570d4ba204ef30

# aktueller valider Hash beim BTC:
# 00000000000000000003bec6c4a0958b8b6020570620422ccb9dc6a4443256ea
# Stand vom 22. Mai 2023 aktuell 19 führende Nullen (je nach Ausladtung des Netzwerks alle 2 Wochen angepasst)

#
# Proof-of-work (Arbeitsnachweis bzw. intensive Rechenleistung um beim Mining einen gültigen Hash zu finden)
#

# Difficulty festlegen
difficulty = 4
# Nonce
nonce = 0 # quasi eine unbekannte Variable, die iLdZ um 1 erhöht wird um ggfs. einen validen Hash zu erzeugen

print(difficulty * "0") # 00
print("0012345".startswith("00")) # True, also ein valider Hash weil 2 führende Nullen

while not computed_hash.startswith("0" * difficulty): # unsere Bedingung noch nicht erreicht

    # Nonce um 1 erhöhen
    nonce += 1
    # neuen Hash generieren in Abhängigkeit der neuen Nonce
    string_to_hash = "Hallo Welt" + str(nonce)
    computed_hash = sha256(string_to_hash.encode("utf-8")).hexdigest()
    # aktuellen Hash ausgeben
    # print("Aktueller Hash:", computed_hash)

print("Nonce:", nonce)
print("Gültiger Hash:", computed_hash)
