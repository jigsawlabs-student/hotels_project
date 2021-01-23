from flask import Flask
from flask import request
import simplejson as json

import api.src.db as db 
import api.src.models as models 

def create_app(database='hotels_development', testing = False, debug = True):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=database,
        DEBUG = debug,
        TESTING = testing
    )

    @app.route('/')
    def root_url():
        return 'Welcome to the hotels API'

    
    @app.route('/hotels')
    def hotels():
        conn = db.get_db()
        cursor = conn.cursor()

        hotels = db.find_all(models.Hotel, cursor)
        hotels_dicts = [hotel.__dict__ for hotel in hotels]
        return json.dumps(hotels_dicts, default = str)

    @app.route('/offers')
    def offers():
        conn = db.get_db()
        cursor = conn.cursor()

        offers = db.find_all(models.Offer, cursor)
        offers_dicts = [offer.__dict__ for offer in offers]
        return json.dumps(offers_dicts, default = str)

    @app.route('/hotels/<id>')
    def search_offers(id):
        conn = db.get_db()
        cursor = conn.cursor()
        hotel = db.find(models.Hotel, id, cursor)        
        return json.dumps(hotel.to_json(cursor), default = str)

    @app.route('/hotels/<id>/cheapest')
    def search_offers_cheapest(id):
        conn = db.get_db()
        cursor = conn.cursor()
        hotel = db.find(models.Hotel, id, cursor)
        return json.dumps(hotel.to_json_cheapest(cursor), default = str)


    return app



    # @app.route('/locations')
    # def locations():
    #     conn = db.get_db()
    #     cursor = conn.cursor()

    #     locations = db.find_all(models.Location, cursor)
    #     locations_dicts = [location.__dict__ for location in locations]
    #     return json.dumps(locations_dicts, default = str)