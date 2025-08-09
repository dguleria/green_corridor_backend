
import requests
from requests.auth import HTTPBasicAuth

class SonarQubeAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.auth = HTTPBasicAuth(token, '')  # token as username, empty password
    
    def get_projects(self):
        url = f"{self.base_url}/api/projects/search"
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        return response.json()
    
    def get_issues(self, project_key: str):
        url = f"{self.base_url}/api/issues/search?projectKeys={project_key}"
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        return response.json()
