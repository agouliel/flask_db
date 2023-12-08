from app_pkg import db

class Monitor(db.Model):
    __tablename__ = 'Monitor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host = db.Column(db.String(100))
    mon_date = db.Column(db.DateTime)
    mon_value = db.Column(db.Float)