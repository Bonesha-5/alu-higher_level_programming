#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit))
    return last_digit
