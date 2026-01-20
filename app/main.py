from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Salary Prediction API")

# Load model once at startup
model = joblib.load("models/salary_model.pkl")

class SalaryRequest(BaseModel):
    age: float
    experience_year: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: SalaryRequest):
    X = pd.DataFrame([{
        "age": req.age,
        "experience_year": req.experience_year
    }])

    pred = model.predict(X)[0]
    return {"predicted_salary": float(pred)}