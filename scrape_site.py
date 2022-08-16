from bs4 import BeautifulSoup
import requests
import urllib.request
import wikipedia
from lxml import html
import requests
    
        
def scrape_wikipedia(input):
    output = wikipedia.summary(input)
    output1 = output.splitlines()
    print(output1[0])
    final = output1[0]      
    return final

def scrape_tech_news():
    # Send request to get the web page
    response = requests.get('https://gadgets.ndtv.com/news')
    
    # Check if the request succeeded (response code 200)
    if (response.status_code == 200):
    
        # Parse the html from the webpage
        pagehtml = html.fromstring(response.text)
    
        # search for news headlines
        news = pagehtml.xpath('//a/span[@class="news_listing"]/text()')
        
    # Print each news item in a new line
    print("\n".join(news))
    final = "\n".join(news)
    return final
    
