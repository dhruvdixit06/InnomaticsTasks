import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("open_pubs_modified.csv")

st.set_page_config(page_title="Pub Locations", page_icon="🗺️", layout="wide")
st.header("All Pubs in UK:-")
st.caption("Pubs in specific area of UK")
loc_authority = st.selectbox('Select a Local Authority', list(df['local_authority'].unique()))

button_click = st.button('Search')
if button_click == True: 
    authority = df[df['local_authority'] == loc_authority]
    st.write("Pubs under the selected Local Authority:", len(authority))
    locations = authority[['latitude','longitude']]
    st.map(locations)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://media.istockphoto.com/photos/empty-white-marble-table-over-blur-store-background-banner-product-picture-id1090379972?k=20&m=1090379972&s=612x612&w=0&h=oBRZqsoa-7LfWxCYxutSH7RfN28ISJ8vJ6j5F9xSGO4=");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
