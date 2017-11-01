FROM python:3

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN mkdir /conf
RUN mkdir /app
RUN mkdir /data

WORKDIR /app

COPY backend/Pipfile /app
COPY backend/Pipfile.lock /app

RUN pipenv install

COPY infrastructure/api/gunicorn.conf /conf

COPY backend /app

EXPOSE 9000
CMD [ \
  "pipenv", \
  "run", \
  "gunicorn", \
  "--config", "/conf/gunicorn.conf", \
  "conduit.wsgi" \
]
