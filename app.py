import streamlit as st
import pickle
from feature_extraction import extract_features

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit app
st.title("Phishing Website Detection")
st.write("Enter a website URL to check if it's likely phishing or safe.")

# Input field for website address
url_input = st.text_input("Website URL")

# Button to detect phishing
if st.button("Detect Phishing"):
    if url_input:
        # Check if the URL has http:// or https://
        if not (url_input.startswith("http://") or url_input.startswith("https://")):
            st.warning("Please enter a full URL starting with http:// or https://")
        else:
            # Extract features from the input URL
            features = extract_features(url_input)

            # Scale the features
            features_scaled = scaler.transform(features)

            # Make a prediction
            prediction = model.predict(features_scaled)

            # Display the result
            if prediction[0] == 1:
                st.error("Warning: This URL is likely a phishing website.")
            else:
                st.success("This URL is likely safe.")
    else:
        st.warning("Please enter a URL.")
