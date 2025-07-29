"""Interface Streamlit do Vegapunk Agent"""
import streamlit as st
from langchain_core.messages import HumanMessage
from vegapunk import create_vegapunk_agent, DEFAULT_PROVIDER

# Configuração da página
st.set_page_config(page_title="Dr. Vegapunk", page_icon="🤖")

# Título
st.title("🧠 Dr. Vegapunk")
st.write("*O cientista mais genial dos mares digitais! Como o Vegapunk original, tenho respostas para tudo - só que com muito mais sarcasmo, cara.*")
st.caption("🏴‍☠️ Navegando pelos mares do conhecimento com atitude brasileira")

# Sidebar
with st.sidebar:
    st.header("Settings")
    provider = st.selectbox("LLM Provider", ["google"])
    st.info("💡 Busco informações como quem procura o One Piece - com determinação!")

# Cache do agente
@st.cache_resource
def load_agent(provider):
    return create_vegapunk_agent(provider=provider)

graph = load_agent(provider)

# Interface de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do chat
if prompt := st.chat_input("What's your question?"):
    # Mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Resposta do agente
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                messages = [HumanMessage(content=prompt)]
                result = graph.invoke({"messages": messages})
                response = result["messages"][-1].content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Botão limpar
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()