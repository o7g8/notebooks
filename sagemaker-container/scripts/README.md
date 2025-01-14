# Scripts

## Build the Docker container

- `build_and_push.sh` - builds the Docker container

## End-to-end test of the SageMaker endpoint

- `test_endpoint.py` - client script to test the endpoint. Use:

```bash
pip3 install -r requirements.txt
python3 test_endpoint.py -e <sagemaker-endpoint-name>
```

## Comparison of serialization protocols

- `test_serialization.py` - script to compare various serialization protocols

```bash
pip3 install -r requirements.txt
protoc --python_out=. args.proto
python3 test_serialization.py
```

Comparison of serialization protocols by amount of data sent "over the wire" from a client to the endpoint for a single calculation.

| Protocol | raw, bytes | lz4(raw), bytes | base64(raw), bytes | base64(lz4(raw)), bytes |
|:---|----:|---:|---:|---:|
|raw in-memory | 26016 | - | - | - |
|msgpack | 28607 | 19494 | 38144 | 25992 |
|json | 47974 | 27598 | 63968 | 36800 |
|pickle | 28644 | 19521 | 38192 | 26028 |
|arrow | 43008 | 31232 | 57344 | 41644 |
|bson | 40946 | 25621 | 54596 | 34164 |
|protobuf | 25393 | 17960 | 33860 | 23948 |

## Performance testing

We use Locust <http://locust.io> to test performance of the endpoint.
To minimize influence fo the network latency consider to run the test on an EC2/Cloud9 instance
"close" to the endpoint itself.
Set the `endpointname` to the SM Endpoint name in `test_load.py`

```bash
pip3 install -r requirements.txt
locust -f test_load.py
```

Open `http://0.0.0.0:8089` in your browser and enter a number of clients and their request rate. You can ignore the endpoint field there.

## References

- Testing of other (non-HTTP) systems with Locust <https://docs.locust.io/en/stable/testing-other-systems.html>
