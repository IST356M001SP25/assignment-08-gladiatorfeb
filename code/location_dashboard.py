'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")
import streamlit as st
import pandas as pd
import pydeck as pdk

df = pd.read_csv("./cache/tickets_in_top_locations.csv")

location = st.selectbox("Choose a Location", df["location"].unique())

filtered = df[df["location"] == location]

st.metric("Total Tickets", len(filtered))
st.metric("Total Fines", f"${filtered['amount'].sum():,.2f}")

day_counts = filtered["dayofweek"].value_counts().sort_index()
hour_counts = filtered["hourofday"].value_counts().sort_index()

st.bar_chart(day_counts)
st.line_chart(hour_counts)

# Map
lat = filtered["lat"].iloc[0]
lon = filtered["lon"].iloc[0]

st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))
