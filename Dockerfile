FROM python:3.10-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . .

