import requests

def printResult(repos):
  for repo in repos:
    name = repo['name']
    description = repo['description']
    url = repo['html_url']
    stars = repo['stargazers_count']
    print("name: ", name, "*-Star: ", stars)
    print("description: ", description)
    print("URL: ", url)
    print()

topSize = 10
githubURL = "https://api.github.com/search/repositories?q=Q&sort=stars&order=desc&per_page={topSize}"
response = requests.get(githubURL)
listOfReposJson = response.json()

printResult(listOfReposJson['items'])



