from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube.db'

db = SQLAlchemy(app)


class Records(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    number_of_likes = db.Column(db.Integer)
    number_of_reply = db.Column(db.Integer)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, author, like, reply, text):
        self.aname = author
        self.number_of_likes = like
        self.number_of_reply = reply
        self.comment = text


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    # pass
