# Libs
import requests
from settings import *
from helpers.auth import parse_cookies


class Auth:

    def __init__(self, user:str, password:str):
        self.user = user
        self.password = password

    def login(self) -> dict:
        return self.__auth_request()
    
    def __auth_request(self) -> dict:
        """ Get credentias of the student """
        jar = requests.cookies.RequestsCookieJar()
        response = requests.post(
            url=URLS["AUTH"],
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=self.__get_body_request(),
            cookies=jar,
            allow_redirects=False
        )
        cookies = parse_cookies(response)
        if response.status_code == 500:
            raise Exception("Backend error ...")

        return cookies if cookies else None

    def __get_body_request(self) -> str:
        """ Get body params of the request """
        payload = PAYLOAD_REQUEST.replace('USER_NAME', self.user)
        payload = payload.replace('PASSWORD', self.password)
        return payload
