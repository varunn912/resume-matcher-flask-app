from app import db
from flask_login import UserMixin
from app.utils import get_ist_time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    matches = db.relationship('MatchHistory', backref='author', lazy=True, cascade="all, delete-orphan")

class MatchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_description = db.Column(db.Text, nullable=False)
    resume_text = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=get_ist_time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)