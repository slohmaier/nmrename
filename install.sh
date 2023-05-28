#!/bin/sh

if [ -e "/usr/local/bin" ]; then
    CWD="$(pwd)"
    NMRENAME="$CWD/nmrename.py"
    ln -s "$NMRENAME" /usr/local/bin/nmrename || exit 1
    echo "Successfully installed nmrename to /usr/local/bin"
else
    echo "ERROR! /usr/local/bin not found!"
    exit -1
fi