import json

with open('1.json') as f:
    t = json.load(f)

c = int(input("kol-vo: "))
p = {"products":[]}
for i in range(c):
    name = input("Название: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))
    available = bool(input("В наличии - 1, не в наличии - 0: "))
    p['products'].append({"name":name,"price":price,"weight":weight,"available":available})

t['products'].extend(p["products"])
for i in t["products"]:
    print("Название: ", i["name"],"\n Цена: ", i["price"],"\n Вес: ", i["weight"],"\n В наличии" if i["available"] else "Нет в наличии!","\n")

with open("1.json","r") as file:
    json.dump(t, file, ensure_ascii=False, indent= None)