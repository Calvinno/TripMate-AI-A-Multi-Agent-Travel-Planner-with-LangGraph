from langchain_community.tools.tavily_search import TavilySearchResults
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Initialisation de l'outil avec le paquet à jour
search_tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced"
)

def tavily_search(query):
    # LangChain exécute la recherche et renvoie directement une liste de dictionnaires
    response = search_tool.invoke(query)

    results = []

    # On itère directement sur 'response' (qui est la liste)
    for i, r in enumerate(response, 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)