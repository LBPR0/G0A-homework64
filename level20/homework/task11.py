colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("Enter an index (0-3): "))
if 0 <= index <= 3:
    new_color = input("Enter a new color: ")
    colors[index] = new_color 
    print("Updated list:", colors)
else:
    print("Invalid index. Please enter a number between 0 and 3.")