import streamlit as st
import requests
import pandas as pd
import datetime
import plotly.graph_objects as go
API_URL = "http://127.0.0.1:5000/hotels"


def find_hotels():
    response = requests.get(API_URL)
    return response.json()

def find_hotel_by_id(id):
    # response = requests.get(API_URL, params={'name': hotel_name})
    response = requests.get(f"{API_URL}/{id}")
    return response.json()

# Sidebar Hotel Selector
hotels = find_hotels()
hotel_name = st.sidebar.selectbox('Select Hotels', [hotel['name'] for hotel in hotels]) 

# Connect Sidebar to Chart, Return Hotel Id
def name_to_id(hotels, hotel_name):
    for hotel in hotels:
        if hotel['name'] == hotel_name:
            return hotel['id']
hotel_id = name_to_id(hotels, hotel_name)

# Chart of Prices
hotel_id_offers = find_hotel_by_id(hotel_id)["offers"]
hotel_rates = [hotel["total_rate"] for hotel in hotel_id_offers]
currency = [hotel["currency"] for hotel in hotel_id_offers]
name = find_hotel_by_id(hotel_id)["name"]
city = find_hotel_by_id(hotel_id)["location"]["city_name"]
check_in = [hotel["check_in"] for hotel in hotel_id_offers]

st.header(name)
st.subheader(city)
st.write(currency[0])
scatter = go.Scatter(x = check_in, 
        y = hotel_rates, 
        hovertext = name, mode = 'markers')
fig = go.Figure(scatter)
st.plotly_chart(fig)

# data = pd.DataFrame(find_locations())
# st.map(data)

# st.header("Hotel Information")
# offers = pd.DataFrame(
#     find_offers()
# )
# st.table(offers)


# def find_countries():
#     response = requests.get(f"{API_URL}/locations").json()
#     return [country["country_code"] for country in response]

# def find_chains():
#     response = requests.get(f"{API_URL}/chains").json()
#     return [hotel["name"] for hotel in response]

# def find_offers():
#     response = requests.get(f"{API_URL}/offers").json()
#     return response

# # Page Header
# st.title('Map of Hotels')

# #Sidebar Price Selector
# price = st.sidebar.slider(min_value = 300, max_value = 2000, step = 100, label = 'Maximum Price (Per Night)')

# #Sidebar Country Selector
# countries = st.sidebar.multiselect('Select Countries', find_countries())

# #Siebar Hotel Brand Selector
# chains = st.sidebar.multiselect('Select Hotel Brands', find_chains())

# #Sidebar Dates Selector
# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# check_in = st.sidebar.date_input('Check In', today)
# check_out = st.sidebar.date_input('Check Out', tomorrow)
# if check_in >= check_out:
#     st.sidebar.error('Error: Check out must be after check in.')