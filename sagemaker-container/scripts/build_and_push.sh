#!/bin/bash

DOCKERFILE='Dockerfile'
ACCOUNT_ID=$1
REGION=$2
REPO_NAME=$3
IS_GPU=$4

cd ../package/ || exit 1
python setup.py sdist || exit 1
cp dist/multi_model_serving-1.0.0.tar.gz ../docker/code/ || exit 1

if [[ ${IS_GPU} == 'True' ]]; then
    DOCKERFILE='Dockerfile.gpu'
fi

echo "Building with ${DOCKERFILE}..."

docker build --no-cache -f ../docker/${DOCKERFILE} -t $REPO_NAME ../docker || exit 1

docker tag $REPO_NAME $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest

$(aws ecr get-login --no-include-email --registry-ids $ACCOUNT_ID)

aws ecr describe-repositories --repository-names $REPO_NAME || aws ecr create-repository --repository-name $REPO_NAME

docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:latest
