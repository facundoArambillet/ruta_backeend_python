items = [
    {"product": "Remera",
     "price": 500,
    },
    {"product": "Camisa",
     "price": 350,
    },
    {"product": "Jean",
     "price": 200,
    }
]

prices = list(map(lambda x: x["price"], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .21 #Es lo mismo que new_item["price"] * 0.21
    return new_item
new_item = list(map(add_taxes,items))
print(new_item)