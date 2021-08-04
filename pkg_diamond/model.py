from pkg_diamond.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from pkg_diamond.pipeline import *
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump, load

class Model(Pipeline):
    def __init__(self, df, target, features="all"):
        super().__init__(df, target, features="all")
    
    def fit_model(self, model):
        # on entraine le modèle
        self.model = model.fit(self.X, self.y)
        # on fait les 
    def save_model(self):
        dump(self.model, '../api/fit_model.joblib')
    
    def load_model(self):
        self.model = load('../api/fit_model.joblib')

    def predict_model(self, data):
        # transformer les data en df 
        self.prediction = self.model.predict(data)

    
# save model

# load model
