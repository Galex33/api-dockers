import sys
sys.path.append('C:/Users/utilisateur/Desktop/simplon_ia/travaux/referentiels/package_ml/ml_mise_prod/diamond')
from pydantic import BaseModel, Field
from fastapi import FastAPI
from joblib import load
import pandas as pd
from fastapi.responses import FileResponse
from sklearn.tree import DecisionTreeRegressor

# data model of predictors
class DiamondController(BaseModel):
    cut: str = Field(..., example='Ideal')
    color: str = Field(..., example='J')
    clarity: str = Field(..., example='IF')
    carat: float = Field(..., example=0.6)
    depth: float = Field(..., example=61.0)
    table: float = Field(..., example=55.0)
    x: float = Field(..., example=3.56)
    y: float = Field(..., example=2.62)
    z: float = Field(..., example=3.98)



model = load('fit_model.joblib')
app = FastAPI()

@app.get("/accueil")
def read_index():
    return FileResponse("../app/views/index.html")


@app.post("/predict")
async def predict(payload: DiamondController):
     # convert the payload to pandas DataFrame
    input_df = pd.DataFrame([payload.dict()])
    prediction = model.predict(input_df)
    return {
    'Price': prediction
    }



# class Prediction:
#     def __init__(self):
#         #self.model = load('../api/fit_model.joblib')
#         self.model = load('/Users/marie/Ecole_IA/Brief_6_Mise_En_Prod/api-dockers/api/fit_model.joblib')
    
#     def prepro_input(api_input):
#         #TODO : read json input, convert each item to its format (int, float, string) 
#         # and then convert all to a DataFrame (return a dataframe input of next function)
#         pass

#     def predict_model(self, data):
#         # data = prepro_input(api_input)
#         self.prediction = self.model.predict(data)
#         # TODO : prepare prediction to json formet
#         return self.prediction
