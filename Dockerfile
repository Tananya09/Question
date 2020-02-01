FROM python:3.6-slim

WORKDIR /Question
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
