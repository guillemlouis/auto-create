import requests
import json
import sys
import os

dev_folder = os.path.expanduser("~") + "/Dev"
username = 'youusername'
token = 'yourtoken'
url = 'https://api.github.com/user/repos'
project_name = sys.argv[1]

def create():
    os.mkdir(dev_folder+"/"+ project_name)
    project_folder = dev_folder+"/"+ project_name


    gh_session = requests.Session()
    gh_session.auth = (username, token)


    repo_param = {
        "name": project_name,
        "auto_init" : True
    }


    repo_response = json.loads(gh_session.post(url,json=repo_param).text)

    os.system("git clone "+ repo_response['clone_url'] + " " + project_folder)

if __name__ == "__main__":
    create()