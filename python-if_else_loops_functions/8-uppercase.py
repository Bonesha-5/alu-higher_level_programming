#!/usr/bin/python3
def uppercase(str):
    result = ""
    if ord(char) >= 97 and ord(char) <= 122:
        result += chr(ord(char) - 32)
    else:
        result += char
    print(result)
