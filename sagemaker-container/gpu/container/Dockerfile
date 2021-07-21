# Build an image that can do training and inference in SageMaker
# This is a Python 2 image that uses the nginx, gunicorn, flask stack
# for serving inferences in a stable way.

FROM tensorflow/tensorflow:latest-gpu

# Install python and other runtime dependencies
RUN apt-get update && \
    apt-get -y install \
        apt-utils \
        build-essential \
        libatlas-base-dev  \
        git \
        wget \
        curl \
        nginx \
        ca-certificates
RUN apt-get clean
    

# Here we get all python packages.
RUN pip --no-cache-dir install -U pip
RUN pip --no-cache-dir install flask gevent gunicorn tensorflow numpy scipy

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
RUN mkdir -p /opt/program
COPY decision_trees /opt/program
WORKDIR /opt/program

