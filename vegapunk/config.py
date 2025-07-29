"""Configurações do Vegapunk Agent"""
import os
from dotenv import load_dotenv

load_dotenv()

# Função para pegar secrets (Streamlit Cloud ou .env)
def get_secret(key):
    try:
        import streamlit as st
        return st.secrets[key]
    except:
        return os.getenv(key)

# API Keys
GOOGLE_API_KEY = get_secret("GOOGLE_API_KEY")
GROQ_API_KEY = get_secret("GROQ_API_KEY")
TAVILY_API_KEY = get_secret("TAVILY_API_KEY")

# Settings
DEFAULT_PROVIDER = "google"
TEMPERATURE = 0.8
MAX_SEARCH_RESULTS = 3
MAX_WIKI_DOCS = 2