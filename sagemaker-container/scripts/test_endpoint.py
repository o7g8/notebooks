#!/usr/bin/python

from argparse import ArgumentParser
import numpy as np
import boto3
import json
import test

# list -> transposed (columnar) np array
def list2arrt(l):
    x = np.array(l)[:, np.newaxis]
    return x.transpose().T

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
#print(list2arrt(result['prediction']))