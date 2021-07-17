# Scripts

- `build_and_push.sh` - builds the Docker container

- `test_endpoint.py` - client script to test the endpoint. Use:

```bash
pip3 install -r requirements.txt
python3 test_endpoint.py -e <sagemaker-endpoint-name>
```

- `test_serialization.py` - script to compare various serialization protocols

```bash
python3 test_serialization.py
```

## Serialization comparison

Comparison of serialization protocols by amount of data sent "over the wire" from a client to the endpoint for a single calculation.

| Protocol | raw, bytes | base64(raw), bytes | lz4(raw), bytes | lz4(base64(raw)), bytes |
|:---|----:|---:|---:|---:|
|raw in-memory | 26016 | - | - | - |
|msgpack | 28607 | 38144 | 19841 | 26456 |
|json | 48474 | 64632 | 27969 | 37292 |
|pickle | 28644 | 38192 | 19867 | 26492 |
|arrow | 43008 | 57344 | 31508 | 42012 |
|bson | 40946 | 54596 | 25897 | 34532 |
|protobuf | 25393 | 33860 | 18244 | 24328 |
