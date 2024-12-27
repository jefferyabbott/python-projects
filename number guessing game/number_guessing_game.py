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
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def get_valid_guess() -> int:
    while True:
        guess = input("Guess a numnber (1-100): ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Your guess must be between 1 and 100.")


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    target = randint(1, 100)
    turns = set_difficulty()

    for attempt in range(1, turns + 1):
        print(f"You have {turns - attempt + 1} attempts remaining to guess the number.")
        guess = get_valid_guess()

        if guess == target:
            print(f"{guess} is correct! You win!")
            return
        elif guess > target:
            print("Too high.")
        else:
            print("Too low.")

    print(f"Sorry, you're out of attempts. The correct number was {target}.")


if __name__ == "__main__":
    play_game()


