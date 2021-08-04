import sys
import pandas as pd 

sys.path.append('C:/Users/utilisateur/Desktop/simplon_ia/travaux/referentiels/package_ml/ml_mise_prod/diamond')


class Data:
    """
    params : 
        df : panda DataFrame
        target : column name of DataFrame (string)
        features("all", ["col1", "col2"]). Default set at "all"
    attributes df, X, y
    returns None
    """
    def __init__(self, df, target, features="all"):
        self.df = df
        self.y = df[target]
        if features == "all":
            self.X = df.drop(target, axis=1)
        else:
            self.X = pd.Datafram(df[features])


        
#    methode : supprimer les outliers et les cols avec trop de data manquantes, plus type 