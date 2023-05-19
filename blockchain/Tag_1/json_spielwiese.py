# Spielwiese zum Thema JSON

# https://de.wikipedia.org/wiki/JavaScript_Object_Notation#Beispiel_2

json_string_wikipedia = """
{
  "Herausgeber": "Xema",
  "Nummer": "1234-5678-9012-3456",
  "Deckung": 2e+6,
  "Waehrung": "EURO",
  "Inhaber":
  {
    "Name": "Mustermann",
    "Vorname": "Max",
    "maennlich": true,
    "Hobbys": ["Reiten", "Golfen", "Lesen"],
    "Alter": 42,
    "Kinder": [],
    "Partner": null
  }
}
"""

ort = "Berlin"
print(ort[0:5]) # Berli

print(json_string_wikipedia)
# Ziel: Herausgeber auslesen - hier: Xema
#print(json_string_wikipedia["Herausgeber"]) # TypeError: string indices must be integers, not 'str'
print(json_string_wikipedia[21:25]) # Xema
# Fazit: zu umständlich
print(type(json_string_wikipedia)) # <class 'str'>

# validen JSON-String in ein dict umwandeln bzw. konvertieren per Modul namens "json"
import json
# per json.loads() nun auf die Werte zugreifen dank "Schlüssel", weil jetzt ein dict vorliegt
json_dict_wikipedia = json.loads(json_string_wikipedia)
# Datentyp ermitteln von json_dict_wikipedia
print(type(json_dict_wikipedia)) # <class 'dict'>
print(json_dict_wikipedia)
# Ziel: Herausgeber auslesen
print(json_dict_wikipedia["Herausgeber"]) # Xema

# Max auslesen
print(json_dict_wikipedia["Inhaber"]["Vorname"])
# alternativ mit Zwischenschritten
inhaber = json_dict_wikipedia["Inhaber"]
vorname = inhaber["Vorname"]
print(vorname)

# das letzte Hobby vom Max auslesen
print("Letztes Hobby von Max:", json_dict_wikipedia["Inhaber"]["Hobbys"][-1]) # Lesen

# per API Kontakt aufnehmen zu einem Server und JSON abholen und weiterverarbeiten
# Modul installieren: "requests", um Anfragen (Requests) als Client (zB Browser) an Server zu schicken
# und Antwort (Response) zu erhalten
import requests

# Ziel: Anfrage an https://randomuser.me/api/ liefert uns eine Antwort in JSON mit einem zufälligen User
# per HTTP-GET-Methode
response = requests.get("https://randomuser.me/api/")
# Fazit: in "response" steckt nun die Antwort vom Server
print(response) # <Response [200]>
print(response.status_code) # 200: alles ok, 404: not found Error
print(response.text) # Content, also unser JSON-String
print(type(response.text)) # <class 'str'>
# JSON-String in ein dict konvertieren
json_string = response.text
dict_random_user = json.loads(json_string)
print(type(dict_random_user)) # <class 'dict'>

# 1) Land ausgeben
print(dict_random_user["results"][0]["location"]["country"])

# 2) Username ausgeben
print(dict_random_user["results"][0]["login"]["username"])

# 3) Straße UND Hausnummer ausgeben
street_name = dict_random_user["results"][0]["location"]["street"]["name"]
street_number = dict_random_user["results"][0]["location"]["street"]["number"]
print(street_name, street_number)

# 4) URL-Adresse von Thumbnail-Grafik
print(dict_random_user["results"][0]["picture"]["thumbnail"])

# Gemeinsame Besprechung ab 14:50 - viel Erfolg!


# Übungsnachmittag ab 15:15 (vorher Kaffeepause):
# - Website Handelsblatt (optional)
# - Recherche eigene API (zB Bitcoin-Kurs auslesen und weiterverarbeiten)
# (idealerweise eine API ohne sich registrieren zu müssen)

# bei Rückfragen bin ich in Raum 1, Freitag Thema OOP und Vererbung, Donnerstag Feiertag

# alternative Kurzform für Request und gleichzeitiger Konvertierung von JSON in dict
response = requests.get("https://randomuser.me/api/").json()
print(response["results"][0]["name"]["first"])

# Sue:
print(json.dumps(dict_random_user, indent=4))

btc_response = requests.get("https://blockchain.info/ticker")
btc_dict = json.loads(btc_response.text)
print("1 BTC in EUR:", btc_dict["EUR"]["last"], btc_dict["EUR"]["symbol"])
print("1 BTC in GBP:", btc_dict["GBP"]["last"], btc_dict["GBP"]["symbol"])
print("1 BTC in USD:", btc_dict["USD"]["last"], btc_dict["USD"]["symbol"])
