
cart=[]
cost=0
store=[ 
{
        "name":"gum",
        "price":3.99,
        "description":"chewing gum"
},
{
    "name":"Chips",
    "price":"1.00",
    "description":"salted chips"
 }, 
{
    "name":"water ",
    "price":"1.00",
    "description":"Get hydrated"
},
{
    "name":"coffee",
    "price":"2.50",
    "description":"get energy and caffeined"
},
]

item=input("What item do you want: gum, Chips,water (type done when done)")

while item != "done":
    if "gum" or "coffee" or "chips" or "water":
        print(input(f"Are you sure you want {item}"))
        if "Yes":
            cost+=3.99
            cart.append(item)
            print(f"You have {cart} and the cost is {cost}")
            input("What else do you want")
    