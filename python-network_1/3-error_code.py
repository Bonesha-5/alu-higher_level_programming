#!/usr/bin/python3
"""
Send request to URL from argv and display body.
If HTTPError occurs, display "Error code: <code>".
"""

from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
