import requests
from .models import *

url = 'https://api.hypixel.net'

class HypixelApiClient:

    def __init__(self, token):
        
        self.token = token
        self.key = None

        self._validate_api_key()

    
    def _validate_api_key(self):
        
        response = requests.get(f"{url}/key", headers={'API-Key':self.token})

        if self._is_response_success(response):
            print("Validation Success")
            data = response.json()
            self.key = Key(data)

    
    def _is_response_success(self, response):
        if response.status_code == 200:
            return True
        elif response.status_code == 400:
            raise Warning("Missing one or more fields")
        elif response.status_code == 403:
            raise ValueError("Invalid API key")
        elif response.status_code == 422:
            raise Warning("Malformed UUID")
        elif response.status_code == 429:
            raise Warning("Key throttle")
        
        return False
