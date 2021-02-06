import api.src.db as db
import api.src.models as models

class Hotel:
    __table__ = 'hotels'
    columns = ['id', 'amadeus_id', 'name', 'location_id', 'chain_id', 'rating']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def location(self, cursor):
        location_query = """SELECT * FROM locations WHERE locations.id = %s"""
        cursor.execute(location_query, (self.location_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Location, record)

    def offers(self, cursor):
        offers_query = """SELECT * FROM offers WHERE offers.hotel_id = %s"""
        cursor.execute(offers_query, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Offer, records)

    def cheapest(self, cursor):
        offers_query = """SELECT * FROM offers WHERE offers.hotel_id = %s ORDER BY total_rate ASC"""
        cursor.execute(offers_query, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Offer, records)

    def to_json(self, cursor):
        offers = self.offers(cursor)
        location = self.location(cursor)
        hotel_dict = self.__dict__
        location_dict = location.__dict__
        offers_dicts = [offer.__dict__ for offer in offers]
        # location_dicts = [location.__dict__ for location in locations]
        hotel_dict['location'] = location_dict
        hotel_dict['offers'] = offers_dicts
        return hotel_dict
    
    def to_json_cheapest(self, cursor):
        offers = self.cheapest(cursor)
        hotel_dict = self.__dict__
        offers_dicts = [offer.__dict__ for offer in offers]
        hotel_dict['offers'] = offers_dicts
        return hotel_dict

    @classmethod
    def find_by_amadeus_id(self, amadeus_id, cursor):
        hotels_query = """SELECT * FROM hotels WHERE amadeus_id = %s"""
        cursor.execute(hotels_query, (amadeus_id, ))
        record = cursor.fetchone()
        return db.build_from_record(models.Hotel, record)