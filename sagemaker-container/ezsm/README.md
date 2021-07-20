

```bash
docker build -f Dockerfile.test -t test-difflearning .
docker run -it --rm test-difflearning
```

In the container:

```bash
python test.py
```

```bash
docker pull tensorflow/tensorflow:latest-gpu
IMAGE_ID=$(docker images tensorflow/tensorflow:latest-gpu -q)

docker tag $IMAGE_ID $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/tensorflow/tensorflow:latest-gpu
$(aws ecr get-login --no-include-email --registry-ids $ACCOUNT_ID)
aws ecr describe-repositories --repository-names tensorflow/tensorflow || aws ecr create-repository --repository-name  tensorflow/tensorflow 
docker push $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/tensorflow/tensorflow:latest-gpu

```