import random
number = random.randint(1,9)
chances = 5

print("Number Guessing Game. Guess a number from 1 to 9.")
while chances>0:
    guess = int(input())

    if guess>number:
        print("Your guess was too high.")
    if guess<number:
        print("Your guess was too low")
    if guess == number:
        print("You win!")
        exit()
        break
    chances = chances-1

if chances == 0:
    print("You lose.")
    exit()