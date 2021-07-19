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
