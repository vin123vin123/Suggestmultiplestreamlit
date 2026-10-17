import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Soccer Analytics", page_icon="⚽")
st.title("⚽ Soccer Insights & Live Standings")

# API Configuration (Using API-Football via RapidAPI)
API_KEY = st.sidebar.text_input("Enter RapidAPI Key", type="password")
API_HOST = "://rapidapi.com"

if not API_KEY:
    st.warning("Please enter your RapidAPI key in the sidebar to fetch live data. You can get one for free at RapidAPI.com.")
else:
    url = f"https://{API_HOST}/v3/standings"
    querystring = {"year": "2026", "league": "39"} # Premier League code is usually 39
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    @st.cache_data
    def fetch_soccer_standings():
        try:
            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return None

    data = fetch_soccer_standings()

    if data and "response" in data and len(data["response"]) > 0:
        league_name = data["response"][0]["league"]["name"]
        st.subheader(f"📊 Current Standings: {league_name}")
        
        standings_list = data["response"][0]["league"]["standings"][0]
        
        # Parse into a readable format
        parsed_data = []
        for team in standings_list:
            parsed_data.append({
                "Rank": team["rank"],
                "Team": team["team"]["name"],
                "Points": team["points"],
                "Played": team["all"]["played"],
                "Goals Diff": team["goalsDiff"]
            })
            
        df = pd.DataFrame(parsed_data)
        st.dataframe(df.set_index("Rank"), use_container_width=True)
    else:
        st.info("No data returned. Ensure your API key is valid and league parameters are correct.")
