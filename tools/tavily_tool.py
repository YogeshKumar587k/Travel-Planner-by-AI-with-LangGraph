from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILA_API_KEY"))

def tavily_search(query: str):
    """
    Search for travel destinations using the Tavily API.
    Args:
        query (str): The search query for travel destinations.
    """
    try:
        response = client.search(query,max_results=5)
    except Exception as e:
        print({"error": str(e)})
    results =[]

    for i,r in enumerate(response['results']):
        title = r.get('title', 'No title')
        url =r.get('url', '')
        snippet = r.get('snippet', '').strip()
        # keep only the first 300 characters of the snippet
        if len(snippet) > 300:
            snippet = snippet[:300].rstrip(" ",1)[0] + '...'
        results.append(f"{i}. **{title}**\n {url}\n ** {snippet}\n")
    return "\n\n".join (results)

        
        