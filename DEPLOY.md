# 🚀 Deploy no Streamlit Community Cloud

## Pré-requisitos
- Conta no GitHub
- Conta no Streamlit Community Cloud (https://share.streamlit.io)
- Repositório público no GitHub

## Passo a Passo

### 1. Preparar o Repositório
```bash
# Adicionar .gitignore
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# Commit e push
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 2. Criar secrets.toml (local)
```bash
mkdir -p .streamlit
```

Criar arquivo `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
TAVILY_API_KEY = "your_tavily_api_key_here"
```

### 3. Atualizar config.py para Streamlit Cloud
Adicionar suporte a secrets do Streamlit:
```python
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Função para pegar secrets
def get_secret(key):
    try:
        return st.secrets[key]
    except:
        return os.getenv(key)

# API Keys
GOOGLE_API_KEY = get_secret("GOOGLE_API_KEY")
TAVILY_API_KEY = get_secret("TAVILY_API_KEY")
```

### 4. Deploy no Streamlit Cloud

1. **Acesse**: https://share.streamlit.io
2. **Login** com GitHub
3. **New app** → **From existing repo**
4. **Repository**: seu-usuario/vegapunk-agent
5. **Branch**: main
6. **Main file path**: app.py
7. **App URL**: escolha um nome único

### 5. Configurar Secrets na Plataforma

1. **Advanced settings** → **Secrets**
2. Adicionar:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
TAVILY_API_KEY = "your_tavily_api_key_here"
```

### 6. Deploy
- Clique **Deploy**
- Aguarde o build (2-3 minutos)
- App estará disponível na URL escolhida

## ⚠️ Importante
- Nunca commite `.env` ou secrets
- Use apenas repositórios públicos (plano gratuito)
- Limite de recursos no plano gratuito

## 🔄 Atualizações
Qualquer push para `main` redeploya automaticamente.