from datetime import datetime
from . import db


class Ads(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    update_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


