#!/usr/bin/python3
"""
Send request to URL from argv and display response body.
If status >= 400, print "Error code: <status>"
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
