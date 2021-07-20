

```bash
docker build -f Dockerfile.test -t test-difflearning .
docker run -it --rm test-difflearning
```

In the container:

```bash
python test.py
```