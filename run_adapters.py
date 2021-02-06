import psycopg2
import pandas
from datetime import date, timedelta
import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters

# Create string of hotel ID's to call from API:
def hotel_ids_str():
    with open ('hotel_list_prod.csv') as csvfile:
        df = pandas.read_csv(csvfile, header=0)
        ids = df.id.to_string(index=False, header=False).split('\n')
        ids_str = ",".join(ids).replace(" ","")
        return ids_str   

class RequestAndBuild:
    def __init__(self):
        self.client = adapters.HotelClient()
        self.builder = adapters.Builder()
        self.conn = psycopg2.connect(database='hotels_development')
        self.cursor = self.conn.cursor()
        self.hotel_list = hotel_ids_str()
       
    def run(self, days_out):
        print(self.hotel_list)
        
        hotel_objs = []
        for i in range(days_out):
            check_in = date.today() + timedelta(days=23) + timedelta(days=i)
            check_out = check_in + timedelta(days=1)
            print(f"{self.hotel_list}", check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
            hotel_details = self.client.request_offers(f"{self.hotel_list}", check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d")) # NEEDS ERROR HANDLING IF A HOTEL COMES BACK 400 - LOGGING?            
            for hotel_detail in hotel_details:
                print(hotel_detail['hotel']['name'])
                hotel_obj = self.builder.run(hotel_detail, self.conn, self.cursor)
                hotel_objs.append(hotel_obj)
        return hotel_objs
        
obj = RequestAndBuild()
obj.run(90)