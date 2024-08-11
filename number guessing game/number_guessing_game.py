from random import randint


def set_difficulty():
    """Lets the user choose an easy or hard game.
    Easy gets 10 turns, hard gets 5 turns."""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

target = randint(1, 100)
turns = set_difficulty()

for x in range(turns):
    guess = 'X'
    while not guess.isdigit():
        print(f"You have {turns - x} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
    guess = int(guess)
    if guess == target:
        print(f"{guess} is correct, you win!")
        break
    elif guess > target:
        print("too high")
    else:
        print("too low")
