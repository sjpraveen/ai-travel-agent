import warnings

warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="AI Travel Planner Agent", layout="wide")
st.title("AI Travel Planner Agent")

with st.form("travel_planner_form"):
    city = st.text_input("Enter the city you want to visit:")
    days = st.number_input("Enter the number of days for your trip:", min_value=1, max_value=30, value=5)
    interests = st.multiselect("Select your interests:", ["Culture", "Nature", "Food", "History", "Adventure"])
    style = st.selectbox("Select your travel style:", ["Budget", "Luxury", "Family", "Solo"])
    pace = st.selectbox("Select your travel pace:", ["Relaxed", "Moderate", "Fast"])
    month = st.selectbox("Select the month of your trip:", ["Any Month"] + ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    
    submit_button = st.form_submit_button("Plan My Trip")
    
if submit_button:
    if city and interests:
        planner = TravelPlanner()
        itinerary = planner.create_itinerary(city=city, 
                                             days=days, 
                                             interests= interests, 
                                             style=style, 
                                             pace=pace, 
                                             month=None if month == "Any Month" else month)
        st.subheader("Your Personalized Itinerary is ready:")
        st.markdown(itinerary)
        logger.info("Itinerary generated successfully.")    
    else:
        st.error("Please enter a city and select at least one interest to plan your trip.")    