"""Vegapunk Agent - Lógica principal"""
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from .tools import ALL_TOOLS
from .prompts import VEGAPUNK_SYSTEM_PROMPT
from .config import TEMPERATURE

def create_vegapunk_agent(provider: str = "google"):
    """Cria o agente Vegapunk"""
    # Seleciona o LLM
    if provider == "google":
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=TEMPERATURE)
    elif provider == "groq":
        llm = ChatGroq(model="qwen-qwq-32b", temperature=TEMPERATURE)
    else:
        raise ValueError("Provider deve ser 'google' ou 'groq'")
    
    # Vincula ferramentas
    llm_with_tools = llm.bind_tools(ALL_TOOLS)
    
    # Mensagem do sistema
    sys_msg = SystemMessage(content=VEGAPUNK_SYSTEM_PROMPT)
    
    def assistant(state: MessagesState):
        """Nó do assistente"""
        messages_with_system = [sys_msg] + state["messages"]
        return {"messages": [llm_with_tools.invoke(messages_with_system)]}
    
    # Constrói o grafo
    builder = StateGraph(MessagesState)
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(ALL_TOOLS))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    
    return builder.compile()