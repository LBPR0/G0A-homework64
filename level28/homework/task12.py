s = "Create your own string here"
word = input()
pos = s.find(word)
if pos != -1:
    print(pos)
else:
    print("word not found")