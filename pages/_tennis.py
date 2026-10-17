import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Tennis Analytics", page_icon="🎾")
st.title("🎾 Tennis Player Rankings & Metrics")

API_KEY = st.sidebar.text_input("Enter RapidAPI Key", type="password", key="tennis_key")
API_HOST = "://rapidapi.com" # Example free-tier tennis API on RapidAPI

if not API_KEY:
    st.warning("Please enter your RapidAPI key in the sidebar to fetch live tennis rankings.")
else:
    # Example endpoint for ATP Rankings
    url = f"https://{API_HOST}/api/tennis/rankings/atp"
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    @st.cache_data
    def fetch_tennis_rankings():
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return None

    tennis_data = fetch_tennis_rankings()

    if tennis_data:
        st.subheader("🥇 ATP Top Rankings")
        # Structure this according to your exact API JSON response structure
        # Below is a mock example assuming a list layout:
        # df = pd.DataFrame(tennis_data['rankings'])
        # st.dataframe(df)
        st.success("API connection successful! Render your parsed data array into dataframes here.")
