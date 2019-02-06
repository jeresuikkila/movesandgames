FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /movesandgames
ADD . /movesandgames

RUN pip3 install -r requirements.txt