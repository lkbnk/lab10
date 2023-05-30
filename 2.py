import json

with open('products.json') as f:
    script = json.load(f)

c = int(input("Количество добавляемого товара: "))
p = {"products":[]}
for i in range(c):
    name = input("Название: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))
    available = bool(input("Наличие (Да - 1, Нет - 0): "))
    p['products'].append({"name":name,"price":price,"weight":weight,"available":available})

script['products'].extend(p["products"])
for i in script["products"]:
    print("Название: ", i["name"],"\n Цена: ", i["price"],"\n Вес: ", i["weight"],"\n В наличии" if i["available"] else "Нет в наличии!","\n")

with open("products.json","r") as file:
    json.dump(script, file, ensure_ascii=False, indent= None)