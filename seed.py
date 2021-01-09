import psycopg2
from api.src.db import *
from api.src.models import *

drop_all_tables(conn_dev, cursor)

# [{'type': 'hotel-offers', 'hotel': {'type': 'hotel', 'hotelId': 'BGMILBGB', 
# 'chainCode': 'BG', 'dupeId': '700025106', 'name': 'BULGARI HOTELS RESORTS MILANO', 
# 'rating': '5', 'cityCode': 'MIL', 'latitude': 45.47253, 'longitude': 9.18805, 
# 'address': {'lines': ['VIA PRIVATA FRATELLI GABBA 7B'], 'postalCode': '20121', 
# 'cityName': 'MILAN', 'countryCode': 'IT'}, 'contact': {'phone': '39-02-8058051', 
# 'fax': '39-02-805805222'}, 
# 'amenities': ['CONVENTION_CENTRE', 'MEETING_ROOMS', 'ICE_MACHINES', 'RESTAURANT', 'DISABLED_FACILITIES', 'DISABLED_ACCESSIBLE_TOILETS', 'ACCESSIBLE_PARKING', 'BABY-SITTING', 'BEAUTY_PARLOUR', 'CAR_RENTAL', 'ELEVATOR', 'EXCHANGE_FACILITIES', 'WIFI', 'LAUNDRY_SERVICE', 'SPA', 'VALET_PARKING', 'HAIRDRESSER', 'SWIMMING_POOL', 'AIR_CONDITIONING', 'HAIR_DRYER', 'MINIBAR', 'MOVIE_CHANNELS', 'ROOM_SERVICE', 'TELEVISION', 'SAFE_DEPOSIT_BOX', 'FITNESS_CENTER'], 
# 'media': [{'uri': 'http://pdt.multimediarepository.testing.amadeus.com/cmr/retrieve/hotel/B6AA0C7920214C49AAFBCFFF32A15300', 'category': 'EXTERIOR'}]}, 
# 'available': True, 'offers': [{'id': '8H6IEBBJW1', 'checkInDate': '2020-12-19', 'checkOutDate': '2020-12-20', 'rateCode': 'RAC', 
# 'rateFamilyEstimated': {'code': 'RAC', 'type': 'P'}, 'room': {'type': 'LCG', 'typeEstimated': {'category': 'SUPERIOR_ROOM', 'beds': 1, 'bedType': 'KING'}, 
# 'description': {'text': 'Short Break in Milano, breakfast daily\nSuperior Room garden view, 1 King, 35sqm/377sqf\nt, Wireless internet, complimentary, Wired inte', 'lang': 'EN'}}, 
# 'guests': {'adults': 1}, 'price': {'currency': 'EUR', 'total': '622.10', 'variations': {'average': {'base': '561.55'}}}, 'policies': {'paymentType': 'guarantee', 
# 'cancellation': {'numberOfNights': 1, 'amount': '622.10', 'deadline': '2020-12-17T23:59:00+01:00'}}}], 
# 'self': 'https://test.api.amadeus.com/v2/shopping/hotel-offers/by-hotel?hotelId=BGMILBGB'}]

# Hotel: 'id', 'amadeus_id', 'name', 'chain_id', 'rating', 'location_id'
# Chain: 'id', 'chain_code', 'name'
# Location: 'id', 'lon', 'lat', 'address', 'city_name', 'postal_code', 'country_code'
# Offer: 'id', 'offer_id', 'hotel_id', 'check_in', 'check_out', 'available', 'currency', 'total_rate', 'comm_percentage'
# Description: 'hotel_id', 'description', 'amenities', 'media_uri'

bulgari_chain = save(Chain(chain_code = 'BG', name = 'Bulgari'), conn_dev, cursor)

bulgari_location = save(Location(lon = 9.18805, lat = 45.47253, address = 'VIA PRIVATA FRATELLI GABBA 7B', city_name = 'MILAN', postal_code = '20121', country_code = 'IT'), conn_dev, cursor)

bulgari = save(Hotel(amadeus_id ='BGMILBGB', name = 'BULGARI HOTELS RESORTS MILANO', chain_id = bulgari_chain.id, rating = 5, location_id = bulgari_location.id), conn_dev, cursor)

bulgari_description = save(Description(hotel_id = bulgari.id, description = 'Short Break in Milano, breakfast daily. Superior Room garden view, 1 King, 35sqm/377sq', amenities = ['CONVENTION_CENTRE', 'MEETING_ROOMS', 'ICE_MACHINES', 'RESTAURANT'], media_uri = 'http://pdt.multimediarepository.testing.amadeus.com/cmr/retrieve/hotel/B6AA0C7920214C49AAFBCFFF32A15300'), conn_dev, cursor)

save(Offer(offer_id = '8H6IEBBJW1', hotel_id = bulgari.id, check_in = '2020-12-19', check_out = '2020-12-20', available = True, currency = 'EUR', total_rate = 622.10, comm_percentage = None), conn_dev, cursor)

bulgari2_location = save(Location(lon = -0.12624, lat = 51.50015, address = 'PORT EL KANTAOUI BP08', city_name = 'LONDON', postal_code = '4089', country_code = 'GB'), conn_dev, cursor)

bulgari2 = save(Hotel(amadeus_id ='BGLONBGB', name = 'TEST CONTENT', chain_id = bulgari_chain.id, rating = 5, location_id = bulgari2_location.id), conn_dev, cursor)

bulgari2_description = save(Description(hotel_id = bulgari2.id, description = 'Flexible Rate, see Rate Rules\nDlx room 43 sqm, Double beds / king bed, large \nbathroom featuring black Marquina marble bathtu', amenities = ['CONVENTION_CENTRE', 'MEETING_ROOMS', 'RESTAURANT'], media_uri = 'http://pdt.multimediarepository.testing.amadeus.com/cmr/retrieve/hotel/B6AA0C7920214C49AAFBCFFF32A15300'), conn_dev, cursor)

save(Offer(offer_id = 'AYZIDUK8H3', hotel_id = bulgari2.id, check_in = '2020-12-19', check_out = '2020-12-20', available = True, currency = 'GBP', total_rate = 903.00, comm_percentage = None), conn_dev, cursor)

melia_chain = save(Chain(chain_code = 'SM', name = 'Melia Hotels Intl'), conn_dev, cursor)

melia_location = save(Location(lon = 2.34846, lat = 48.85154, address = "7, RUE DE L'HOTEL COLBERT", city_name = 'PARIS', postal_code = '75005', country_code = 'FR'), conn_dev, cursor)

melia = save(Hotel(amadeus_id ='SMPARCOL', name = 'MELIA COLBERT', chain_id = melia_chain.id, rating = 4, location_id = melia_location.id), conn_dev, cursor)

melia_description = save(Description(hotel_id = melia.id, description = 'Semi-flexible Rate\nMELIA TWIN ROOM 1 PERSON\nPrivate Bathroom, Mini-bar, Colour TV, Radio,', amenities = ["BAR", "RESTAURANT", "ELEVATOR", "EXCHANGE_FACILITIES"], media_uri = 'http://uat.multimediarepository.testing.amadeus.com/cmr/retrieve/hotel/8068E4C4D7AB41A3BA9979FAE52F67BF'), conn_dev, cursor)

save(Offer(offer_id = 'JXDYBFEVC3', hotel_id = melia.id, check_in = '2020-12-19', check_out = '2020-12-20', available = True, currency = 'EUR', total_rate = 176.00, comm_percentage = 10.00), conn_dev, cursor)