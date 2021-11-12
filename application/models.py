from application import db 

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    reviews = db.relationship('Review', backref='books')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'))