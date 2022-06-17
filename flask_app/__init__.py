from flask import Flask, render_template, request
# from flask_app.routes import user_routes

import os
import sys
sys.path.append('C:/Users/aryij/Documents/AI Bootcamp/Section 3/project3')

from project3 import project_sc
from load_lightgbm import july_pred


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def pred():
    date = request.args["date"]
    city = request.args["city"]
    transfer = request.args["transfer"]

    pred_price = july_pred(city, date, transfer)
    price = round(pred_price[0],2)

    return render_template("date.html", avg_price=price, date=date, city=city)

if __name__ == "__main__":
    app.run(debug=True)
