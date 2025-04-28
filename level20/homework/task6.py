sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1
    elif char >= 'a' and char <= 'z':  
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)