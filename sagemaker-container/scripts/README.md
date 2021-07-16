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
