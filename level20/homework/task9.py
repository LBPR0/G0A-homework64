colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("Enter an index (0-4): "))
if 0 <= index <= 4:
    print("The color at index", index, "is:", colors[index])
else:
    print("Invalid index. Please enter a number between 0 and 4.")