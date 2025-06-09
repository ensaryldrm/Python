fruits = ["Grape","Orange","Strawberry","Pineapple","Melon","Watermelon"]
new_fruits = fruits + ["Cherry","Apple"]
print(new_fruits[7])
print(len(new_fruits))
print("-----------------------------------------\n")

new_fruits.append("Banana")
print(new_fruits)
print(len(new_fruits))

print("-----------------------------------------\n")


new_fruits.insert(1,"Cherry")
print(new_fruits)
print(len(new_fruits))

print("-----------------------------------------\n")


Car = ["Ford","Honda"]
Car2 = ["Mazda","Ferrari"]

Car.extend(Car2)

print(Car)
print(len(Car))