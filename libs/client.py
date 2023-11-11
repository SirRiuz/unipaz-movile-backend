

class BaseClient:
    
    def __init__(self, credentials=None, headers=None):
        self.credentials = credentials
        self.headers = headers
