#!/bin/sh

ACCOUNT_ID=$1
REGION=$2
REPO_NAME=$3

cd ../package/ || exit 1
python setup.py sdist || exit 1
cp dist/multi_model_serving-1.0.0.tar.gz ../docker/code/ || exit 1

docker build -f ../docker/Dockerfile -t $REPO_NAME ../docker

docker tag $REPO_NAME $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest

$(aws ecr get-login --no-include-email --registry-ids $ACCOUNT_ID)

aws ecr describe-repositories --repository-names $REPO_NAME || aws ecr create-repository --repository-name $REPO_NAME

docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest
