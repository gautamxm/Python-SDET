import random
guess  = random.randint(1,10)
attempts = 0
while guess > 0:
    n = int(input("Guess the no. : "))
    attempts+= 1
    if n < guess:
        print("Try Higher Value")
    elif n > guess:
        print("Try Lower Value")
    else : print(f"You Won the game in {attempts} Attempts")

