
words = ["პალინდრომი", "სიტყვა", "ტესტი", "კოდი", "პითონი"]


reversed_words = words[::-1]


index = 0


for word in reversed_words:

    if index % 2 == 0:
        print(word)

    index += 1