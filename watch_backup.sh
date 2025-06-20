#!/bin/bash

WATCH_DIR="/mnt/c/Users/Username/Documents" 

inotifywait -m -r -e modify,create,delete,move "$WATCH_DIR" |
while read path action file; do
    echo "Detected $action on $file at $path"
    ./backup.sh
done
