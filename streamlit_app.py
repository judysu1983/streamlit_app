import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding markdown content
languages = {
    "English": "# How to Apply for a Chinese Visa (English)\n\n... (8000 words of content in English)",
    "Japanese": "# 中国ビザの申請方法(日本語)\n\n... (8000 words of content in Japanese)",
    "Korean": "# 중국 비자 신청 방법 (한국어)\n\n... (8000 words of content in Korean)",
    "Portuguese": "# Como Solicitar um Visto Chinês (Português)\n\n... (8000 words of content in Portuguese)",
    "Chinese": "# 如何申请中国签证 (中文)\n\n... (8000 words of content in Chinese)",
    "Persian": "# چگونه ویزای چین را درخواست کنیم (فارسی)\n\n... (8000 words of content in Persian)",
    "Arabic": "# كيفية التقدم بطلب للحصول على تأشيرة صينية (العربية)\n\n... (8000 words of content in Arabic)",
    "French": "# Comment demander un visa chinois (Français)\n\n... (8000 words of content in French)",
    "Italian": "# Come richiedere un visto cinese (Italiano)\n\n... (8000 words of content in Italian)",
    "German": "# Wie man ein chinesisches Visum beantragt (Deutsch)\n\n... (8000 words of content in German)",
    "Spanish": "# Cómo solicitar una visa china (Español)\n\n... (8000 words of content in Spanish)"
}

# Create a sidebar for language selection
selected_language = st.sidebar.selectbox("", list(languages.keys()))

# Display the content based on the selected language
st.markdown(languages[selected_language])
