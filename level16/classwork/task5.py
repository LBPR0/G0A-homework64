# სწორი პაროლი
correct_password = "12345"
incorrect_password = ""
# პაროლის შემოწმება
user_input = ""
while user_input != correct_password:
    user_input = input("შეიყვანეთ პაროლი: ")
    if user_input != correct_password:
        print("არასწორი პაროლი, სცადეთ თავიდან.")

print("პაროლი სწორია! წვდომა ნებადართულია.")