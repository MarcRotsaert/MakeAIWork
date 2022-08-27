#!/usr/bin/env bash

dockerPath="/c/Program Files/Docker/Docker/Docker Desktop.exe"

# Make sure ~/.bashrc exists
touch ~/.bashrc 

# Add current path to .bashrc or show that this has been done already
cat ~/.bashrc | grep $PWD || echo "cd \"$PWD\"" >> ~/.bashrc

# Add path to Docker Desktop to .bashrc or show that this has been done already
cat ~/.bashrc | grep 'Docker Desktop' || echo "start /min \"${dockerPath}\"" >> ~/.bashrc
