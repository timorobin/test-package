# base image is 3.9 python
FROM python:3.9-buster

# Install poetry and update path
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "${PATH}:/root/.local/bin"

WORKDIR /test-package

COPY . .

RUN poetry install --without dev

ENTRYPOINT poetry run python scripts/call_sub_1.py

