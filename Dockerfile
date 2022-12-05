FROM python:latest

USER rudghks531

WORKDIR /diablo2img2option_backend/

COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

CMD uvicorn --host=0.0.0.0 --port 8000 main:app
