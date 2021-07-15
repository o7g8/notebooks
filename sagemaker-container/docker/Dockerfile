FROM tensorflow/tensorflow:latest

LABEL maintainer="Oleg Grytsynevych"

# Set a docker label to advertise multi-model support on the container
LABEL com.amazonaws.sagemaker.capabilities.multi-models=true
# Set a docker label to enable container to use SAGEMAKER_BIND_TO_PORT environment variable if present
LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true

# Install python and other runtime dependencies
RUN apt-get update && \
    apt-get -y install \
        build-essential \
        libatlas-base-dev  \
        git \
        wget \
        curl \
        openjdk-8-jdk-headless

# Python won’t try to write .pyc or .pyo files on the import of source modules
# Force stdin, stdout and stderr to be totally unbuffered. Good for logging
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install MMS, and SageMaker Inference Toolkit to set up MMS
RUN pip --no-cache-dir install multi-model-server \
                               sagemaker-inference \
                               retrying
                                
WORKDIR /

COPY code/multi_model_serving-1.0.0.tar.gz /multi_model_serving-1.0.0.tar.gz
RUN pip install /multi_model_serving-1.0.0.tar.gz && rm /multi_model_serving-1.0.0.tar.gz

COPY code/serve.py /serve.py
ENTRYPOINT ["python", "serve.py"]
