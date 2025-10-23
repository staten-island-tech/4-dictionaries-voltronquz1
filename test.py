# microcenter{
#     {    item=
#         "name":"Nvidia GeForce 5070 "
#         "price":549.99
#         "description": 
#         }
# }



count=0
quarter=input()
first=input()
second=input()
third=input()
while quarter>0:
    quarter-1
    count+=1
    first+=1
    if first==35:
        quarter+30
        first=0
    quarter-1
    count+=1
    if second==100:
        quarter+60
        second=0
    quarter-1
    count+=1
    if third==10:
        quarter+9
    print(f"She plays{count}times before poor")