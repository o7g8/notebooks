import random
import blackscholes as bs

def flatten(x):
    return x[:, 0].tolist()

def invokeCreateArgs(generator, nTest, size, simulSeed, isDiff: bool, testSeed=None):
    # simulation
    print("simulating training, valid and test sets")
    xTrain, yTrain, dydxTrain = generator.trainingSet(size, seed=simulSeed)
    xTest, xAxis, yTest, dydxTest, vegas = generator.testSet(num=nTest, seed=testSeed)
    print("done")
    # (xTest, size, isDiff : bool, xTrain, yTrain, dydxTrain, weightSeed=None, deltidx=0)
    return (flatten(xTest), size, isDiff, flatten(xTrain), flatten(yTrain), flatten(dydxTrain))

def test():
    # simulation set sizes to perform
    size = 1024 #[1024, 8192]
    # show delta?
    showDeltas = True
    # seed
    # simulSeed = 1234
    simulSeed = random.randint(0, 10000) 
    print("using seed %d" % simulSeed)
    weightSeed = None
    # number of test scenarios
    nTest = 100    
    # go
    generator = bs.BlackScholes()
    return invokeCreateArgs(generator, nTest, size, True, simulSeed)
