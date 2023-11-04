# Libs
import http
import requests


def parse_cookies(http_response: requests.Request) -> dict:
    """Parse cookies of request"""
    cookie_grp = http.cookies.SimpleCookie()
    for h, v in http_response.headers.items():
        if "set-cookie" in h.lower():
            for cook in v.split(","):
                cookie_grp.load(cook)

    return {k: v.value for k, v in cookie_grp.items()}
