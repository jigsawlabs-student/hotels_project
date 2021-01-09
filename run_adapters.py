import psycopg2
import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters



class RequestAndBuild:
    def __init__(self):
        self.client = adapters.HotelClient()
        self.builder = adapters.Builder()
        self.conn = psycopg2.connect(database='hotels_development')
        self.cursor = self.conn.cursor()
        self.hotel_list = 'TILONRHO' #BGMILBGB,
       
    def run(self):
        hotel_details = self.client.request_offers(self.hotel_list) # PUT IN MULTIPLE HOTELS VIA self.hotel_list >>
        for hotel_detail in hotel_details:
            hotel_obj = self.builder.run(hotel_detail, self.conn, self.cursor)
            return hotel_obj
        
        # for hotel in hotel_list:
        # location = adapters.LocationBuilder().run(hotel_details[hotel], self.conn, self.cursor) 
        # hotel = adapters.HotelBuilder().run(hotel_details[hotel], location, self.conn, self.cursor)
        # offer = adapters.OfferBuilder().run(hotel_details[hotel], hotel, self.conn, self.cursor)

        # hotel_amadeus_ids = [hotel['amadeus_id'] for hotel in hotels]
        # hotel_objs = []
        # for amadeus_id in hotel_amadeus_ids:
        #     hotel_details = self.client.request_offers(amadeus_id)
        #     hotel_obj = self.hotelbuilder.run(hotel_details, self.conn, self.cursor)
        #     hotel_objs.append(hotel_obj)
        # return hotel_objs

obj = RequestAndBuild()
obj.run()