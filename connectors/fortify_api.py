
import requests

class FortifyAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    def get_projects(self):
        url = f"{self.base_url}/api/v1/projects"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_scan_results(self, project_id: int):
        url = f"{self.base_url}/api/v1/projects/{project_id}/issues"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
