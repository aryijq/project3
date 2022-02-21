import numpy as np
import pandas as pd
from xgboost import XGBRegressor
import xgboost
import matplotlib.pyplot as plt
from category_encoders import OrdinalEncoder

from project_sc import X_test, X_test_encoded



model = XGBRegressor(enable_categorical=True)
model.load_model("xgb_model.model")

# model.score


def mar_pred(date):
    start_date = pd.to_datetime("2022-03-01")
    end_date = pd.to_datetime("2022-03-31")
    date_range = pd.date_range(start_date, end_date, freq="D")

    march=[]
    for day in date_range:
        days = str(day)[:10]
        march.append(days)

    encoder = OrdinalEncoder()
    march_enc = encoder.fit_transform(march)
    idx = march.index(date)
    mar_idx = march_enc.loc[idx]

    return model.predict(mar_idx)
mar_pred("2022-03-04")