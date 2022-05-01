import sys
import pickle
import pandas as pd
import requests

with open('./models/X_test.pickle', 'rb') as handle:
    X_test = pickle.load(handle)

print (f"Requesting prediction for item number {sys.argv[1]} in X_test")
req_json = X_test.iloc[int(sys.argv[1])].to_json()
print(req_json)

r = requests.post('http://localhost:5000/predict', json=req_json)
print(f"Got status code {r.status_code} with contents {r.content}")
