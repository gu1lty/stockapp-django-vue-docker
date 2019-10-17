FROM python:3.7-alpine
MAINTAINER Rax Otero

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./backend /backend

RUN adduser -D appuser
USER appuser