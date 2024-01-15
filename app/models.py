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
    
# Creating powers table    

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Define the relationship to HeroPower
    hero_power = db.relationship('HeroPower', backref='power', lazy=True)
    
    serialize_rules = ('-hero_power.power',)
    
    @validates('description')
    def validate_description(self, key, body):
        if len(body) < 20:
            raise ValueError('description must be at least 20 characters')
        return body
    
    def __repr__(self):
        return f'<Power {self.id}: {self.name}; {self.description}>'
