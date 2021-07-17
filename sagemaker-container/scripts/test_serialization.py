import test
import sys
import json
import msgpack
import lz4.frame
import base64
import pyarrow as pa
import pickle
import bson
import args_pb2 as pb

# Compile protobuf
# protoc --python_out=. args.proto 

def printSize(prefix, blob):
    print(prefix + ': ' + str(len(blob)) + ' ' + str(len(base64.b64encode(blob))))

def l(x):
    return len(x)
def lb64(x):
    return l(base64.b64encode(x))

def lf(x):
    return sys.getsizeof(x)

def reportSize(prefix, blob):
    p = lz4.frame.compress(blob, lz4.frame.COMPRESSIONLEVEL_MAX)
    print(f"|{prefix} | {l(blob)} | {l(p)} | {lb64(blob)} | {lb64(p)} |")

(xTest, size, isDiff, xTrain, yTrain, dydxTrain) = test.test()
mydict = {
    'xTest': xTest,
    'size': size,
    'isDiff': isDiff,
    'xTrain': xTrain,
    'yTrain': yTrain,
    'dydxTrain': dydxTrain
}

print(f"Raw in-memory 'xTest': {lf(xTest)}; 'size': {lf(size)}, 'isDiff': {lf(isDiff)}, 'xTrain': {lf(xTrain)}, 'yTrain': {lf(yTrain)}, 'dydxTrain': {lf(dydxTrain)}\n")
print("| Protocol | raw, bytes | lz4(raw), bytes | base64(raw), bytes | base64(lz4(raw)), bytes |")
print("|:---|----:|---:|---:|---:|")
print('|raw in-memory | ' + str(
    sys.getsizeof(mydict)
    + sys.getsizeof(xTest)
    + sys.getsizeof(size)
    + sys.getsizeof(isDiff)
    + sys.getsizeof(xTrain)
    + sys.getsizeof(yTrain)
    + sys.getsizeof(dydxTrain)
    ) + ' | - | - | - |')
msgPacked  = msgpack.packb(mydict)
reportSize('msgpack', msgPacked)

inputJson = json.dumps(mydict)
reportSize('json', inputJson.encode("utf-8"))

pick = pickle.dumps(mydict)
reportSize('pickle', pick)

arrow = pa.serialize(mydict).to_buffer()
reportSize('arrow', arrow)

bb = bson.dumps(mydict)
reportSize('bson', bb)

x = pb.InputParams()
x.xTest.extend(xTest)
x.size = size
x.isDiff = isDiff
x.xTrain.extend(xTrain)
x.yTrain.extend(yTrain)
x.dydxTrain.extend(dydxTrain)
xx = x.SerializeToString()
reportSize('protobuf', xx)