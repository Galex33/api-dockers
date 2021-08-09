from pkg_diamond.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from pkg_diamond.pipeline import *
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump, load

class Model(Pipeline):
    def __init__(self, df, target, features="all"):
        super().__init__(df, target, features="all")
        
    def split(self, X, y, test_size):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, random_state=0)

    def model_pipeline(self, model, preprocessor):
        self.model = make_pipeline(preprocessor, model)
        return self.model
    
    def fit_model(self, X_train, y_train, model, preprocessor):
        self.model_pipeline(model, preprocessor)
        self.model = self.model.fit(X_train, y_train)
        
    def save_model(self):
        dump(self.model, '../api/fit_model.joblib')
    
