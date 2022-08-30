#!/usr/bin/env bash

runnable="docker"
containerName="python-ai-jupyter"
cmd="docker/run/miw_container.sh jupyter"

# No docker?
if (! command -v ${runnable} &> /dev/null) then
    echo "Try locally installed jupyter"
    runnable="jupyter-lab"

    if (! command -v ${runnable} &> /dev/null) then
        echo "${runnable} could not be found"
        exit -1
    else
        cmd="(cd notebooks; ${runnable})"
    fi
fi

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}

if [[ "${runnable}" == "docker" ]]; then
    sleep 5;
    docker logs ${containerName} 2> log.txt
    url=$(cat log.txt | grep -Eo 'http://127.0.0.1:8888/lab\?.*' | tail -n1)

    # Check if url is non-empty
    if [ "${url}" != "" ]; then
        rm log.txt
        printf "Open %s in your browser\n" "${url}"
        python3 -m webbrowser ${url}
    fi
fi
