#!/usr/bin/env bash

# Install virtualenv
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv

# Create virtual environment env
python3 -m venv env

activatePath=""

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     
        machine="Linux"
        activatePath="${PWD}/env/bin/activate"
        ;;
    Darwin*)    
        machine="Mac"
        activatePath="${PWD}/env/bin/activate"
    ;;
    MINGW*)     
        machine="Git Bash"
        activatePath="${PWD}/env/Scripts/activate"
    ;;
    *)          
        activatePath="${PWD}/env/bin/activate"
esac

# Activate virtual environment env
source ${activatePath}

# Automatically activate env
touch ~/.bash_profile && echo "source ${activatePath}" >> ~/.bash_profile