# Spacy NLP API Wrapper

This is a simple fastAPI wrapper for [Spacy](https://spacy.io/).

## Environment

```
pip install -U spacy
pip install -U spacy-transformers
pip install -U fastapi
pip install -U "uvicorn[standard]"
```

## Docker

### Build

```bash
docker build -t spacy-nlp-api .
```

### Save
```bash
docker save spacy-nlp-api > spacy-nlp-api.tar
```

### Run

```bash
docker run -p 8000:8000 spacy-nlp-api
```
