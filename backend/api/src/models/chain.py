import api.src.db as db
import api.src.models as models

class Chain:
    __table__ = 'chains'
    columns = ['id', 'chain_code', 'name']

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

    