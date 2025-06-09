age = 19
name = "Ensar Yildirim"
text = f"My name is {name}, I am {age} years old!"
print(text)

text2 = "The prince only {price} turkish liras!"
print(text2.format(price = 70))

text3 = "My name is {fullName}, I'm {age} years old!".format(fullName = "Ensar Yildirim", age = 19)
print(text3)