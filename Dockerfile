FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN useradd appuser && chown -R appuser /app
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get -y install libglib2.0-0
RUN apt -y install tesseract-ocr
RUN apt-get -y install tesseract-ocr-script-hang tesseract-ocr-script-hang-vert

USER appuser

ENTRYPOINT ["uvicorn","main:app","--port","8000","--host","0.0.0.0"]