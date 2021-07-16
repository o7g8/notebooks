#!/usr/bin/python

from argparse import ArgumentParser
import boto3
import json

parser = ArgumentParser()
parser.add_argument("-e", "--endpoint-name", dest="endpointname", required=True,
                    help="SageMaker endpoint name (not URL!)")
args = parser.parse_args()

p = [1,2,3]
client = boto3.client('sagemaker-runtime')
response = client.invoke_endpoint(
    EndpointName=args.endpointname, 
    ContentType='application/json',
    Accept='Accept',
    TargetModel='/model1.tar.gz',
    Body=json.dumps({'input': p})
)
resultStr = response['Body'].read().decode("utf-8")
result = json.loads(resultStr)
print(result['prediction'])
print(result['diff'])
