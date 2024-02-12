from bs4 import BeautifulSoup
import requests
import locale
from concurrent.futures import ThreadPoolExecutor

GITHUB_BASE_URL = "https://github.com"
GITHUBAPI_BASE_URL = "https://api.github.com"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Repository:
    def __init__(self, html_url, name, description, stargazers_count):
        self.html_url = html_url
        self.name = name
        self.description = description
        self.stargazers_count = stargazers_count

def filteredRepos(username):
        trendingRepos = getTrendingRepos()
        reposWithUserInterest = getAllRepos(username)
        trendingRepos = [
            repo for repo in trendingRepos
            if repo.html_url not in {user_interested_repo.html_url for user_interested_repo in reposWithUserInterest}
        ]
        return trendingRepos;

def getTopStarredRepos(topSize=10):
    githubURL =  f"{GITHUBAPI_BASE_URL}/search/repositories?q=Q&sort=stars&order=desc&per_page={topSize}"
    response = requests.get(githubURL)
    listOfReposJson = response.json()
    return listOfReposJson['items']

def getReposFromUrl(url):
    result = []
    while url:
        response = requests.get(url)
        reposJson = response.json();
        for repo in reposJson:
            result.append(Repository(repo['html_url'], repo['name'], repo['description'], repo['stargazers_count']))
        if 'next' in response.links:
            url = response.links['next']['url']  # Get the URL for the next page
        else:
            url = None  # No more pages
    return result

def getWatchedRepos(username):
    url = f'https://api.github.com/users/{username}/subscriptions'
    return getReposFromUrl(url)

def getForkedRepos(username):
        url = f'https://api.github.com/users/{username}/repos?type=forks'
        return getReposFromUrl(url)

def getAllStarredRepos(username):
    url = f'https://api.github.com/users/{username}/starred'
    return getReposFromUrl(url)

def getAllRepos(username):
    with ThreadPoolExecutor(max_workers=3) as executor:
        watched_future = executor.submit(getWatchedRepos, username)
        forked_future = executor.submit(getForkedRepos, username)
        starred_future = executor.submit(getAllStarredRepos, username)

    watched_repos = watched_future.result()
    forked_repos = forked_future.result()
    starred_repos = starred_future.result()

    return watched_repos + forked_repos + starred_repos;

def getTrendingRepos():
    result = []
    trendingPage = requests.get(f"{GITHUB_BASE_URL}/trending");
    soup = BeautifulSoup(trendingPage.content, 'html.parser')
    repos = soup.find_all('article', class_='Box-row')
    for repo in repos:
        link = repo.find('h2', class_='h3 lh-condensed').a
        name = link.text.strip()
        description_element = repo.find('p', class_='col-9 color-fg-muted my-1 pr-4')
        description = description_element.text.strip() if description_element is not None else None
        html_url = GITHUB_BASE_URL + link['href']
        stars = locale.atoi(repo.find('a', class_='Link Link--muted d-inline-block mr-3').text.strip())
        result.append(Repository(html_url, name, description, stars))
    return result;
