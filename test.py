
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
""" for index, item in enumerate(store):
    print(index, ":", item["name"], item["price"]) """
item=input("What item do you want:1. gum, 2.Chips,3.water ")
while True:
        print(input(f"Are you sure you want {item}"))
        if "Yes" or "yes":
            for index,item in enumerate(store):
                cost+=store["price"]
            cart.append(item)
            print(f"You have {cart} and the cost is {cost}")
            input("What else do you want")
        if "no" or "No":
            break   



# print(f"You have these items:{cart} and the cost {cost}")
# for index, item in enumerate(items):
#         print(index, ":" ,(item)["name"])
#         items[1]["name"]



# cart = []
# cost = 0
# choice = int(input("What would you like to buy?"))
# cart.append(items[choice])
# cost += items[choice]["price"]
# print(f"Added {items[choice]['name']} into cart")

# while True:
#     checkout = (input("Would you like to continue shopping? (Yes/No)"))
#     if checkout == "Yes":
#         choice = int(input("What else would you like to buy?"))
#         cart.append(items[choice])
#         cost += items[choice]["price"]
#         print(f"Added {items[choice]['name']} into cart")
#     if checkout == "No":
#          break

# for item in cart: 
#     print(f'{item["name"]} ${int(item["price"])}')
# print(f"Total: ${cost}")