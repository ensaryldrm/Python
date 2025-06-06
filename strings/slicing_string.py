text = "python is weird"
print(text[1:5]) # 1 to 5: ytho
print("------")
print(text[:5]) # 0 to 5: pytho
print("------")
print(text[5:]) # 5 to final char: n is weird
print("------")
print(text[::]) # all of them: python is weird
print("------")
print(text[-5:-1]) # -1 to -5: weir