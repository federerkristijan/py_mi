# Spielwiese für Cäsar-Verschlüsselung
# https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung


# https://edube.org/learn/pe-2/four-simple-programs-12 (Encryption)
# Nachricht erzeugen
nachricht = "Zoo" # plain bzw. Klartext
schluessel = 1 # Schlüssel für die Verschiebung um n-Stellen
geheime_nachricht = "" # Platzhalter für die geheime Nachricht

for char in nachricht:

    if not char.isalpha(): # KEIN Buchstabe vom Alphabet
        continue

    char = char.upper()
    # https://edube.org/learn/pe-2/characters-and-strings-vs-computers-9
    code = ord(char) + schluessel

    # gibt es einen Überlauf von Z, dann wieder bei A starten, d.h. Z wird zu A
    if code > ord('Z'):
        code = ord('A')

    geheime_nachricht += chr(code)

print("Geheime Nachricht:" ,geheime_nachricht) # QZUIPOJD

nachricht= ""
schluessel2 = -1 # Schlüssel für die Verschiebung um n-Stellen
geheime_nachricht = "APP" # Platzhalter für die geheime Nachricht

for char in geheime_nachricht:

    if not char.isalpha(): # KEIN Buchstabe vom Alphabet
        continue

    char = char.upper()
    # https://edube.org/learn/pe-2/characters-and-strings-vs-computers-9
    code = ord(char) + schluessel2

    if code < ord('A'):
        code = ord('Z')

    nachricht += chr(code)

print("Nachricht:" ,nachricht) # QZUIPOJD

# 5 Minuten Übung: Geheime Nachricht wieder entschlüsseln
# ab 14:41 Besprechung der Lösung

# jetzt mal entschlüsseln
# v. 2
# geheime_nachricht = "QZUIPOJD"
# nachricht = ""

# for char in geheime_nachricht:

#     if not char.isalpha(): # KEIN Buchstabe vom Alphabet
#         continue

#     char = char.upper()
#     # https://edube.org/learn/pe-2/characters-and-strings-vs-computers-9
#     code = ord(char) - schluessel # Zeichencode des neuen Buchstabens nach der Verschiebung

#     if code < ord('A'):
#         code = ord('Z')

#     nachricht += chr(code)

# print("Die Original-Botschaft war:" ,nachricht) # PYTHONIC

# 2 Übungsaufgaben:
# 1) beide Skripte so anpassen dass auch ein Schlüssel größer 1 funktionieren würde
# 2) (26 Groß-Buchstaben im Alphabet berücksichtigt)
# per Brute-Force per Schleife versuchen eine geheime Botschaft zu entschlüssel, allerdings OHNE dass man den Schlüssel kennt
# per Schleife

# 1.
# key = 1
# message = "Wir Kinder vom Bahnhof Zoo"
# secret = ""

# for char in secret:

#     message.slice()

#     if not char.isalpha():
#         continue

#     code = ord(char) +- key

nachricht = "Zoo" # Klartext
schluessel = 3 # Schlüssel für die Verschiebung um 3 Stellen
geheime_nachricht = "" # Platzhalter für die geheime Nachricht

for char in nachricht:
    if not char.isalpha(): # Kein Buchstabe vom Alphabet
        continue

    char = char.upper()
    code = ord(char) + schluessel # Zeichencode des neuen Buchstabens nach der Verschiebung

    if code > ord('Z'):
        code = ord('A') + (code - ord('Z')) - 1

    geheime_nachricht += chr(code)

print("Geheime Nachricht:", geheime_nachricht) # CRR

geheime_nachricht = "CRR" # Geheime Nachricht
schluessel = 3 # Schlüssel für die Rückverschiebung um 3 Stellen
nachricht = "" # Platzhalter für die entschlüsselte Nachricht

for char in geheime_nachricht:
    if not char.isalpha(): # Kein Buchstabe vom Alphabet
        continue

    char = char.upper()
    code = ord(char) - schluessel # Zeichencode des ursprünglichen Buchstabens nach der Rückverschiebung

    if code < ord('A'):
        code = ord('Z') - (ord('A') - code) + 1

    nachricht += chr(code)

print("Entschlüsselte Nachricht:", nachricht) # ZOO
