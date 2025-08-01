#!/usr/bin/python3
"""
Fetch https://alu-intranet.hbtn.io/status with requests
Display the response body info.
"""

import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
