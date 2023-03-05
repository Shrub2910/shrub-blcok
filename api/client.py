import requests
from .models import *

url = 'https://api.hypixel.net'

class SkyBlockApiClient:

    def __init__(self, token):
        
        self.token = token
        self.key = None

        if self._validate_api_key():
            print("Authorisation Success!")
        else:
            raise Exception("Invalid API key")

    
    def _validate_api_key(self):
        
        response = requests.get(f"{url}/key", headers={'API-Key':self.token})

        if response.status_code == 200:
            data = response.json()
            self.key = Key(data)
            return True

        return False
