import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class AnalyzeRequest(BaseModel):
    food: str
    weight: str
    goal: str
    allergies: str

GROQ_API_KEY = "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"

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    prompt = f"""
    Role: Nutrition AI Assistant
    Food: {req.food}
    Weight: {req.weight}
    Goal: {req.goal}
    Allergies: {req.allergies}

    Return ONLY a valid JSON object with these keys:
    "calories": "Total estimate",
    "protein": "Grams estimate",
    "meals": ["List of 3 meal suggestions"],
    "recipe": "One simple healthy recipe",
    "tip": "One health tip"
    """

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()
        result = res.json()
        content = result["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Analysis failed: {str(e)}")