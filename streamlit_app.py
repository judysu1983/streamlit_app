import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding markdown content
languages = {
    "English": """
# How to Apply for a Chinese Visa (English)

... (8000 words of content in English)
""",
    "Japanese": """
# 中国ビザの申請方法(日本語)

... (8000 words of content in Japanese)
""",
    "Korean": """
# 중국 비자 신청 방법 (한국어)

... (8000 words of content in Korean)
""",
    "Portuguese": """
# Como Solicitar um Visto Chinês (Português)

... (8000 words of content in Portuguese)
""",
    "French": """
# Comment demander un visa chinois (Français)

... (8000 words of content in French)
""",
    "Italian": """
# Come richiedere un visto cinese (Italiano)

... (8000 words of content in Italian)
""",
    "Traditional Chinese": """
# 如何申請中國簽證 (繁體中文)

... (8000 words of content in Traditional Chinese)
"""
}

# Create a sidebar for language selection
selected_language = st.sidebar.selectbox(" :de:", list(languages.keys()))

# Display the content based on the selected language
st.markdown(languages[selected_language])
