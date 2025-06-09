number = int(input("Enter a number: "))
isPrime = True
if(number < 0):
    print("You entered a wrong number! Please, enter a positive number!")
elif(number == 1):
    print("The lowest prime number is 2!")
else:
    for i in range(2,int(number**0.5) + 1):
        if(number % i == 0):
            isPrime = False
            break
    if(isPrime):
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not a prime number!") 
