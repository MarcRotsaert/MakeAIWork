#!/usr/bin/env bash

# # Activate virtual environment env
# source env/bin/activate

# CONDA

# Install Miniconda
function installConda {
  if (machine=="Mac") then
    echo "Install Miniconda for %s" "${machine}"

    arch=$(uname -m)
    printf "Detected architecture %s\n" "${arch}"

    if (arch=="aarch64") then
      # Support Apple M* processors
      condaInstaller="install/conda/Miniconda3-latest-MacOSX-arm64.sh"
    else
      condaInstaller="install/conda/Miniconda3-latest-MacOSX-x86_64.sh"  
    fi

    eval "${condaInstaller}" && ( zsh || bash)

  fi
}

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     machine="Linux";;
    Darwin*)    
      machine="Mac"
      brew update && brew install freeglut
      export LIBGL_ALLOW_SOFTWARE=1
      ;;
    CYGWIN*)    machine="Cygwin";;
    MINGW*)     machine="Git Bash";;
    *)          machine="UNKNOWN:${os}"
esac

function install_with_conda {
  if (! command -v "conda" &> /dev/null ) then
    installConda
  fi

  conda install --yes -c conda-forge \
    beautifulsoup4 \
    py-cpuinfo \
    freeglut3 \
    jupyter_core \
    jupyterlab \
    keras \
    Keras-Preprocessing \
    lidar \
    pandas \
    Pillow \
    pyopengl \
    scikit-image \
    scikit-learn \
    selenium \
    tensorflow \
    tensorboard-plugin-wit \
    tensorflow-estimator 
    
}

# Install all required libraries t
function install_with_pip {
  # Upgrade pip
  python3 -m pip install --upgrade pip

  # Install setuptools
  python3 -m pip install setuptools
  python3 -m pip install --no-cache-dir -r install/pip/requirements.txt

}

# install_with_conda
install_with_pip 