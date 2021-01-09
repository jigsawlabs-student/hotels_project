import api.src.db as db
import api.src.models as models

class Offer:
    __table__ = 'offers'
    columns = ['id', 'offer_id', 'hotel_id', 'check_in', 'check_out', 'available', 'currency', 'total_rate', 'comm_percentage']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)