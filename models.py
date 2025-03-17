from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    reposts = db.Column(db.Integer, default=0)
    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)  # Ответ на пост
