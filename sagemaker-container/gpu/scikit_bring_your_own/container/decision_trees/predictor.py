# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

import os
import flask
import inference

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

# A singleton for holding the model. This simply loads the model and holds it.
# It has a predict function that does a prediction based on the model and the input data.

class PredictionService(object):

    def predict(self, data):
        """For the input, do the predictions and return them.

        Args:
            input: The data on which to do the predictions."""
        input = json.loads(data)
        (pred, diff) = inference.predict(input)
        result = json.dumps({
                'prediction': pred.tolist(),
                'diff': diff.tolist(),
        })
        mimetype = 'application/json'
        return (result, mimetype)

# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy."""
    status = 200 # always healthy
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    """Do an inference on a single batch of data."""
    service = PredictionService()
    
    try
        data = flask.request.data.decode('utf-8')
        (result, mimetype) = service.predict(data)
        return flask.Response(response=result, status=200, mimetype=mimetype)
    except Exception as e:
        resp = json.dumps({'error':str(e)})
        return flask.Response(response=resp, status=500, mimetype='application/json')
