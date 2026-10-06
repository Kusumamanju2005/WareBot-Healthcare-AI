import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
DATA_PATH = BASE_DIR / "data" / "aiml_labelled_samples.json"


app = FastAPI(
    title="WareBot Healthcare AI",
    description="Healthcare text intent classification API",
    version="1.0.0",
)


vectorizer = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")
model = joblib.load(MODEL_DIR / "baseline_classifier.pkl")


class PredictionRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    text: str
    intent: str


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "WareBot Healthcare AI",
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    text = request.text.strip()

    if not text:
        return {
            "text": request.text,
            "intent": "general_query",
        }

    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]

    return {
        "text": text,
        "intent": prediction,
    }