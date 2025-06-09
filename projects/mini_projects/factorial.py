result = 1
i = 1
number = int(input("Enter a max value: "))
while i<=number:
    result *= i
    i += 1
print(f"Factorial of {number}! = {result}")