FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /task

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

EXPOSE 8000

COPY . .
