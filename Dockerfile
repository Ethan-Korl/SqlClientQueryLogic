# simple docker file to build the sqlbin

FROM python:3.11.4-slim-buster

LABEL version="testing 1.0"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 9000

CMD [ "fastapi", "dev", "src/http_client/main.py" ]

