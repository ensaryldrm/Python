adjectives = ["Red","Big","Tasty"]
fruits = ["Grape","Strawberry","Cherry"]

for i in adjectives:
    for j in fruits:
        print(i,j,end=" ")
    print("\n")



myNumbers = [[70,19],
             [34,7],
             [23,41]]

for i,j in myNumbers:
    print(f"{i} - {j}")