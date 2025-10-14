import streamlit as st
import joblib

# Load saved pipeline
@st.cache_resource
def load_model():
    return joblib.load('model.joblib')

model = load_model()

st.title("📰 Fake News Detection System")

news_text = st.text_area("Enter a news headline or article:")

if st.button("Detect"):
    if news_text.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([news_text])[0]

        # Set background color based on prediction
        if prediction.lower() == 'real':
            color = "#d4edda"  # light green
            text_color = "#155724"
        else:
            color = "#f8d7da"  # light red
            text_color = "#721c24"

        st.markdown(
            f"<div style='background-color: {color}; color: {text_color}; padding: 15px; border-radius: 5px;'>"
            f"<h4>News Type: {prediction.upper()}</h4>"
            f"</div>",
            unsafe_allow_html=True
        )
