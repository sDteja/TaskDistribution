FROM python:3.8
RUN apt-get update
RUN mkdir /code
WORKDIR /code
COPY app.py /code/app.py
COPY worker.py /code/worker.py
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

