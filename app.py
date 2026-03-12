from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("30-house_price_model_complete.pkl", "rb") as f:
    saved_data = pickle.load(f)
    model = saved_data["model"]
    scaler = saved_data["scaler"]

class HouseFeatures(BaseModel):
    OverallQual: int
    GrLivArea: int
    GarageCars: int
    TotalBsmtSF: int
    FullBath: int
    BedroomAbvGr: int
    LotArea: int
    AgeOfBuilt: int

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(features : HouseFeatures):
    input_data = pd.DataFrame([features.model_dump()])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return{"prediction": prediction[0]}