# Artist-ID, Track-ID, Published_date,

# extra: number_of_tracks (0 = default), sold (boolean)

class Transaction:

    def __init__(self, artist, buyer, amount):


        self.artist = artist
        self.buyer = buyer
        self.amount = amount

        self.sold = False

        #self.hash = sha256
