import webbrowser
import objc

def search_google(query):
    print(f"Searching Google for: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
