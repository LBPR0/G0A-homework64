
temperature = 35
cloudy = False
result1 = temperature > 30 and not cloudy  # True: ტემპერატურა მეტია 30-ზე და მოღრუბლული არ არის


temperature = -5
cloudy = True
result2 = temperature < 0 or cloudy  # True: ტემპერატურა ნაკლებია 0-ზე ან მოღრუბლულია


temperature = 20
cloudy = True
result3 = temperature == 20 and cloudy  # True: ტემპერატურა ტოლია 20-ის და მოღრუბლულია


temperature = 10
windy = True
result4 = temperature < 15 and windy  # True: ტემპერატურა 15-ზე ნაკლებია და ქარია


temperature = 28
windy = False
result5 = temperature > 25 or not windy  # True: ტემპერატურა 25-ზე მეტია ან არ არის ქარი