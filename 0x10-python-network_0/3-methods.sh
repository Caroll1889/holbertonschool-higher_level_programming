#!/bin/bash
#script that takes in a URL, and displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d ' ' -f1 --complement
