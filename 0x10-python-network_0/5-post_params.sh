#!/bin/bash
#script that takes in a URL, and displays the body of the response
curl -sXd POST "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
