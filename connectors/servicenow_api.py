
import requests
from requests.auth import HTTPBasicAuth

class ServiceNowAPI:
    def __init__(self, instance_url: str, client_id: str, client_secret: str, token_url: str):
        self.instance_url = instance_url.rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token = None
    
    def authenticate(self):
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        self.token = response.json()['access_token']
        self.headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
    
    def get_cmdb_items(self, limit=10):
        if not self.token:
            self.authenticate()
        url = f"{self.instance_url}/api/now/table/cmdb_ci?sysparm_limit={limit}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
