FROM python:latest

RUN adduser -D @rudghks531
USER @rudghks531

WORKDIR /@rudghks531/roa-backend:main/roa-backend/

COPY ./main.py /@rudghks531/roa-backend:main/roa-backend/
COPY ./requirements.txt /@rudghks531/roa-backend:main/roa-backend/

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

CMD uvicorn --host=0.0.0.0 --port 8000 main:app
