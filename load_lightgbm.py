import joblib
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
import xgboost
import matplotlib.pyplot as plt
from category_encoders import OrdinalEncoder
from lightgbm import LGBMRegressor
import joblib
from project_sc import X_test, X_test_encoded, encoder



file_path = "C:/Users/aryij/Documents/AI Bootcamp/Section 3/project3/pickle/lgbm_model.pkl"

lgbm_from_pickle = joblib.load(file_path)


def july_pred(city, date, transfer="Y"):
    df = pd.DataFrame({"departure_1" : [city],
                        "dep_date" : [date],
                        "transfer" : [transfer]})
    df_enc = encoder.transform(df)
    pred = lgbm_from_pickle.predict(df_enc)
    return pred

print(july_pred("PAR", "2022-07-21"))

