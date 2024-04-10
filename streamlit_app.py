import streamlit as st

# Set the app title
st.set_page_config(page_title="Chinese Visa Application Guide")

# Define the languages and their corresponding markdown content
languages = {
    "English": """
# How to Apply for a Chinese Visa (English)

## Introduction

This is the introduction section in English...

## Step 1

...

## Step 2

...

(8000 words of content in English)
""",
    "Japanese": """
# 中国ビザの申請方法(日本語)

## はじめに

これは日本語の紹介セクションです...

## ステップ1

...

## ステップ2

...

(8000 words of content in Japanese)
""",
    "Korean": """
# 중국 비자 신청 방법 (한국어)

## 소개

이것은 한국어 소개 섹션입니다...

## 1단계

...

## 2단계

...

(8000 words of content in Korean)
""",
    # Add more languages and their corresponding markdown content here
}

# Create a sidebar for language selection
selected_language = st.sidebar.selectbox("Select Language", list(languages.keys()))

# Display the content based on the selected language
st.markdown(languages[selected_language])
