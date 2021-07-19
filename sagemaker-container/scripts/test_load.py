import time
import json
from locust import User, task, between
import boto3
import test

# Don't create real methods on the class otherwise event registration will stop working
# see <https://stackoverflow.com/questions/62219054/locust-request-success-fire-does-not-do-anything> was a saviour here.
class SageMakerEndpointClient:

    def __init__(self, sm_endpoint, request_event):
        self._sm_endpoint = sm_endpoint
        self._request_event = request_event
        self._client = boto3.client('sagemaker-runtime')

    def __getattr__(self, name):

        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            request_meta = {
                "request_type": "smSigV4",
                "name": name,
                "response_length": 0,
                "response": None,
                "context": {},
                "exception": None,
            }
            try:
                request_meta["response"] = self._client.invoke_endpoint(*args, **kwargs)
                request_meta["response_length"] = len(request_meta["response"]['Body'].read().decode("utf-8"))
            except boto3.SageMakerRuntime.Client.exceptions.InternalFailure as e:
                request_meta["exception"] = e.Message
            except boto3.SageMakerRuntime.Client.exceptions.ServiceUnavailableException as e:
                request_meta["exception"] = e.Message
            except boto3.SageMakerRuntime.Client.exceptions.ValidationError as e:
                request_meta["exception"] = e.Message
            except boto3.SageMakerRuntime.Client.exceptions.ModelError as e:
                request_meta["exception"] = e.Message
            except Exception as e:
                request_meta["exception"] = "Other exception"
            request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
            self._request_event.fire(**request_meta)  # This is what makes the request actually get logged in Locust
            return request_meta["response"]

        return wrapper


class SageMakerEndpointUser(User):
    """
    A minimal Locust user class that provides an SageMakerEndpointClient to its subclasses
    """

    abstract = True  # don't instantiate this as an actual user when running Locust

    def __init__(self, environment):
        super().__init__(environment)
        self.client = SageMakerEndpointClient(self.host, request_event=environment.events.request)


# The real user class that will be instantiated and run by Locust
# This is the only thing that is actually specific to the service that we are testing.
class MyUser(SageMakerEndpointUser):
    endpointname = "multi-model-server-ep-2021-07-19-15-45-25"
    wait_time = between(1,5)

    @task
    def call_endpoint(self):
        (xTest, size, isDiff, xTrain, yTrain, dydxTrain) = test.test()
        inputJson = json.dumps({
            'xTest': xTest,
            'size': size,
            'isDiff': isDiff,
            'xTrain': xTrain,
            'yTrain': yTrain,
            'dydxTrain': dydxTrain
        })
        self.client.invoke_endpoint(
            EndpointName=self.endpointname, 
            ContentType='application/json',
            Accept='Accept',
            TargetModel='/model1.tar.gz',
            Body=inputJson)
