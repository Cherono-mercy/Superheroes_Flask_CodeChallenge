#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify

from flask_restful import Resource, Api
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to my superheroes API'

class Heroes(Resource):
    def get(self):
        heroes =[]
        for hero in Hero.query.all():
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
            heroes.append(hero_dict)
        return make_response(jsonify(heroes), 200)  

api.add_resource(Heroes, '/heroes')    


if __name__ == '__main__':
    app.run(port=4000)
