FROM python:3.7-alpine

WORKDIR /code

RUN apk add --no-cache alpine-sdk libffi-dev libressl-dev

RUN pip install --upgrade pip && pip --no-cache-dir install poetry

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false && poetry install

COPY . .

EXPOSE 8000

CMD ["gunicorn", "app:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
