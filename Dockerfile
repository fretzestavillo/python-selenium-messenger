FROM python:3.10.6-alpine

WORKDIR /messenger

COPY requirements.txt .

COPY . .


RUN pip install -r requirements.txt

CMD  ["python3","test.py"]
