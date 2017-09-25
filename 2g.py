import json
import pandas as pd
from sklearn.linear_model import LogisticRegression as lr

with open('train.json') as data:
    train = json.load(data)
with open('test.json') as data:
    test = json.load(data)

cuisine = []
ingredients = []
for i in train:
    cuisine.append(i["cuisine"])
    ingredients.extend(i["ingredients"])

singredients = list(set(ingredients))
traind = []
rowlen = len(singredients)
d = {singredients[i]: i for i in range(rowlen)}
for i in train:
    row = [0] * rowlen
    for j in i["ingredients"]:
        row[d[j]] = 1
    traind.append(row)

ingredients = []
id = []
for i in test:
    ingredients.extend(i["ingredients"])
    id.append(i["id"])

singredients = list(set(ingredients))
testd = []
for i in test:
    row = [0] * rowlen
    for j in i["ingredients"]:
        if j in d:
            row[d[j]] = 1
    testd.append(row)

LR = lr()
LR.fit(traind, cuisine)
pdOut = pd.DataFrame(columns = ["id", "cuisine"])
pdOut["id"] = id
pdOut["cuisine"] = LR.predict(testd)
pdOut.to_csv("submit.csv", index = False)