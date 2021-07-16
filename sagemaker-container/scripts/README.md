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

| Protocol | raw, bytes | base64, bytes |
|:---|----:|---:|
|msgpack| 28607| 38144|
|lz4(msgpack)| 19651| 26204|
|json| 48263| 64352|
|lz4(json)| 27810| 37080|
|pickle| 28644| 38192|
|lz4(pickle)| 19683| 26244|
|arrow| 43008| 57344|
|lz4(arrow)| 31327| 41772|
|bson| 40946| 54596|
|lz4(bson)| 25759| 34348|
|protobuf| 25393| 33860|
|lz4(protobuf)| 18050| 24068|
