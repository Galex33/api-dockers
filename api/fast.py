import sys
sys.path.append('/home/asabuzz/python_ml_dl/api-dockers/')
from pydantic import BaseModel, Field
from fastapi import FastAPI
from joblib import load
import pandas as pd
from fastapi.responses import FileResponse
import os

# data model of predictors
class DiamondController(BaseModel):
    carat: float = Field(..., example=0.6)
    cut: str = Field(..., example='Ideal')
    color: str = Field(..., example='J')
    clarity: str = Field(..., example='IF')
    depth: float = Field(..., example=61.0)
    table: float = Field(..., example=55.0)
    x: float = Field(..., example=3.56)
    y: float = Field(..., example=2.62)
    z: float = Field(..., example=3.98)

app = FastAPI()

def get_model():
    path = os.path.dirname(os.path.realpath(__file__))
    model = load(f'{path}/fit_model.joblib')
    return model

@app.get("/accueil")
def read_index():
    return FileResponse("../app/views/index.html")

@app.post("/predict")
async def predict(payload:DiamondController):
    # convert the payload to pandas DataFrame
    input_df = pd.DataFrame(payload.dict(), index=range(1))
    prediction = get_model().predict(input_df)[0]
    return {
        'prediction': prediction
    }

