def find_divisors(number):
    divisors = []
    for item in range(1,number + 1):
        if(number % item == 0):
            divisors.append(item)
            
    return divisors

number = int(input("Enter a positive integer: "))
if(number <= 0):
    print("Please, enter a positive number")
else:
    result = find_divisors(number)
    print(f"The divisors of {number} are: {result}")