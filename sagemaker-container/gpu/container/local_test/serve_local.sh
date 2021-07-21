#!/bin/sh

image=$1

docker run -p 8081:8080 --rm ${image} serve
