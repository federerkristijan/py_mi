geheime_nachricht = "QZUIPOJD" # Geheime Nachricht - auch mal CRR für ZOO testen
nachrichten_varianten = [] # Liste für alle Varianten der entschlüsselten Nachrichten

for schluessel in range(26): # Durchlaufen aller 26 Schlüsselwerte
    nachricht = ""

    for char in geheime_nachricht:
        if not char.isalpha(): # Kein Buchstabe vom Alphabet
            continue

        char = char.upper()
        code = ord(char) - schluessel # Zeichencode des ursprünglichen Buchstabens nach der Rückverschiebung

        if code < ord('A'):
            code = ord('Z') - (ord('A') - code) + 1

        nachricht += chr(code)

    nachrichten_varianten.append(nachricht)

print("Alle Varianten der entschlüsselten Nachrichten:")
i = 0
for variante in nachrichten_varianten:
    print("Schlüssel:", i)
    print("Wert:", variante)
    print()
    i += 1

"""
AUSGABE:

Schlüssel: 0
Wert: QZUIPOJD

Schlüssel: 1
Wert: PYTHONIC

Schlüssel: 2
Wert: OXSGNMHB

Schlüssel: 3
Wert: NWRFMLGA

Schlüssel: 4
Wert: MVQELKFZ

Schlüssel: 5
Wert: LUPDKJEY

Schlüssel: 6
Wert: KTOCJIDX

Schlüssel: 7
Wert: JSNBIHCW

Schlüssel: 8
Wert: IRMAHGBV

Schlüssel: 9
Wert: HQLZGFAU

Schlüssel: 10
Wert: GPKYFEZT

Schlüssel: 11
Wert: FOJXEDYS

Schlüssel: 12
Wert: ENIWDCXR

Schlüssel: 13
Wert: DMHVCBWQ

Schlüssel: 14
Wert: CLGUBAVP

Schlüssel: 15
Wert: BKFTAZUO

Schlüssel: 16
Wert: AJESZYTN

Schlüssel: 17
Wert: ZIDRYXSM

Schlüssel: 18
Wert: YHCQXWRL

Schlüssel: 19
Wert: XGBPWVQK

Schlüssel: 20
Wert: WFAOVUPJ

Schlüssel: 21
Wert: VEZNUTOI

Schlüssel: 22
Wert: UDYMTSNH

Schlüssel: 23
Wert: TCXLSRMG

Schlüssel: 24
Wert: SBWKRQLF

Schlüssel: 25
Wert: RAVJQPKE
"""
