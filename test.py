
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
buying=True
while buying:
        print("What item do you want:1. gum, 2.Chips,3.water 4.Instant Coffee ")
        item=int(input("1,2,3,4 "))
        item-=1 #list reads from 0,1,2,3..etc so if 1 it gives correct input
        result=store[item]
        cart.append(result)
        cost+=result["price"]
        print(input("Do you want to continue?Y/N"))
        if "Y" or "y":
              buying=True
              print(cart)
              # print(result)
              print(cost)
        elif "N" or "n":

            buying=False
            print(f"Your item are {cart} and the cost is {cost}")
