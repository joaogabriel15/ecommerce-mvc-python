# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install -r /app/requirements.txt



