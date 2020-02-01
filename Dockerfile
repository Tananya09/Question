FROM python:3.6-slim
RUN apt-get update && \
    apt-get install -y g++ && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /Question
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
