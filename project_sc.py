import numpy as np
import pandas as pd
import datetime
from datetime import timedelta

offer = pd.read_csv("C:/Users/aryij/Documents/AI Bootcamp/Section 3/project3/db_csv/departure_mod_2.csv")
prediction = pd.read_csv("C:/Users/aryij/Documents/AI Bootcamp/Section 3/project3/db_csv/prediction_mod.csv")


def country(x):
    if x == "FRA":
        return "FRA"
    elif x == "FCO":
        return "ROM"
    elif x == "MAD":
        return "MAD"
    elif x == "CDG" or x == "ORY":
        return "PAR"
    elif x == "STN" or x == "LGW" or x == "LCY" or x == "LHR":
        return "LON"

offer["dest"] = offer["iatacode_2.1"].apply(lambda x : country(x))

offer["dest_2"] = offer["iatacode_1.1"].apply(lambda x : country(x))



offer["dest"] = offer["dest"].fillna(offer["dest_2"])

offer = offer.drop(columns=["dest_2"], axis=1)

offer["arr_date"] = offer["at_2"]
offer["arr_date_2"] = offer["at_1"]

offer["arr_date"] = offer["arr_date"].fillna(offer["arr_date_2"])

offer = offer.drop(columns=["arr_date_2"], axis=1)

prediction = prediction.drop(columns=["id", "number"], axis=1)

prediction.rename(columns={"date" : "arr_date"}, inplace=True)

offer = pd.merge(left=offer, right=prediction)

offer = offer.drop(columns=["number", "seg_id_1", "seg_id_1.1", "air_number_1", 'air_number_2', 'at_2'])

offer.columns = ['code', 'total_dur', 'dur_1', "departure_1", "arrival_1", 'carriercode_1', "dep_date", 'transfer', 'dur_2',
                 "departure_2", "arrival_2", 'carriercode_2', 'bookable_seats', 'currency', 'total', 'dest', 'arr_date', 'ontime_proba']

offer = offer[['code', 'total_dur', 'dur_1', "departure_1", "arrival_1", 'carriercode_1', "dep_date", 'transfer', 'dur_2',
                 "departure_2", "arrival_2", 'carriercode_2', 'arr_date', 'bookable_seats', 'currency', 'total', 'dest', 'ontime_proba']]


# pip install isodate

# import isodate

# offer["dur_2"] = offer["dur_2"].fillna("PT0H00M")

# offer["total_dur"] = offer["total_dur"].apply(isodate.parse_duration)
# offer["dur_1"] = offer["dur_1"].apply(isodate.parse_duration)
# offer["dur_2"] = offer["dur_2"].apply(isodate.parse_duration)

# offer["dep_date"] = offer["dep_date"].apply(pd.to_datetime)

# "departure_1", "dep_date", "transfer" category??? ?????????
offer["departure_1"] = offer["departure_1"].astype("category")
offer["dep_date"] = offer["dep_date"].astype("category")
offer["transfer"] = offer["transfer"].astype("category")

from sklearn.model_selection import train_test_split

train, test = train_test_split(offer, train_size=0.8, random_state=42)

train, val = train_test_split(train, train_size=0.8, random_state=42)

# train.shape, val.shape, test.shape

target = "total"
features = ["departure_1", "dep_date", "transfer"]
# features = offer.drop(columns=[target]).columns

X_train = train[features]
y_train = train[target]

X_val = val[features]
y_val = val[target]

X_test = test[features]
y_test = test[target]

# ?????? ???????????? ??????
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt

# ?????? ?????????
predicted = y_train.mean()
y_pred_base = [predicted] * len(y_val)

mae_base = mean_absolute_error(y_val, y_pred_base)
mse_base = mean_squared_error(y_val, y_pred_base)
rmse_base = sqrt(mse_base)
r2_base = r2_score(y_val, y_pred_base)

# print("?????? ?????? (??????) :", predicted)
# print("?????? ?????? MAE :", mae_base)
# print("?????? ?????? MSE :", mse_base)
# print("?????? ?????? RMSE :", rmse_base)
# print("?????? ?????? R2 score :", r2_base)

# pip install category-encoders

# ??????????????? ??????????????? ?????? ??????

from xgboost import XGBRegressor
from category_encoders import OrdinalEncoder

encoder = OrdinalEncoder()
X_train_encoded = encoder.fit_transform(X_train)
X_val_encoded = encoder.transform(X_val)
X_test_encoded = encoder.transform(X_test)

# boosting = XGBRegressor(
#     n_estimators=1000,
#     objective="reg:squarederror",
#     learning_rate=0.2,
#     n_jobs=-1,
#     enable_categorical=True
# )

# eval_set = [(X_train_encoded, y_train),
#             (X_val_encoded, y_val)]

# boosting.fit(X_train_encoded, y_train,
#              eval_set=eval_set,
#              early_stopping_rounds=100)

# y_pred_val_xgb = boosting.predict(X_val_encoded)
# y_pred_test_xgb = boosting.predict(X_test_encoded)

# print("XGB val MAE :", mean_absolute_error(y_val, y_pred_val_xgb))
# print("XGB val MSE :", mean_squared_error(y_val, y_pred_val_xgb))
# print("XGB val RMSE :", sqrt(mean_squared_error(y_val, y_pred_val_xgb)))
# print("XGB val R2 score :", r2_score(y_val, y_pred_val_xgb))


# print("XGB MAE_test :", mean_absolute_error(y_test, y_pred_test_xgb))
# print("XGB MSE_test :", mean_squared_error(y_test, y_pred_test_xgb))
# print("XGB RMSE_test :", sqrt(mean_squared_error(y_test, y_pred_test_xgb)))
# print("XGB R2 score_test :", r2_score(y_test, y_pred_test_xgb))

# boosting.save_model("xgb_model.model")

# LightGBM ????????? ??????
from lightgbm import LGBMRegressor

lgbm = LGBMRegressor(n_estimators=100, learning_rate=0.2)

evals = [(X_train_encoded, y_train),
         (X_val_encoded, y_val)]

lgbm.fit(X_train_encoded, y_train, 
         eval_set=evals, 
         early_stopping_rounds=100)

y_pred_val_xgb = lgbm.predict(X_val_encoded)
y_pred_test_xgb = lgbm.predict(X_test_encoded)

# print("XGB val MAE :", mean_absolute_error(y_val, y_pred_val_xgb))
# print("XGB val MSE :", mean_squared_error(y_val, y_pred_val_xgb))
# print("XGB val RMSE :", sqrt(mean_squared_error(y_val, y_pred_val_xgb)))
# print("XGB val R2 score :", r2_score(y_val, y_pred_val_xgb))

# lgbm.booster_.save_model("lgbm_model.model")

import joblib
import pickle

filename = "lgbm_model.pkl"
joblib.dump(lgbm, filename)
