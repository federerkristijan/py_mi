class Artist():

    def __init__(self, name, id, account):

       self.name = name,
       self.id = id,
       self.account = account,

class Tracks(Artist):

    def __init__(self, name, id, account, tracks, track_id, publish_date):

        super().__init__(name, id, account, tracks,)
        self.track_id = track_id,
        self.publish_date = publish_date

        self.number_of_tracks = 0 # Default
