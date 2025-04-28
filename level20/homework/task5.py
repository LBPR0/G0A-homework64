total = 0  
count = 0  

number = 0 
while number != -1:  
    number = int(input("Enter a number: "))
    
    if number != -1: 
        total += number
        count += 1

if count > 0: 
    average = total / count
    print("The average of the entered numbers is:", average)
