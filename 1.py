import json

with open('products.json') as f:
    script = json.load(f)

for i in script['products']:
    print("Название: ", i["name"],"\n Цена: ", i["price"],"\n Вес: ", i["weight"],"\n В наличии" if i["available"] else "Нет в наличии!","\n")