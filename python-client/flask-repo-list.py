from flask import Flask, render_template
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

def getRepos():
  topSize = 10
  githubURL = "https://api.github.com/search/repositories?q=Q&sort=stars&order=desc&per_page={topSize}"
  response = requests.get(githubURL)
  listOfReposJson = response.json()
  return listOfReposJson['items']

app = Flask(__name__)

@app.route('/')
def listOfRepos():
  repos_list = getRepos();
  printResult(repos_list);
  return render_template('index.html', repos = repos_list)

if __name__ == '__main__':
    app.run(debug=True)