from run_adapters import *

# Production Test - Tests the CSV of hotels to call from the API is properly opened and the Amadeus ID's are converted to a string to prepare for API call
# If add more hotels than Aman, update the hotel_ids str below:
hotel_ids = 'AMATHAAZ, AMBJVARU, AMCMBAAW, AMCMBAMA, AMCVFAAL, AMDPSAKA, AMDPSAMI, AMHGHAFA, AMHKTAMP, AMJACAMG, AMJAIAAK, AMJAIAMA, AMJOGABA, AMLJGAMA, AMLPQAAT, AMMNLAMP, AMNGOAMA, AMNHAAOI, AMPEKASP, AMPGAAGI, AMPLSAAY, AMPOPAME, AMQBAAAS, AMRAKTAH, AMREPASA, AMSHAAMN, AMSWQAWA, AMTYOATK, AMVCECGV, AMDPSASN, AMUKYANK'

def test_hotel_ids_prod():
    hotel_id_str = hotel_ids_str()
    assert hotel_id_str == hotel_ids

# Development Test - The hotels in Dev are a different list than in Production. Tests the CSV of Development hotels is properly opened and Amadeus ID's are converted to a string
dev_hotel_ids = ''

def test_hotel_ids_dev():
    hotel_id_str = hotel_ids_str()
    assert hotel_id_str == hotel_ids
