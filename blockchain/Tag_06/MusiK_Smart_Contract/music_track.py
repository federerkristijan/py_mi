import datetime

class Track:

    def __init__(self, name, track_id, publish_date):

        self.name = name,
        self.track_id = track_id,
        self.publish_date = publish_date

        publish_date = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%B-%Y-%H-%M")

