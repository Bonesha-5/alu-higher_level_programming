#!/usr/bin/python3
"""
Send request to URL from argv and display the X-Request-Id header value.
"""

from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        header_value = response.getheader("X-Request-Id")
        print(header_value)
