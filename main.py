import os
from typing import List
import time
from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
import spacy
import uvicorn

# init api
from pydantic import BaseModel

app = FastAPI(
    title=os.getenv("APP_TITLE", "Spacy App"),
    description=os.getenv("APP_DESCRIPTION", "Spacy App"),
    version=os.getenv("APP_VERSION", "0.0.0"),
)

# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# load model
nlp = spacy.load('./model')


class TextRequest(BaseModel):
    text: str


class NerElement(BaseModel):
    text: str
    start: int
    end: int
    label: str


def predict(text: str):
    res = []
    doc = nlp(text, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
    for ent in doc.ents:
        res.append({
            "text": ent.text,
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_,
        })
    return res


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.put("/", response_model=List[NerElement])
async def handle_request(
        payload: TextRequest,
):
    res = predict(payload.text)
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
