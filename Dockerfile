FROM python:3.7.9-alpine

WORKDIR /usr/src/app
RUN mkdir /usr/src/app/staticfiles

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache g++ linux-headers musl-dev
RUN apk add --no-cache \
            curl \
            git \
            jpeg-dev \
            libffi-dev \
            libxml2-dev \
            libxslt-dev \
            postgresql-dev \
            zlib-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2==2.8.5
RUN pip install gunicorn==20.0.4

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
