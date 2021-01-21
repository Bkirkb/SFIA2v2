from application import db

class Fortune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(40), nullable=False)
    fortune = db.Column(db.String(200), nullable=True)
    
