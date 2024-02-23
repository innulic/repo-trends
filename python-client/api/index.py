from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.base_client.errors import OAuthError
from os import getenv
from authlib.integrations.flask_client import OAuth
import requests
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

import login_data

def getRepos(user_login):
  if user_login is not None:
    return login_data.filteredRepos(user_login);
  else:
    return login_data.getTopStarredRepos();

oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("SECRET_ID"),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': ''},
)  

@app.route('/')
def listOfRepos():
  token = session.get("token");
  user_login = session.get("user_login");
  repos_list = getRepos(user_login);
  return render_template('index.html', repos = repos_list, token = token, user_login = user_login)

@app.route("/login")
def login():
    redirect_url = url_for("authorize", _external=True)
    return github.authorize_redirect(redirect_url)

@app.route("/authorize")
def authorize():
  try:
    token = github.authorize_access_token()
    resp = github.get('user', token=token)
    resp.raise_for_status()
    profile = resp.json()
    session["user_login"] = profile["login"]
    session["token"] = token
    return redirect('/')
  except OAuthError as ex:
    print(f"An error occurred: {ex}")
    return redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    # load_dotenv()
    app.run()