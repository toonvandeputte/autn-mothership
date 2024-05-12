#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo $SCRIPT_DIR
docker rm $(docker stop $(docker ps -a -q --filter ancestor=autn-mothership --format="{{.ID}}"))

docker build --tag autn-mothership "$SCRIPT_DIR"
docker run -v "$SCRIPT_DIR/data":/python-docker/data -v "$SCRIPT_DIR/app/static":/python-docker/app/static -v "$SCRIPT_DIR/app/templates":/python-docker/app/templates -p 5050:5050 autn-mothership 
