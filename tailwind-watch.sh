#!/bin/bash

DIR=$(cd `dirname $0` &&PWD)

echo $DIR

docker run --rm -t --init --interactive --volume "$DIR":/root --workdir /root node npx tailwindcss -i ./app/src/style.css -o ./app/static/style.css --watch