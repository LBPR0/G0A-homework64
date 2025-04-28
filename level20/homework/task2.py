positive_sum = 0
number = 0 

while number >= 0:  
    number = int(input("Enter a number: "))
    
    if number >= 0:  
        positive_sum += number

print("The sum of all positive numbers is:", positive_sum)