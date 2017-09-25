import json
import numpy as np
from sklearn.model_selection import KFold as kf, cross_val_score as cvs
from sklearn.linear_model import LogisticRegression as lr

with open('train.json') as data:
    train = json.load(data)

cuisine = []
ingredients = []
for i in train:
    cuisine.append(i["cuisine"])
    ingredients.extend(i["ingredients"])

singredients = list(set(ingredients))
traind = []
d = {singredients[i]: i for i in range(len(singredients))}
for i in train:
    row = [0] * len(singredients)
    for j in i["ingredients"]:
        row[d[j]] = 1
    traind.append(row)


k_fold = kf(n_splits=3)
la = cvs(lr(), traind, cuisine, cv=k_fold, n_jobs=-1)

f = open('2f', 'wb')
s = "Logistic Regression accuracy is: " + str(np.mean(la))
print s
f.write(s)