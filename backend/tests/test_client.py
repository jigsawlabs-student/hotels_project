import pytest
import psycopg2
import api.src.adapters as adapters
import api.src.db.db as db
import api.src.models as models

def test_client_response():
    hotel = adapters.HotelClient()
    response = hotel.amadeus.shopping.hotel_offers.get(
                    hotelIds="BGMILBGB", # TILONRHO,BGMILBGB,BGLONBGB
                    bestRateOnly='true')
    assert response.status_code == 200