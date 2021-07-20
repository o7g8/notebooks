FROM tensorflow/tensorflow:latest

RUN apt update && apt upgrade -y

RUN pip --no-cache-dir install -U pip
RUN pip --no-cache-dir install tensorflow numpy scipy

RUN mkdir /app
WORKDIR /app
COPY *.py /app/