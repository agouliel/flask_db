from app_pkg import db

class Tblsongs(db.Model):
    __tablename__ = 'tblsong'
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text())
    artist = db.Column(db.Text())
    composer = db.Column(db.Text())
    album = db.Column(db.Text())
    comment = db.Column(db.Text())

    def to_dict(self):
        return {
            'sid': self.sid,
            'title': self.title,
            'artist': self.artist,
            'composer': self.composer,
            'album': self.album,
            'comment': self.comment,
        }
