#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo $SCRIPT_DIR
docker rm $(docker stop $(docker ps -a -q --filter ancestor=autn-mothership --format="{{.ID}}"))

docker build --tag autn-mothership "$SCRIPT_DIR"
docker run -p 5050:5050 autn-mothership 
