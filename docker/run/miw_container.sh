#!/usr/bin/env bash

argumentNames=("mode" "[script]")
argumentValues=("$@")
nrOfArguments=${#argumentValues[@]}

#  Image

repo="jaboo"
name="${repo}/miw"
version="0.9"
image="${name}:${version}"

if [ $nrOfArguments -lt 1 ]; then
    printf "USAGE: %s %s\n" "$0" "${argumentNames[*]}"
    exit 1;
fi

# Host

hostdirHome="${PWD}"
hostdirNotebooks="${hostdirHome}/notebooks"
hostdirPics="${hostdirHome}/pics"
hostdirProjects="${hostdirHome}/projects"
hostdirScripts="${hostdirHome}/scripts"

function makeWindowsProof {
    hostdirNotebooks=$(cygpath -w -p ${hostdirNotebooks})
    hostdirProjects=$(cygpath -w -p ${hostdirProjects})
    hostdirPics=$(cygpath -w -p ${hostdirPics})
    hostdirScripts=$(cygpath -w -p ${hostdirScripts})
    dockerPrefix="winpty "
    # hostIP=$( ipconfig | grep IPv4 | sed 's/.*://' | tail -n1 | xargs)
    export DISPLAY="${hostIP}:0"
    # export DISPLAY="host.docker.internal:0.0"
}

function makeMacProof {
    # Support Apple M* processors
    arch=$(uname -m)
    printf "Use architecture %s\n" "${arch}"
    dockerPostfix=" --platform linux/${arch}"

    # Set global variable DISPLAY to enable X Window System
    hostIP=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
    export DISPLAY="${hostIP}:0"
    export LIBGL_ALLOW_SOFTWARE=1
}

dockerPrefix=""
dockerPostfix=""

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     machine="Linux";;
    Darwin*)    machine="Mac" && makeMacProof;;
    CYGWIN*)    machine="Cygwin" && makeWindowsProof;;
    MINGW*)     machine="Git Bash" && makeWindowsProof;;
    *)          machine="UNKNOWN:${os}"
esac

printf "hostIP : [%s]\n" "${hostIP}"
printf "dockerPostfix : [%s]\n" "${dockerPostfix}"

export HOSTPATH_NOTEBOOKS=${hostdirNotebooks}
export HOSTPATH_PICS=${hostdirPics}
export HOSTPATH_PROJECT=${hostdirProjects}
export HOSTPATH_SCRIPTS=${hostdirScripts}

# Container

mode="${argumentValues[0]}"

containerName="python-ai-${mode}"
containerHome="/home/student"
containerdirNotebooks="${containerHome}/notebooks"
containerdirProjects="${containerHome}/projects"
containerdirPics="${containerHome}/pics"
containerdirScripts="${containerHome}/scripts"
composePath="docker/compose"
graphicsParams="-v \"/tmp/.X11-unix:/tmp/.X11-unix:ro\" -e \"DISPLAY=${DISPLAY}\" --net=host"
graphicsParams="-e \"DISPLAY=${DISPLAY}\" --net=host"

cmd="${dockerPrefix}docker run -it --rm --name ${containerName}"
cmd="${cmd} -v \"${hostdirNotebooks}:${containerdirNotebooks}\""
cmd="${cmd} -v \"${hostdirPics}:${containerdirPics}\""
cmd="${cmd} -v \"${hostdirProjects}:${containerdirProjects}\""
cmd="${cmd} -v \"${hostdirScripts}:${containerdirScripts}\""

case "${mode}" in
    bash*)
        entryPoint="bash"
        cmd="${cmd}${dockerPostfix} --entrypoint ${entryPoint} ${image}";;
    jupyter*)
        composefile="${composePath}/python-ai-jupyter.yaml"
        version="0.1"
        image="${repo}/miw-notebook:${version}"
        export IMAGE=${image}
        export CONTAINER_NAME=${containerName}
        cmd="docker/compose/up.sh ${composefile}";;
    python-repl*)
        entryPoint="ptipython"
        cmd="${cmd} --entrypoint ${entryPoint} ${image}";;
    python-script*)
        entryPoint="run_script"
        cmd="${cmd} ${graphicsParams}"
        cmd="${cmd} -e SCRIPT=\"${argumentValues[1]}\" --entrypoint ${entryPoint} ${image}";;
    # Default
    *)
        cmd="${cmd} ${image}";;
esac

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}
