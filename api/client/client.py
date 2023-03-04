import requests

class SkyBlockApiClient:

    def __init__(self, api_key) -> None:
        
        self.api_key = api_key

    
    def _validate_api_key(self):
        requests.get("")
