from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return "<User(id='%s', username='%s)>" % (self.id, self.username)