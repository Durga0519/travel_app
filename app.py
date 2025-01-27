import streamlit as st
import google.generativeai as genai


api_key = st.secrets["google_api"]["api_key"]

# Configure the Google Gemini API
api_key = "Your_api_key"  # Replace with your actual API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_itinerary(destination, duration, budget, preferences, dietary_restrictions, mobility, accommodation):
    # Prompt setup for Google Gemini
    prompt = f"""
    You are a smart travel planner AI. Create a detailed {duration}-day travel itinerary for the following details:
    - Destination: {destination}
    - Budget: {budget}
    - Preferences: {preferences}
    - Dietary Restrictions: {dietary_restrictions}
    - Mobility Concerns: {mobility}
    - Accommodation Preferences: {accommodation}
    Format the output as a day-by-day itinerary.
    """

    # Generate content using Google Gemini
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI setup
st.set_page_config(page_title="AI-Powered Travel Planner", page_icon="🌍", layout="centered")

# Title and Intro
st.title("🌍 AI-Powered Travel Planner")
st.markdown("""
Welcome to the AI-powered travel planner! 🚀
Create your personalized travel itinerary by entering your preferences below.
""")

# User Inputs Section
st.header("Your Travel Details")

# Destination Input
destination = st.text_input("📍 Enter your destination", "Paris")

# Duration Slider
duration = st.slider("⏳ Select the trip duration (in days)", 1, 14, 5)

# Budget Dropdown
budget = st.selectbox("💸 Select your budget", ["Low", "Moderate", "High"])

# Preferences Text Area
preferences = st.text_area("🍴 Describe your preferences (e.g., food, art, hidden gems, etc.)", "Local food, art galleries, hidden gems")

# Dietary Restrictions Input
dietary_restrictions = st.text_input("🚫 Do you have any dietary restrictions?", "None")

# Mobility Concerns Dropdown
mobility = st.selectbox("🦽 Mobility concerns?", ["No concerns", "Minimal walking", "Wheelchair accessible"])

# Accommodation Preferences Dropdown
accommodation = st.selectbox("🏨 Accommodation preference", ["Luxury", "Budget-friendly", "Central location"])

# Action Button to Generate Itinerary
st.markdown("---")  # Horizontal line for separation

if st.button("🎒 Generate Itinerary"):
    with st.spinner("Generating your personalized itinerary... Please wait."):
        itinerary_response = generate_itinerary(destination, duration, budget, preferences, dietary_restrictions, mobility, accommodation)
        
        st.success("🎉 Here is your personalized travel itinerary!")
        st.markdown(itinerary_response)

        # Optional: Add a section to display some inspiration images
        st.markdown("### Some Travel Inspiration 🌟")
        st.image("https://source.unsplash.com/800x400/?travel,adventure", caption="Explore the world!")
        
# Add footer to make it look complete
st.markdown("---")
st.markdown("Made with ❤️ by Your Travel Buddy")
