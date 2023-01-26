FROM python:3.10

WORKDIR /neural-api

COPY requirements.txt .
COPY ./src ./src

RUN pip3 install -r requirements.txt

CMD ["python", "./src/main.py"]