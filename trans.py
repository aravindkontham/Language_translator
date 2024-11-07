import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator setup
translator = Translator()

# Set up Streamlit page configuration
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            color: #333;
        }
        .title-text {
            color: #0066ff;
            font-size: 2.5em;
            font-weight: bold;
            animation: fadeIn ease 2s;
        }
        .translate-button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            transition: transform 0.3s ease;
        }
        .translate-button:hover {
            transform: scale(1.1);
            background-color: #45a049;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .output-text {
            color: #00008b;
            font-size: 1.5em;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Application title
st.markdown("<div class='title-text'>🌐 Language Translator 🌐</div>", unsafe_allow_html=True)

# User input for text and language 
text_input = st.text_area("Enter text to translate:", "")
language_options = LANGUAGES  # This imports all available languages in googletrans
target_language = st.selectbox("Select target language:", options=list(language_options.values()))

# Translation button
if st.button("Translate", key="translate", help="Click to translate"):
    if text_input:
        # Get language code from selected language name
        language_code = list(language_options.keys())[list(language_options.values()).index(target_language)]
        
        # Translate and display the output
        translation = translator.translate(text_input, dest=language_code)
        
        # Display translated text
        st.markdown(f"<div class='output-text'>Translated Text: <strong>{translation.text}</strong></div>", unsafe_allow_html=True)
        
        # Display pronunciation if available
        if translation.pronunciation:
            st.markdown(f"<div class='output-text'>Pronunciation (in English): <strong>{translation.pronunciation}</strong></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='output-text'><em>Pronunciation not available.</em></div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter text to translate!")
