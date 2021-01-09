import api.src.adapters as adapters

def test_client_response():
    hotel = adapters.HotelClient()
    response = hotel.amadeus.shopping.hotel_offers.get(
                    hotelIds="BGMILBGB", # TILONRHO,BGMILBGB,BGLONBGB
                    bestRateOnly='true')
    assert response.status_code == 200