import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding text
languages = {
    "English": "This is the English guide for applying for a Chinese visa...",
    "Japanese": "これは中国ビザ申請のための日本語ガイドです...",
    "Korean": "이것은 중국 비자 신청을 위한 한국어 가이드입니다...",
    "Portuguese": "Este é o guia em português para solicitar um visto chinês...",
    "Chinese :de:": "This is the English guide for applying for a Chinese visa...",
    # Add more languages and their corresponding text here
}

# Create a sidebar for language selection
selected_language = st.sidebar.selectbox("Select Language", list(languages.keys()))

# Display the content based on the selected language
st.title(f"How to Apply for a Chinese Visa ({selected_language})")
st.write(languages[selected_language])
