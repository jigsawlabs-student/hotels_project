import streamlit as st
import requests
import pandas as pd
import datetime
import plotly.graph_objects as go
API_URL = "http://127.0.0.1:5000/"


def find_locations():
    response = requests.get(f"{API_URL}/locations")
    return response.json()

def find_countries():
    response = requests.get(f"{API_URL}/locations").json()
    return [country["country_code"] for country in response]

def find_chains():
    response = requests.get(f"{API_URL}/chains").json()
    return [hotel["name"] for hotel in response]

def find_offers():
    response = requests.get(f"{API_URL}/offers").json()
    return response

#Page Header
# st.title('Map of Hotels')

#Sidebar Price Selector
price = st.sidebar.slider(min_value = 300, max_value = 2000, step = 100, label = 'Maximum Price (Per Night)')

#Sidebar Country Selector
countries = st.sidebar.multiselect('Select Countries', find_countries())

#Siebar Hotel Brand Selector
chains = st.sidebar.multiselect('Select Hotel Brands', find_chains())

#Sidebar Dates Selector
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
check_in = st.sidebar.date_input('Check In', today)
check_out = st.sidebar.date_input('Check Out', tomorrow)
if check_in >= check_out:
    st.sidebar.error('Error: Check out must be after check in.')



# data = pd.DataFrame(
#     find_locations()
# )
# st.map(data)

# st.header("Hotel Information")
# offers = pd.DataFrame(
#     find_offers()
# )
# st.table(offers)

