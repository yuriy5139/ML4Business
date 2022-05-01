import pandas as pd
from flask import Blueprint
import pickle
import flask

import sys
import numpy as np
from catboost import CatBoostClassifier

main = Blueprint('main', __name__)

with open('./project/models/model.pickle', 'rb') as handle:
    model = pickle.load(handle)

#with open('./project//models/X_test.pickle', 'rb') as handle:
#    X_test = pickle.load(handle)


@main.route('/predict', methods=('POST',))
def make_prediction():

    if flask.request.method == "POST":
        request_json = flask.request.get_json()
    print("test item is ", request_json)
    test_item = pd.read_json(request_json, orient='records', typ='series')

    prediction = str(model.predict(test_item))
    print("predicion is ", prediction)

    return prediction

