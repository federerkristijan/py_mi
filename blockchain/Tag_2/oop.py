# Vererbung -> classe sind IMMER Singluar and CamelCase!

class Person(): # Elternklasse/Super-Klasse
    def __init__(self, name, alter):

        self.name = name
        self.alter = alter

    def feier_geburtstag(self):

        self.alter += 1
        print("Happy Bday! Du bist jetzt: ", self.alter)

# Ziel:
""" Klasse User (erbt von Klasse Person)
name
alter
username
ist_online
feier_geburtstag()
check_online_status()
"""

class User(Person): # User erbt alle Information von Person
    def __init__(self, name, alter, username, ist_online):

        # self.name = name
        # self.alter = alter

        # Kurzform: den Konstruktor der Superklasse Person nutzen
        super().__init__(name, alter)
        self.username = username
        self.ist_online = ist_online

    def check_online_status(self):

        if self.ist_online:
            print("User ist online")
        else:
            print("User ist offline")

# Person erzeugen
person1 = Person("Laura", 33)
print(person1.name)
person1.feier_geburtstag()

# User erzogen
user1 = User("Ingo", 44, "ingo44", True)
user2 = User("Petra", 55, "petra55", False)

# Liste mit 2 Usern
users = [
    user1,
    user2,
    User("Bob", 66, "bob66", True)
]

# alle Username auflisten
for user in users:
    print("User: ", user.name, "Username: ", user.username)

# Vesuch, ob ein Person-Objekt Online_Status checken kann
# person1.check_online_status() - Attribute Error: 'Person' object has not attribute "Check_online_status"
# funktionier dank Vererbung
user1.feier_geburtstag()
user1.check_online_status()

"""
# Aufgabe (Gruppenarbeit in 2-3er-Gruppen):
1.
- gemeinsam eine Mutter- bzw. Superklasse erzeugen (bei uns war das Person)
- Idee: zB Tiere, Fahrzeuge, Fußball etc.
- diese Klasse gemeinsam mit Eigeschaften UND mind. 1 Methode ausstatten plus Konstruktor
2.
- selbständig im Anschluss jeder Teilnehmer eine eigene Unterklasse definieren (bei uns war das User)
- Unterklasse mit Eigenschaften UND mind. 1 Methode ausstatten
- 1-2 Objekt der Unterklasse erzeugen und Methoden darauf anwedden, ggfs. auch in eine Liste stecken und darüber iterieren
Dauer: ingesamt Zeit bis 13 Uhr - gemeinsame Besprechung ab 14:05
"""

class Tier:
    def __init__(self, size, age, name):
        self.size = size
        self.size = age
        self.name = name

    def athme(self):
        print(self.name + "athmet ein, ...athmet aus.")

class Hund(Tier):
    def __init__(self, size, age, name, race):
        super().__init__(size, age, name)
        self.race = race

    def bellt(self):
        print(self.name + " bellt")


class Pferd(Tier):
    def __init__(self, size, age, name, speed):
        super().__init__(size, age, name)
        self.speed = speed

    def is_faster_than(self, horse2=None):
        if horse2= None:
            print("2. Pferd fehlt")
            raise ValueError
        elif isinstance(horse2,Pferd):
            self.speed > horse2.speed
        else:
            print("2. Pferd ist gar kein Pferd.")
            raise ValueError

tier1 = Tier(122, 20, "Ulf")
tier2 = Tier(30, 150, "Gundula")
tier1.athme()
tier2.athme()

hund1 = Hund(160, 4, "Johhny", "Labrador")

hund1.bellt()

horse1=Pferd(200,3,"Gustav",80)
horse2=Pferd(190,4,"Sven",70)


print(horse2.speed)
print(horse1.is_faster_than())

list = [
    horse1,
    horse2,
    hund1,
    tier1,
    Hund(130, 5, "Rex", "Schäferhund")
]
