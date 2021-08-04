import sys
sys.path.append('C:/Users/utilisateur/Desktop/simplon_ia/travaux/referentiels/package_ml/ml_mise_prod/diamond')
from fastapi import FastAPI     
from joblib import load


app = FastAPI()
@app.get("/")
async def root():
    model = load('fit_model.joblib')

    return {"message": model}