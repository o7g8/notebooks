import ezsmdeploy
ezonsm = ezsmdeploy.Deploy(model = None,
    script = 'inference.py',
    requirements = ['numpy','scipy','tensorflow'],
    name = 'diffdl-container-gpu2',
    wait = True,
    image = '785577973223.dkr.ecr.us-east-1.amazonaws.com/tensorflow/tensorflow:latest-gpu',
    instance_type = 'ml.g4dn.xlarge',
    monitor = False) # turn on model monitoring
