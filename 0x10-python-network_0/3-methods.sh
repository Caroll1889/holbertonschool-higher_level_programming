#!/bin/bash
#script that takes in a URL, and displays the body of the response
curl -sILX "$1" | grep "Allow:" | cut -d ' ' -f2 --complement
