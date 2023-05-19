import requests
import json
from decouple import config

class CreatePR:
	def __init__(self):
		self.repo_owner = config('REPO_OWNER')
		self.repo_name = config('REPO_NAME')
		self.base_branch = config('BASE_BRANCH')
		self.head_branch = config('HEAD_BRANCH')
		self.pr_title = "testing PR programmatically"
		self.pr_body = "Testing the thing out"
		self.access_token = config('GITHUB_ACCESS_TOKEN')
		print("ds,nfnklsdnfkllfd")
    
	def call(self):
		print(f"Pull request URL: {self.repo_owner}")
		# url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"
		# response = requests.post(url, headers=self._headers(), data=json.dumps(self._data()))
		# if response.status_code == 201:
		# 	print("Pull request created successfully!")
		# 	pr_data = response.json()
		# 	print(f"Pull request URL: {pr_data['html_url']}")
		# else:
		# 	print("Failed to create pull request.")
		# 	print(f"Error message: {response.json()['message']}")

	def _headers(self):
		return {
        "Authorization": f"Bearer {self.access_token}",
        "Accept": "application/vnd.github.v3+json"
    	}

	def _data(self):
		return {
			"title": self.pr_title,
			"body": self.pr_body,
			"head": self.head_branch,
			"base": self.base_branch
    }

