import numpy as np
import json
import blackscholes as bs
import inference as pr


def invokePredict(generator, nTest, size, simulSeed, isDiff: bool, testSeed=None):
    # simulation
    print("simulating training, valid and test sets")
    xTrain, yTrain, dydxTrain = generator.trainingSet(size, seed=simulSeed)
    xTest, xAxis, yTest, dydxTest, vegas = generator.testSet(num=nTest, seed=testSeed)
    print("done")
    inputJson = json.dumps({
        'xTest': xTest,
        'size': size,
        'isDiff': isDiff,
        'xTrain': xTrain,
        'yTrain': yTrain,
        'dydxTrain': dydxTrain
    })
    # (xTest, size, isDiff : bool, xTrain, yTrain, dydxTrain, weightSeed=None, deltidx=0)
    return pr.predict(xTest, size, isDiff, xTrain, yTrain, dydxTrain)

def test():
    # simulation set sizes to perform
    size = 1024 #[1024, 8192]
    # show delta?
    showDeltas = True
    # seed
    # simulSeed = 1234
    simulSeed = np.random.randint(0, 10000) 
    print("using seed %d" % simulSeed)
    weightSeed = None
    # number of test scenarios
    nTest = 100    
    # go
    generator = bs.BlackScholes()
    return invokePredict(generator, nTest, size, True, simulSeed)


print("testing...")
result = test()
print(result)
print("test done.")