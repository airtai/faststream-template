#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <username> <repo-name>"
    exit 1
fi

username="$1"

reponame="$2"

docker build -t ghcr.io/$username/$reponame:latest .
