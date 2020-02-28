import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dburi = os.getenv('QUOTES_DB_URI')
if not dburi:
    raise Exception('QUOTES_DB_URI environment variable not set')

app = Flask('fakeapp')
app.config['SQLALCHEMY_DATABASE_URI'] = dburi
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.Text)
    author = db.Column(db.String(60))

    def __repr__(self):
        return '<User %r - %r>' % (self.author, self.quote)


@app.route('/')
def hello_world():
    return {'message': 'Hello, World!'}


@app.route('/quote')
def quote():
    quotes = Quote.query.all()
    res = []
    for q in quotes:
        res.append({
            'author': q.author,
            'quote': q.quote
        })
    return {'quotes': res}


@app.cli.command("initdb")
def initdb():
    db.create_all()
