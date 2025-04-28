vowels = "aeiouAEIOU"
sentence = input("Enter a sentence: ")

vowel_count = 0
lenght = 0

for char in sentence:
    if char == "a" or char == "A":
        vowel_count += 1
    elif char == "e" or char == "E":
        vowel_count += 1
    elif char == "i" or char == "I":
        vowel_count += 1
    elif char == "o" or char == "O":
        vowel_count += 1   
    elif char == "u" or char == "U":
        vowel_count += 1
        else:
            consonant_count += 1
        lenght += 1
        print(f"Vowels in total: {vowel_count}")
        print(f"Consonants in total: {consonant_count}")
    print(char)



    for char in sentence:
        if char in vowels:
            vowel_count += 1
    elif:
        consonant_count += 1
    lenght += 1
    print(f"Vowels in total: {vowel_count}")
    print(f"Consonants in total: {consonant_count}")
    print(char)


        for char in sentence:
        if char in vowels:
            vowel_count += 1
    elif char not in vowels and char != " ":
        consonant_count += 1
    lenght += 1
    print(f"Vowels in total: {vowel_count}")
    print(f"Consonants in total: {consonant_count}")
    print(char)