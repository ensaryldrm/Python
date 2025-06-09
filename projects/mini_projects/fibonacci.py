fib_number = int(input("Enter the number of ficonacci elements: "))

if(fib_number <= 0):
    print("Please enter a positive number")

else:
    fibonacci_series = []
    first = 0
    second = 1
    for _ in range(fib_number + 1):
        fibonacci_series.append(first)
        temp = first + second
        first = second
        second = temp
    print(f"The first {fib_number} elements of the Fibonacci series: {fibonacci_series}")