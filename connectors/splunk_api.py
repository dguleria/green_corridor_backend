
import requests

class SplunkAPI:
    def __init__(self, base_url: str, client_id: str, client_secret: str, token_url: str):
        self.base_url = base_url.rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token = None
        self.headers = {}
    
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
    
    def search(self, query: str, earliest_time: str = "-24h", latest_time: str = "now"):
        if not self.token:
            self.authenticate()
        url = f"{self.base_url}/services/search/jobs/export"
        params = {'search': query, 'earliest_time': earliest_time, 'latest_time': latest_time, 'output_mode': 'json'}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
