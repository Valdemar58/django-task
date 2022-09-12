# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /djtask
COPY requirements.txt /djtask/
RUN pip install -r requirements.txt
COPY . /djtask/