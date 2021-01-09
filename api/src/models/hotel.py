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

    @classmethod
    def find_by_amadeus_id(self, amadeus_id, cursor):
        hotels_query = """SELECT * FROM hotels WHERE amadeus_id = %s"""
        cursor.execute(hotels_query, (amadeus_id, ))
        record = cursor.fetchone()
        return db.build_from_record(models.Hotel, record)


    # find by location
    # find by brand
    # find cheapest price
    # find greatest sale relative to average price
    