#!/bin/bash

function usage {
    echo "Usage():"
    echo "./run.sh [seq N | par N P]"
    exit 1
}

if [ $# -lt 2 ]; then
    usage
fi

if [ $1 == "par" ]; then
    if [ $# -lt 3 ]; then
        usage
    fi
    mpiexec -n $3 python main.py par $2
fi

if [ $1 == "seq" ]; then
    python main.py seq $2
fi

