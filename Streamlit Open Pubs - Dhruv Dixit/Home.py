import streamlit as st
import pandas as pd

df = pd.read_csv("open_pubs_modified.csv")

st.set_page_config(page_title="Home", page_icon="🍻",layout="wide")
st.title("🥂WELCOME!🥂")
st.subheader("Find Nearest Pub!")
st.header("All details:-")
total_pubs= len(df['fsa_id'].unique())
total_localAuthority= len(df['local_authority'].unique())
total_postalCodes= len(df['postcode'].unique())
st.subheader(f"Total pubs in United Kingdom is {total_pubs}")
st.subheader(f"Total local authorities of pubs is {total_localAuthority}")
st.subheader(f"Total postal codes in United Kingdom is {total_postalCodes}")
st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: x-large;
}
</style>
""",
    unsafe_allow_html=True,
)
with st.expander(label="Glimpse of dataset:-",expanded=False):
    st.dataframe(df.head(20))
page_bg_img = '''
<style>
.stApp {
background-image: url("https://media.istockphoto.com/photos/empty-white-marble-table-over-blur-store-background-banner-product-picture-id1090379972?k=20&m=1090379972&s=612x612&w=0&h=oBRZqsoa-7LfWxCYxutSH7RfN28ISJ8vJ6j5F9xSGO4=");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
