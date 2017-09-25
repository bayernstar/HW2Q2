import json

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
d = {singredients[i]: i for i in range(len(singredients))}
for i in train:
    row = [0] * len(singredients)
    for j in i["ingredients"]:
        row[d[j]] = 1
    traind.append(row)

ingredients = []
for i in test:
    ingredients.extend(i["ingredients"])

singredients = list(set(ingredients))
testd = []
d = {singredients[i]: i for i in range(len(singredients))}
for i in test:
    row = [0] * len(singredients)
    for j in i["ingredients"]:
        row[d[j]] = 1
    testd.append(row)