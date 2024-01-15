from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

# Creating a heroes table

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Define the relationship to HeroPower
    hero_power = db.relationship('HeroPower', backref='hero', lazy=True)
    
    serialize_rules = ('-hero_power.hero',)
    
    def __repr__(self):
        return f'<Hero {self.id}: {self.super_name}>'

# add any models you may need. 