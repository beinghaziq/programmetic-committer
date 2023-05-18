import requests
import json
from decouple import config

API_USERNAME = config('USER')
API_KEY = config('KEY')

# Define the necessary variables
repo_owner = "owner"
repo_name = "repo"
base_branch = "main"
head_branch = "test_pr_prog"
pr_title = "testing PR programetically"
pr_body = "Testing the thing out"
access_token = "abc"

# Set the API endpoint URL
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"

# Set the headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Set the data for the pull request
data = {
    "title": pr_title,
    "body": pr_body,
    "head": head_branch,
    "base": base_branch
}

# Send a POST request to create the pull request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 201:
    print("Pull request created successfully!")
    pr_data = response.json()
    print(f"Pull request URL: {pr_data['html_url']}")
else:
    print("Failed to create pull request.")
    print(f"Error message: {response.json()['message']}")
