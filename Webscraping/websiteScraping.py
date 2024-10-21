import requests
from bs4 import BeautifulSoup

def scrape_directory(url):
    """Scrapes a web directory and extracts links."""

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/'):
            href = url + href
        links.append(href)

    return links

def crawl_website(url, depth=1):
    """Crawls a website recursively to a specified depth."""

    if depth == 0:
        return []

    links = scrape_directory(url)

    all_links = links.copy()
    for link in links:
        if link.startswith(url):
            all_links.extend(crawl_website(link, depth - 1))

    return all_links

if __name__ == '__main__':
    base_url = "https://www.cseproject.drngpit.ac.in/" 
    links = crawl_website(base_url, depth=2)

    for link in links:
        print(link)