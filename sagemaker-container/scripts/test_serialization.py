import test
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

def reportSize(prefix, blob):
    printSize(prefix, blob)
    lz4Packed = lz4.frame.compress(blob, lz4.frame.COMPRESSIONLEVEL_MAX)
    printSize('lz4('+prefix+')', lz4Packed)

(xTest, size, isDiff, xTrain, yTrain, dydxTrain) = test.test()
mydict = {
    'xTest': xTest,
    'size': size,
    'isDiff': isDiff,
    'xTrain': xTrain,
    'yTrain': yTrain,
    'dydxTrain': dydxTrain
}
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