import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    # response.raise_for_status()  # Ensure we notice bad responses
    # return response.text
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.find_all("a")) #finding all anchor tags

fetch_page(input("Enter URL: "))
