import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Indian Language Translator", page_icon="🌍")

st.title("🌍 Indian Language Translator")
st.caption("English ↔ Indian Languages (Auto Translate, No Ctrl Needed)")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Urdu": "ur",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Assamese": "as",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

from_lang = st.selectbox("From Language", languages.keys(), index=0)
to_lang = st.selectbox("To Language", languages.keys(), index=1)

text = st.text_input("Enter text")

if text:
    try:
        translated = GoogleTranslator(
            source=languages[from_lang],
            target=languages[to_lang]
        ).translate(text)

        st.success(translated)

    except Exception as e:
        st.error("Translation failed. Please try again.")
