import api.src.db as db
import api.src.models as models

class Description:
    __table__ = 'descriptions'
    columns = ['hotel_id', 'description', 'amenities', 'media_uri']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)