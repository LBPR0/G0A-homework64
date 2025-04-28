even_count = 0 
odd_count = 0 
number = 0    

while number >= 0:
    number = int(input("Enter a number: "))
    
    if number >= 0: 
        if number % 2 == 0:  
            even_count += 1
        else:  
            odd_count += 1

print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)

