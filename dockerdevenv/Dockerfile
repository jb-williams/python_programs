FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src ./scr

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]