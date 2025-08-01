#!/usr/bin/python3
"""
Display GitHub user id by authenticating with username and token (password).
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, token))
    try:
        print(r.json().get("id"))
    except Exception:
        print("None")
