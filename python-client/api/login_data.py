from bs4 import BeautifulSoup
import requests

GITHUB_BASE_URL = "https://github.com/"

class Repository:
    def __init__(self, html_url, name, description, stargazers_count):
        self.html_url = html_url
        self.name = name
        self.description = description
        self.stargazers_count = stargazers_count

def getTrandingRepos(token):
    result = []
    trendingPage = requests.get(GITHUB_BASE_URL + "trending");
    soup = BeautifulSoup(trendingPage.content, 'html.parser')
    repos = soup.find_all('article', class_='Box-row')
    for repo in repos:
        link = repo.find('h2', class_='h3 lh-condensed').a
        name = link.text.strip()
        description_element = repo.find('p', class_='col-9 color-fg-muted my-1 pr-4')
        description = description_element.text.strip() if description_element is not None else None
        html_url = GITHUB_BASE_URL + link['href']
        stars = repo.find('a', class_='Link Link--muted d-inline-block mr-3').text.strip()
        result.append(Repository(html_url, name, description, stars))
    return result;
