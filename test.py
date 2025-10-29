
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
for index, item in enumerate(store):
    print(index+1, ":", item["name"])
# storecost=input("What item do you want: gum, Chips,water (put done when done)")

# while storecost != "done":
#     if "gum":
#         print(input("Are you sure you want gum"))
#         cost+3.99