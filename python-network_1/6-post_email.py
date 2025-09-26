#!/usr/bin/python3
"""
Send POST request to URL from argv[1] with email argv[2] as parameter.
Display response body.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={"email": email})
    print(r.text)
