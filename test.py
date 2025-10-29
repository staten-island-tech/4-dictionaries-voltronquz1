
cart=[]
cost=0
store=[ 
        "name":"gum",
        "price":3.99,
        "description":"chewing gum"
 }
ships={
    "name":"Chips",
    "price":"1.00",
    "description":"salted chips"
 }    
item2={
    "name":"water ",
    "price":"1.00",
    "description":"Get hydrated"
    }
coffee={
    "name":"coffee",
    "price":"2.50",
    "description":"get energy and caffeined"
    }
]
storecost=input("What item do you want: gum, Chips,water (put done when done)")

while storecost != "done":
    if "gum":
        print(input("Are you sure you want gum"))
        cost+3.99