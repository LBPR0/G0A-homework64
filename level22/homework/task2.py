
vegetables = ["კარტოფილი", "სტაფილო", "ხახვი", "ბროკოლი"]


user_choice = int(input("შეიყვანეთ რიცხვი 0-იდან 4-მდე: "))

if 0 <= user_choice < 4:
    print(f"თქვენ აირჩიეთ: {vegetables[user_choice]}")
else:
    print("არასწორი არჩევანი!")