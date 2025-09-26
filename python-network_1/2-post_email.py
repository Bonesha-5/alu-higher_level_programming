#!/usr/bin/python3
"""
Send POST request to URL with email parameter from argv[2]
Display response body decoded in utf-8.
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    req = Request(url, data=data)
    with urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
