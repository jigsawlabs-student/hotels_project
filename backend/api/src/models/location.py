import api.src.db as db
import api.src.models as models
class Location:
    __table__ = 'locations'
    columns = ['id', 'lon', 'lat', 'address', 'city_name', 'postal_code', 'country_code']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)