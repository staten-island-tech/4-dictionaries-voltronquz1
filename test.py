
cart=[]
cost=0
store = [

{
      "name" : "watermelon gum",
      "price" : 3.99,
      "description:": "chewing gum"
},
  {
      "name" : "lays chips",
      "price" : 1.00,
      "description":"salted chips"
    },
  {
      "name" : "Poland Spring",
      "price" : 1.00,
      "description":"Get hydrated"
    },
  {
        "name":"instant coffee",
        "price":2.50,
        "description":"get caffeined"
    }

]
for index, item in enumerate(store):
    print(index, ":", item["name"], item["price"])
item=input("What item do you want: gum, Chips,water (type done when done)")

while True:
    if store["name"]:   
        print(input(f"Are you sure you want {item}"))
        if "Yes" or "yes":
            for index,item in enumerate(store):
                cost+=store["price"]
            cart.append(item)
            print(f"You have {cart} and the cost is {cost}")
            input("What else do you want")
        if "no" or "No":
            break 