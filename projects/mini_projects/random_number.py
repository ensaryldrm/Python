import random

random_number = random.randint(1,100)
remaining_attempts = 5
attempt_count = 0

print("--Guess a number between 1 and 100--")

while(remaining_attempts > 0):
    guess = int(input("Your guess: "))
    attempt_count += 1
    if(guess > 100 or guess < 1):
        remaining_attempts -= 1
        print("Please! Enter a number between 1 and 100")
        continue

    elif(guess > random_number):
        remaining_attempts -= 1
        print("Try a smaller number!")

    elif(guess < random_number):
        remaining_attempts -= 1
        print("Try a larger number!")
    
    else:
        print(f"Congrulations! You guessed the number correctly on your {attempt_count}.attempt")
        break

if(remaining_attempts == 0):
    print("You lost!")
    print("Correct answer: ", random_number)


