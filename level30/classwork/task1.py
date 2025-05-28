numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
name = 'stopasianhate'

print(len(numbers))
print(len(name))

numbers.append(10)
numbers.append(11)
numbers.append(12)

numbers.insert(2, 99)
numbers.insert(4, 58)
numbers.insert(6, 78)

numbers.remove(1)
numbers.remove(2)
numbers.remove(3)

numbers.pop(0)
numbers.pop(9)
numbers.pop(8)

print(numbers)



def greet():
    print('Hello')
    print('Welcome')

greet()
greet()



def new_greet(first_name, last_name):
    print(f'Greetings {first_name} {last_name}')

new_greet('black', 'guy')
new_greet('Jackie', 'Chan')

# პარამეტრი არის ფუნქციის განსაზღვრის დროს გამოყენებული ცვლადი
# არგუმენტი არის ის მნიშვნელობა, რომელიც ფუნქციის გამოძახების დროს გადაეცემა პარამეტრს