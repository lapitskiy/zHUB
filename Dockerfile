FROM --platform=$BUILDPLATFORM python:3.10 AS builder

EXPOSE 8002

ENV MICRO_SERVICE=/home/zHUB

RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static
RUN mkdir -p $MICRO_SERVICE/media

WORKDIR $MICRO_SERVICE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends && apt-get install -y software-properties-common

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales \

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

COPY ./requirements.txt $MICRO_SERVICE
RUN pip install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir
ADD . $MICRO_SERVICE