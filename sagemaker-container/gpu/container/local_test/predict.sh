#!/bin/bash

payload=$1
content=${2:-application/json}

curl --data-binary @${payload} -H "Content-Type: ${content}" -v http://localhost:8081/invocations
