import requests

class WebSearchHandler:
    def __init__(self):
        self.search_url = "https://www.google.com/search"
    
    def search_duckduckgo(self, query):
        try:
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json"
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            abstract = data.get("AbstractText", "")
            if abstract:
                return abstract[:500]
            
            topics = data.get("RelatedTopics", [])
            if topics:
                return topics[0].get("Text", "No results found.")
            
            return "No results found for that query."
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def format_search_response(self, result):
        return f"Here's what I found: {result}"