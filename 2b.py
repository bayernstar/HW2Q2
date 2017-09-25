import json

with open('train.json') as data:
    train = json.load(data)

cuisine = []
ingredients = []
for i in train:
    cuisine.append(i["cuisine"])
    ingredients.extend(i["ingredients"])

print "number of samples: " + str(len(train))
print "number of categories: " + str(len(set(cuisine)))
print "number of unique ingredients: " + str(len(set(ingredients)))