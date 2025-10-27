# microcenter{
#     {    item=
#         "name":"Nvidia GeForce 5070 "
#         "price":549.99
#         "description": 
#         }
# }




quarters = int(input("Amount of quarters she has. | Input Total Quarters:  "))    # This the amount of quarters she has or the amount you would like her to have.
first = int(input("First Slot Machine | Input amount of time this Slot Machine was played already:  "))    #This is how many times the first slot machine has already been played.
second = int(input("Second Slot Machine | Input amount of time this Slot Machine was played already:  "))    #JUST READ THE DAM "----" I AIN'T TYPING ALL THIS OUT:c
third = int(input("Third Slot Machine | Input amount of time this Slot Machine was played already:  "))    # read the comment stuff in the line above this one.

count = 0    

while quarters >= 0:     
    first += 1     
    quarters -= 1    
    count += 1    
    if first == 35:      
        quarters += 30    
        first = 0      

    second += 1    
    quarters -= 1   
    count += 1   
    if second == 100:    
        quarters += 60    
        second = 0   
        
    third += 1    
    quarters -= 1  
    count += 1    
    print(quarters)
    if third == 10:   
        quarters += 9    
        third = 0   



print(f"Martha plays {count} times before going broke.")

