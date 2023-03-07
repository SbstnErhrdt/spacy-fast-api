FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN pip install -U spacy-transformers

EXPOSE 80

COPY ./main.py /app