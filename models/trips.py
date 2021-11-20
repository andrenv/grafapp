from db import db


class DataModel(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(80))
    origin_coord = db.Column(db.String(80))
    destination_coord = db.Column(db.String(80))
    datetime = db.Column(db.DateTime)
    datasource = db.Column(db.String(80))

    def __init__(self, region, origin_coord, destination_coord, datetime, datasource):
        self.region = region
        self.origin_coord = origin_coord
        self.destination_coord = destination_coord
        self.datetime = datetime
        self.datasource = datasource

    def save_to_db(self):
        db.session.add(self)

