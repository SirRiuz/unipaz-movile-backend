# Libs
import requests
import hashlib
import json
from typing import Dict
from libs.storage import Storage
from bs4 import BeautifulSoup



class BaseClient:
    
    def __init__(self, credentials) -> None:
        self.credentials = credentials

class Cliet:

    def __init__(self, config:Dict):
        self.config = config

    def __get_request_hash(self) -> str:
        """ Get hash of the request """
        METHOD = self.config.get("method", "get")
        HEADERS = self.config.get("headers", {})
        CREDENTIALS = self.config.get("credentials", {})
        BODY = self.config.get("data", {})

        PAYLOAD = (METHOD + json.dumps(HEADERS) \
            + json.dumps(CREDENTIALS) \
                + json.dumps(BODY)).encode()
        return hashlib.sha256(PAYLOAD).hexdigest()

    def __request_data(self) -> requests.Response.text:
        """ Generate a custom request """
        REQUEST_HASH = self.__get_request_hash()
        storage = Storage()
        response = None
        
        if storage.get(REQUEST_HASH):
            return storage.get(REQUEST_HASH)

        response = requests.get(
            url=self.config.get("url"),
            headers=self.config.get("headers"),
            cookies=self.config.get("credentials"),
        )
        if self.config.get("method") == "post":
            response = requests.post(
                url=self.config.get("url"),
                headers=self.config.get("headers"),
                data=self.config.get("data"),
                cookies=self.config.get("credentials"),
                allow_redirects=self.config.get("redirect")
            )
        
        if response.status_code == 200:
            storage.set(REQUEST_HASH, response.text) 
            return response.text

    def get_html_object(self) -> BeautifulSoup:
        """ Get bf object of the response """
        response = self.__request_data()
        if response:
            return BeautifulSoup(response, "html.parser")

