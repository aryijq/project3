from flask import Flask, render_template, request
# from flask_app.routes import user_routes
import pandas as pd

from xgboost import XGBRegressor
import xgboost
import matplotlib.pyplot as plt
from category_encoders import OrdinalEncoder
import numpy as np
import pandas as pd



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


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<date>")
def date(date):
    
    pred_price = mar_pred(date)
    price = round(pred_price.tolist()[0],2)

    return render_template("date.html", avg_price=price, date=date)



if __name__ == "__main__":
    app.run(debug=True)
