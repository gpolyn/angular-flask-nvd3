from db import db


class Post(db.Document):
	text = db.StringField()
