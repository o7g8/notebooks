# Predictor for differential learning

The entry point is `predictor.predict()`.

The test entry point is `test.test()`.

Create container:

```bash
docker build -t test-difflearning .
```

Run the container:

```bash
docker run -it --rm test-difflearning
```

Run the test in the container:

```bash
python test.py 
```
