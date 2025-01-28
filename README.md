# README.md

## AI-Powered Travel Planner

### Overview
The AI-Powered Travel Planner is a Streamlit application that generates personalized travel itineraries using Google Gemini's generative AI. Users can specify their preferences, destination, budget, and other details to receive a detailed day-by-day travel plan.

### Features
- **User-Friendly Interface:** Simple and intuitive design powered by Streamlit.
- **Personalized Itineraries:** Custom itineraries tailored to the user's preferences, budget, and mobility concerns.
- **Powered by AI:** Leverages Google Gemini's generative AI to create unique travel plans.
- **Travel Inspiration:** Includes dynamic travel photos for inspiration.

### How to Run the Application
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Google Gemini API key in the `api_key` variable in the code.
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Open the application in your browser at `http://localhost:8501`.

### Inputs
- **Destination:** Specify the travel location.
- **Duration:** Select the number of days for the trip.
- **Budget:** Choose a budget level (Low, Moderate, High).
- **Preferences:** Add preferences such as food, activities, or interests.
- **Dietary Restrictions:** Mention dietary preferences or restrictions.
- **Mobility Concerns:** Choose mobility requirements (No concerns, Minimal walking, Wheelchair accessible).
- **Accommodation Preferences:** Choose between luxury, budget-friendly, or central-location options.

### Outputs
- A detailed, day-by-day travel itinerary tailored to the user's preferences.
- Travel inspiration images to ignite wanderlust.

### Sample Prompts and Responses

#### System Prompt
"""
You are a smart travel planner AI. Create a detailed {duration}-day travel itinerary for the following details:
- Destination: {destination}
- Budget: {budget}
- Preferences: {preferences}
- Dietary Restrictions: {dietary_restrictions}
- Mobility Concerns: {mobility}
- Accommodation Preferences: {accommodation}
Format the output as a day-by-day itinerary.
"""

#### User Prompt
- Destination: Paris
- Duration: 3 days
- Budget: Moderate
- Preferences: Local food, art galleries, hidden gems
- Dietary Restrictions: Vegetarian
- Mobility: Minimal walking
- Accommodation: Central location

#### Model Response
"""
Day 1:
- Morning: Breakfast at a local cafe near Montmartre, followed by a visit to Sacré-Cœur Basilica.
- Afternoon: Explore the hidden art galleries in Le Marais and enjoy vegetarian lunch at Wild & The Moon.
- Evening: Dinner at a riverside restaurant with Seine views.

Day 2:
- Morning: Visit the Louvre Museum, focusing on lesser-known exhibits.
- Afternoon: Relax at Place des Vosges and enjoy a vegetarian falafel lunch.
- Evening: Take a Seine River cruise to enjoy the illuminated landmarks.

Day 3:
- Morning: Explore the Latin Quarter and its quaint bookshops and cafes.
- Afternoon: Visit the Musée d'Orsay for Impressionist art.
- Evening: Dinner at a rooftop restaurant with panoramic views of Paris.
"""

### Documentation for Prompt Process
1. **System Prompt:**
   - The system prompt defines the AI's role as a travel planner and outlines the format and details needed for the itinerary.
   - This ensures the response is structured and addresses all user inputs.

2. **Input Refinement:**
   - The user inputs are mapped directly into the system prompt, allowing the AI to clarify vague or incomplete preferences.
   - Example: If preferences are vague (e.g., "fun places"), the AI asks follow-up questions or infers specifics based on context.

3. **Response Validation:**
   - The model response is checked for coherence, alignment with user inputs, and logical flow of activities within the itinerary.

### Requirements
- Python 3.8+
- Google Gemini API key
- Dependencies listed in `requirements.txt`


### Acknowledgments
- [Streamlit](https://streamlit.io) for an amazing Python web app framework.
- [Google Gemini](https://ai.google/tools/) for generative AI capabilities.

---

# requirements.txt

streamlit>=1.20.0
google-generativeai>=0.2.0
