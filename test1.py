quarters = int(input("Amount of quarters she has. | Input Total Quarters:  "))    
first = int(input("First Slot Machine | Input amount of time this Slot Machine was played already:  "))   
second = int(input("Second Slot Machine | Input amount of time this Slot Machine was played already:  "))
third = int(input("Third Slot Machine | Input amount of time this Slot Machine was played already:  "))   

count = 0    

while quarters >= 0:     
    first += 1     
    quarters -= 1    
    count += 1    
    if first == 35 and quarters > 0:      
        quarters += 30    
        first = 0      

    second += 1    
    quarters -= 1   
    count += 1   
    if second == 100 and quarters > 0:    
        quarters += 60    
        second = 0   
    if quarters==0:
        break
    third += 1    
    quarters -= 1  
    count += 1    
    print(quarters)
    if third == 10 and quarters > 0:
        quarters += 9    
        third = 0   



print(f"Martha plays {count} times before going broke.")

