#!/usr/bin/python3
"""
Fetch https://alu-intranet.hbtn.io/status and display:
    - type of response content
    - raw content
    - decoded UTF-8 content
"""

from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
