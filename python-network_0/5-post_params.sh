#!/bin/bash
# Send POST with email and subject
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
