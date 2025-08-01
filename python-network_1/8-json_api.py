#!/usr/bin/python3
"""
Send POST request to http://0.0.0.0:5000/search_user with letter from argv as q parameter.
If no arg given, q is empty string.
If valid JSON and not empty, display [<id>] <name>.
Otherwise display error messages.
"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post(url, data={"q": q})
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
