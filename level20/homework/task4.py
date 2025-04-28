correct_pin = 1234  
attempts = 3  

while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    
    if entered_pin == correct_pin: 
        print("Access Granted")
        attempts = 0  
    else:
        attempts -= 1 
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempts left.")
        else:
            print("Access Denied")