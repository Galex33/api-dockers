import sys
sys.path.append('C:/Users/utilisateur/Desktop/simplon_ia/travaux/referentiels/package_ml/ml_mise_prod/diamond')
from fastapi import FastAPI
from joblib import load

app = FastAPI()
@app.get("/")
async def root():
    model = load('fit_model.joblib')
    return {"message": model}

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
