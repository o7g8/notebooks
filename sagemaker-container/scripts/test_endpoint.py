#!/usr/bin/python

from argparse import ArgumentParser
import boto3
import json
import test


parser = ArgumentParser()
parser.add_argument("-e", "--endpoint-name", dest="endpointname", required=True,
                    help="SageMaker endpoint name (not URL!)")
args = parser.parse_args()

(xTest, size, isDiff, xTrain, yTrain, dydxTrain) = test.test()
inputJson = json.dumps({
    'xTest': xTest,
    'size': size,
    'isDiff': isDiff,
    'xTrain': xTrain,
    'yTrain': yTrain,
    'dydxTrain': dydxTrain
})

client = boto3.client('sagemaker-runtime')
response = client.invoke_endpoint(
    EndpointName=args.endpointname, 
    ContentType='application/json',
    Accept='Accept',
    TargetModel='/model1.tar.gz',
    Body=inputJson
)
resultStr = response['Body'].read().decode("utf-8")
result = json.loads(resultStr)
print(result['prediction'])
print(result['diff'])
