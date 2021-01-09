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