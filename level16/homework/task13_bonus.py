correct_pin = "1234"  
attempts = 0

pin = ""
while pin != correct_pin:
    pin = input("შეიყვანეთ 4-ციფრიანი PIN კოდი: ")
    attempts += 1

print("ავტორიზაცია წარმატებით გაიარეთ!")
print("სულ" + " " + str(attempts) + " " + "ცდა დასჭირდა.")