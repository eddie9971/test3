import random
print('Number Guessing Game')
number = random.randint(1, 9)

chances = 0

while True:
    guess = int(input('Guess a number between 1 and 9: '))
    if guess == number:
        print(f'CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!')
        break
    elif guess < number:
        print(f"Your guess was too low: Guess a number higher than {guess}")
    else:
        print(f"Your guess was too high: Guess a number lower than {guess}")

    chances += 1