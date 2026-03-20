import random

secret = random.randint(1,100) # this generates 12

guess = int(input("Guess a number: "))  # i guess 14

while guess is not secret:

    if guess < secret:

        print("low")

    elif guess > secret:

        print("high")

    guess = int(input("Guess a number: "))  # i guess 14

print("You guessed the number")

