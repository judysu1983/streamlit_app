import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding markdown content
languages = {
    "English": ("# How to Apply for a Chinese Visa (English)\n\n... (8000 words of content in English)", "Select Language"),
    "Japanese": ("# 中国ビザの申請方法(日本語)\n\n... (8000 words of content in Japanese)", "言語を選択"),
    "Korean": ("# 중국 비자 신청 방법 (한국어)\n\n... (8000 words of content in Korean)", "언어 선택"),
    "Portuguese": ("# Como Solicitar um Visto Chinês (Português)\n\n... (8000 words of content in Portuguese)", "Selecione o Idioma"),
    "Chinese": ("# 如何申请中国签证 (中文)\n\n... (8000 words of content in Chinese)", "选择语言"),
    "Persian": ("# چگونه ویزای چین را درخواست کنیم (فارسی)\n\n... (8000 words of content in Persian)", "زبان را انتخاب کنید"),
    "Arabic": ("# كيفية التقدم بطلب للحصول على تأشيرة صينية (العربية)\n\n... (8000 words of content in Arabic)", "اختر اللغة"),
    "French": ("# Comment demander un visa chinois (Français)\n\n... (8000 words of content in French)", "Sélectionnez la langue"),
    "Italian": ("# Come richiedere un visto cinese (Italiano)\n\n... (8000 words of content in Italian)", "Seleziona la lingua"),
    "German": ("# Wie man ein chinesisches Visum beantragt (Deutsch)\n\n... (8000 words of content in German)", "Wählen Sie die Sprache"),
    "Spanish": ("# Cómo solicitar una visa china (Español)\n\n... (8000 words of content in Spanish)", "Selecciona el idioma")
}

# Create a sidebar for language selection
language_options = [lang_text for _, lang_text in languages.values()]
selected_language_text = st.sidebar.selectbox(language_options[0], language_options)
selected_content, _ = next((content, lang_text) for content, lang_text in languages.values() if lang_text == selected_language_text)

# Display the content based on the selected language
st.markdown(selected_content)
