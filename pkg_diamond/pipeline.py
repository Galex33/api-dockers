from pkg_diamond.preprocessing import Data
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import *


class Pipeline(Data):
    def __init__(self, df, target, features="all"):
        super().__init__(df, target, features="all")

    def list_features(self):
        self.categorical_ordinal_features = list(self.X.select_dtypes(include=['category']).columns)
        self.numerical_features = list(self.X.select_dtypes(exclude=['category']).columns)

    def features_pipeline(self, strategy_num, strategy_cat_ordi, scaler, encoder, cat_ordi):
        self.numerical_pipeline = make_pipeline(SimpleImputer(strategy=strategy_num), scaler())
        self.categorical_ordinal_pipeline = make_pipeline(SimpleImputer(strategy=strategy_cat_ordi), encoder(categories =cat_ordi, handle_unknown='use_encoded_value', unknown_value= -1))

    def prepro(self, strategy_num, strategy_cat_ordi, scaler, encoder, cat_ordi):
        self.list_features()
        self.features_pipeline(strategy_num, strategy_cat_ordi, scaler, encoder, cat_ordi)
        
        self.preprocessor = make_column_transformer(
            (self.numerical_pipeline, self.numerical_features),
            (self.categorical_ordinal_pipeline, self.categorical_ordinal_features))
    