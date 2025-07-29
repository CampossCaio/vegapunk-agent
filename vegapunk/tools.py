"""Ferramentas do Vegapunk Agent"""
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.document_loaders import WikipediaLoader
from .config import MAX_SEARCH_RESULTS, MAX_WIKI_DOCS

# Ferramentas matemáticas
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Ferramentas de busca
@tool
def wiki_search(query: str) -> str:
    """Search Wikipedia for a query."""
    search_docs = WikipediaLoader(query=query, load_max_docs=MAX_WIKI_DOCS).load()
    formatted_search_docs = "\n\n---\n\n".join([
        f'<Document source="{doc.metadata["source"]}"/>\n{doc.page_content}\n</Document>'
        for doc in search_docs
    ])
    return {"wiki_results": formatted_search_docs}

@tool
def web_search(query: str) -> str:
    """Search the web for a query."""
    search_docs = TavilySearchResults(max_results=MAX_SEARCH_RESULTS).invoke(query=query)
    formatted_search_docs = "\n\n---\n\n".join([
        f'<Document source="{doc.metadata["source"]}"/>\n{doc.page_content}\n</Document>'
        for doc in search_docs
    ])
    return {"web_results": formatted_search_docs}

# Lista de todas as ferramentas
ALL_TOOLS = [multiply, add, subtract, divide, wiki_search, web_search]