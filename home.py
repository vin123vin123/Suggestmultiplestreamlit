import streamlit as st

st.set_page_config(
    page_title="Global Sports Dashboard",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Global Sports Analytics Dashboard")
st.write("Welcome to your ultimate hub for real-time **Soccer** and **Tennis** insights.")

st.markdown("""
### 🧭 How to Navigate:
*   **⚽ Soccer Section:** View live scores, league standings, and top scorers using free football APIs.
*   **🎾 Tennis Section:** Track player rankings, upcoming tournaments, and historical head-to-head match stats.
""")

# Quick summary or placeholder dashboard metrics
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Tracked Soccer Leagues", value="15+", delta="Live Data")
with col2:
    st.metric(label="Active Tennis Players", value="500+", delta="ATP / WTA")
