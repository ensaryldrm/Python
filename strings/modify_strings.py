text = "Python is doing well"
text2 = "   Python is doing well   "
text3 = "Hello, Python, java, c#"
print(text.upper()) #upper case : PYTHON IS DOING WELL
print("------")
print(text.lower()) #lower case : python is doing well
print("------")
print(text2.strip()) #no space in start and finish char
print("------")
print(text.replace("P","T")) # P -> T: Tython is doing well
print("------")
print(text3.split("a")) 

