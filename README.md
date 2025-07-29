# 🧠 Dr. Vegapunk Agent

> *O cientista mais genial dos mares digitais! Como o Vegapunk original, tenho respostas para tudo - só que com muito mais sarcasmo, cara.*

Um agente de IA sarcástico e brasileiro construído com LangGraph, inspirado no Dr. Vegapunk de One Piece.

## 🚀 Funcionalidades

- **Chat sarcástico** em português brasileiro
- **Ferramentas matemáticas** (soma, subtração, multiplicação, divisão)
- **Busca na Wikipedia** para informações gerais
- **Busca na web** com Tavily para informações atualizadas
- **Interface Streamlit** intuitiva

## 🛠️ Tecnologias

- **LangGraph** - Framework para agentes
- **LangChain** - Integração com LLMs
- **Streamlit** - Interface web
- **Google Gemini** - Modelo de linguagem
- **Tavily** - Busca web
- **Wikipedia API** - Busca enciclopédica

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <repo-url>
cd vegapunk-agent
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o .env com suas API keys
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

## 🔑 Variáveis de Ambiente

```env
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 🏗️ Estrutura do Projeto

```
vegapunk-agent/
├── vegapunk/           # Pacote principal
│   ├── agent.py        # Lógica do agente
│   ├── config.py       # Configurações
│   ├── prompts.py      # Sistema de prompts
│   └── tools.py        # Ferramentas
├── app.py              # Interface Streamlit
├── requirements.txt    # Dependências
└── .env.example        # Template de variáveis
```

## 🎯 Como Usar

1. Abra a interface no navegador
2. Digite sua pergunta no chat
3. O Dr. Vegapunk responderá com seu sarcasmo característico
4. Use ferramentas matemáticas ou peça buscas na web/Wikipedia

## 🤖 Personalidade do Agente

- **Muito sarcástico**: "Francamente, cara...", "Sério mesmo?"
- **Gírias brasileiras**: "cara", "mano", "trem", "uai"
- **Respostas diretas**: máximo 2 frases
- **Zoeiro mas prestativo**: sempre ajuda, mesmo zoando

## 📝 Exemplos de Uso

```
Usuário: "Quanto é 2 + 2?"
Vegapunk: "Sério mesmo, cara? 2 + 2 = 4. Que pergunta óbvia..."

Usuário: "Quem te criou?"
Vegapunk: "O Caio me criou, cara! Aquele maluco viciado em moto."

Usuário: "Pesquise sobre One Piece"
Vegapunk: "Agora sim, mano! Vou buscar sobre o melhor anime que existe..."
```

## 🔧 Desenvolvimento

Para adicionar novas ferramentas, edite `vegapunk/tools.py`:

```python
@tool
def nova_ferramenta(param: str) -> str:
    """Descrição da ferramenta."""
    return resultado
```

Para modificar a personalidade, edite `vegapunk/prompts.py`.

## 📄 Licença

MIT License - Criado por Caio Campos