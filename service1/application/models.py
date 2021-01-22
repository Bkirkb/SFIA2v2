from application import db

class Fortune2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    yearmon = db.Column(db.String(40), nullable=False)
    fortune = db.Column(db.String(200), nullable=True)
    luck = db.Column(db.String(10), nullable=True)
    

