import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    # response.raise_for_status()  # Ensure we notice bad responses
    # return response.text
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title.string) #printing the title of the page
    print(soup.find_all("a")) #finding all anchor tags
    
    tag = soup.find_all("a")
    for t in tag:
        print(t.get("href")) #printing all the href attributes of anchor tags


fetch_page(input("Enter URL: "))
