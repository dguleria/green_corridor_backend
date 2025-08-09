
import requests

class AzureDevOpsAPI:
    def __init__(self, organization: str, project: str, token: str):
        self.organization = organization
        self.project = project
        self.token = token
        self.headers = {'Authorization': f'Basic {token}', 'Content-Type': 'application/json'}
        self.base_url = f"https://dev.azure.com/{organization}/{project}/_apis"
    
    def get_builds(self, top=5):
        url = f"{self.base_url}/build/builds?api-version=6.0&$top={top}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_releases(self, top=5):
        url = f"{self.base_url}/release/releases?api-version=6.0&$top={top}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
