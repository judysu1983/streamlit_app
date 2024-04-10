import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding markdown content
languages = {
    "English": ("""
# How to Apply for a Chinese Visa (English)

... (8000 words of content in English)
""", "Select Language"),
    "Japanese": ("""
# 中国ビザの申請方法(日本語)

... (8000 words of content in Japanese)
""", "言語を選択"),
    "Korean": ("""
# 중국 비자 신청 방법 (한국어)

... (8000 words of content in Korean)
""", "언어 선택"),
    "Portuguese": ("""
# Como Solicitar um Visto Chinês (Português)

... (8000 words of content in Portuguese)
""", "Selecione o Idioma"),
    "French": ("""
# Comment demander un visa chinois (Français)

... (8000 words of content in French)
""", "Sélectionnez la langue"),
    "Italian": ("""
# Come richiedere un visto cinese (Italiano)

... (8000 words of content in Italian)
""", "Seleziona la lingua"),
    "Traditional Chinese": ("""
# 如何申請中國簽證 (繁體中文)

... (8000 words of content in Traditional Chinese)
""", "選擇語言")
}

# Create a sidebar for language selection
language_options = [lang for lang, _ in languages.values()]
selected_language = st.sidebar.selectbox(language_options[0], language_options)
selected_content, _ = languages[selected_language]

# Display the content based on the selected language
st.markdown(selected_content)
