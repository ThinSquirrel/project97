import random
print("Number Guessing Game")
number = random.randint(0,20)
print("Guess a number between 0 and 20")
chances = 0

while chances < 5:
    guess = int(input("Enter Your Guess: "))

    if guess == number :
        print("Good Job")
        break
    elif guess < number :
        print("Guess was too low, guess higher than ",guess)
    else:
        print("Your Guess was too high. Guess lower than",guess)
        
    chances += 1

if not chances < 5:
    print("You lose, The number is", number)