
number = int(input("Enter a number: "))


if number > 0:
    if number % 2 == 0:
        print("The number is positive and odd.")
    else:
        print("The number is positive and even.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")