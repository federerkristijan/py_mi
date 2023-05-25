# Artist-ID, Track-ID, Published_date,

# extra: number_of_tracks (0 = default), sold (boolean)

class Transaction:

    def __init__(self, artist_id, track_id, publish_date):

        self.artist_id = artist_id,
        self.track_id = track_id,
        self.publish_date = publish_date

        self.number_of_tracks = 0 # Default
        self.sold = False
