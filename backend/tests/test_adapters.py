import api.src.models as models
import api.src.adapters as adapters
import api.src.db as db


json = {'type': 'hotel-offers', 'hotel': {'type': 'hotel', 'hotelId': 'BGMILBGB', 'chainCode': 'BG', 'dupeId': '700025106', 
'name': 'BULGARI HOTELS RESORTS MILANO', 'rating': '5', 'cityCode': 'MIL', 'latitude': 45.47253, 'longitude': 9.18805, 
'address': {'lines': ['VIA PRIVATA FRATELLI GABBA 7B'], 'postalCode': '20121', 'cityName': 'MILAN', 'countryCode': 'IT'}, 
'contact': {'phone': '39-02-8058051', 'fax': '39-02-805805222'}, 
'amenities': ['CONVENTION_CENTRE', 'MEETING_ROOMS', 'ICE_MACHINES', 'RESTAURANT', 'DISABLED_FACILITIES', 'DISABLED_ACCESSIBLE_TOILETS', 'ACCESSIBLE_PARKING', 'BABY-SITTING', 'BEAUTY_PARLOUR', 'CAR_RENTAL', 'ELEVATOR', 'EXCHANGE_FACILITIES', 'WIFI', 'LAUNDRY_SERVICE', 'SPA', 'VALET_PARKING', 'HAIRDRESSER', 'SWIMMING_POOL', 'AIR_CONDITIONING', 'HAIR_DRYER', 'MINIBAR', 'MOVIE_CHANNELS', 'ROOM_SERVICE', 'TELEVISION', 'SAFE_DEPOSIT_BOX', 'FITNESS_CENTER'], 'media': [{'uri': 'http://pdt.multimediarepository.testing.amadeus.com/cmr/retrieve/hotel/B6AA0C7920214C49AAFBCFFF32A15300', 'category': 'EXTERIOR'}]}, 
'available': True, 'offers': [{'id': '2EXFRBKV8D', 'checkInDate': '2020-12-31', 'checkOutDate': '2021-01-01', 'rateCode': 'RAC', 
'rateFamilyEstimated': {'code': 'BAR', 'type': 'P'}, 'room': {'type': 'REG', 'typeEstimated': {'category': 'DELUXE_ROOM', 'beds': 2, 'bedType': 'QUEEN'}, 
'description': {'text': 'Flexible Rate\nDeluxe room with 2 queen beds, 2 Queen, 40sqm/4\n30sqft, Wireless internet, for a fee, Wired int', 'lang': 'EN'}}, 
'guests': {'adults': 1}, 'price': {'currency': 'EUR', 'total': '973.00', 'variations': {'average': {'base': '879.87'}}}, 'policies': {'paymentType': 'guarantee', 
'cancellation': {'amount': '973.00', 'deadline': '2020-12-30T23:59:00+01:00'}}}], 'self': 'https://test.api.amadeus.com/v2/shopping/hotel-offers/by-hotel?hotelId=BGMILBGB'}

def test_hotel_attributes():
    builder = adapters.HotelBuilder()
    builder_details = builder.select_attributes(json)
    assert builder_details == {'amadeus_id': 'BGMILBGB', 'name': 'BULGARI HOTELS RESORTS MILANO', 'chain_id': 'BG', 'rating': '5'}

def test_location_attributes():
    location_builder = adapters.LocationBuilder()
    location_details = location_builder.select_attributes(json)
    assert location_details == {'lon': 9.18805, 'lat': 45.47253, 'address': 'VIA PRIVATA FRATELLI GABBA 7B', 'city_name': 'MILAN', 'postal_code': '20121', 'country_code': 'IT'}

def test_offer_attributes():
    offer_builder = adapters.OfferBuilder()
    offer_details = offer_builder.select_attributes(json)
    assert offer_details == {'offer_id': '2EXFRBKV8D', 'check_in': '2020-12-31', 'check_out': '2021-01-01', 'available': True, 'currency': 'EUR', 'total_rate': '973.00', 'comm_percentage': None}


# cleaned up the json
json_postal_break = {'type': 'hotel-offers', 'hotel': 
{'type': 'hotel', 'hotelId': 'AMJAIAAK', 'chainCode': 'AM', 'dupeId': '700035202', 
    'name': 'Aman-i-Khas', 'rating': '5', 'cityCode': 'JAI', 'latitude': 26.01736, 
    'longitude': 76.4556, 'address': {'lines': ['RANTHAMBHORE', 'RAJASTHAN'], 
    'cityName': 'RANTHAMBHORE', 'countryCode': 'IN', 'stateCode': 'RJ'}, 
    'contact': {'phone': '91-7462-252052', 'fax': '91-7462-252178', 
    'email': 'aman-i-khas@aman.com'}, 'description': {'lang': 'en', 
    'text': '''A wilderness location and a sensitive connection to Rajasthans 
    history and culture await guests at Aman-i-Khas an outpost on the threshold 
    of Ranthambore National Park inspired by lavish Mughal hunting parties of old. 
    Each of the ten soaring guest tents is beautifully furnished and assigned a personal 
    butler. In-between daily Jeep safaris to catch a glimpse of tigers and other
    wildlife guests can enjoy rejuvenating spa treatments or a dip in the traditional 
    step-well pool before drinks around a communal firepit and dinners lit by flickering 
    candles under a canopy of stars.\rTraditional treatments as well as Reiki healing - body 
    scrubs and facials soothe and revive in the spa tent.\rMade with vegetables and herbs 
   '''}, 'amenities':
   ['FEMA_FIRE_SAFETY_COMPLIANT', 'FIRST_AID_STAF', 'RESTAURANT', 'LOUNGE', 
   'MASSAGE', 'OUTDOOR_POOL', 'SPA', 'CAR_RENTAL', 'PARKING', 'VALET_PARKING', 
   'ROOM_SERVICE', 'INTERNET_SERVICES', 'FREE_INTERNET', 'INTERNET_HOTSPOTS', 'WIFI',
   'WIRELESS_CONNECTIVITY'], 
   'media': 
   [{'uri': 'https://d2573qu6qrjt8c.cloudfront.net/440C93E270674E02ADE6C0A1D25500B3/440C93E270674E02ADE6C0A1D25500B3.JPEG', 'category': 'RESTAURANT'}]}, 
'available': True, 'offers': [{'id': '3NC3TC5VMF', 'checkInDate': '2021-03-02', 'checkOutDate': '2021-03-03', 'rateCode': 'RAC', 
    'rateFamilyEstimated': {'code': 'RAC', 'type': 'P'}, 'commission': {'percentage': '10.00'}, 'boardType': 'FULL_BOARD', 'room': {'type': 'A1K', 'typeEstimated': {'beds': 1, 'bedType': 'KING'}, 'description': {'text': 'DAILY RATE INCL FULL BOARD \nTent-King or Twin-108sqm-1162sqft-Free Wifi-Garden view-\nOversized daybed for lounging Dining area-Twin writing desks-\nBathing area with shower-Bathtub-Separate toilet-Dressing area-\nTwin vanities-Sundeck-Air conditioning-Ceiling fan-Heating-Chest\ncooler for drinks ', 'lang': 'EN'}}, 'guests': {'adults': 1}, 'price': {'currency': 'USD', 'total': '1557.60', 'variations': {'average': {'base': '1200.00'}, 'changes': [{'startDate': '2021-03-02', 'endDate': '2021-03-03', 'base': '1200.00'}]}}, 'policies': {'deposit': {'deadline': '2021-02-05T00:00:00', 'acceptedPayments': {'creditCards': ['VI', 'CA', 'AX'], 'methods': ['CREDIT_CARD']}}, 'paymentType': 'deposit', 'cancellation': {'amount': '1557.60', 'deadline': '2021-01-31T00:00:00+05:30'}}}], 
'self': 'https://api.amadeus.com/v2/shopping/hotel-offers/by-hotel?hotelId=AMJAIAAK&checkInDate=2021-03-02&checkOutDate=2021-03-03'}

def test_location_postal_break():
    location_builder = adapters.LocationBuilder()
    location_details = location_builder.select_attributes(json_postal_break)
    assert location_details == {'lon': 76.4556, 'lat': 26.01736, 'address': 'RANTHAMBHORE', 'city_name': 'RANTHAMBHORE', 'postal_code': None, 'country_code': 'IN'}


