"""One shot Wordle."""

__author__ = "730482406"

secret_word: str = "python"
secret_word_length = len(secret_word)
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != secret_word_length:
    guess = input(f"That was not {len(secret_word)} letters! Try again: ") 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
starting_point_emoji: str = ""

while index < secret_word_length:
    if guess[index] == secret_word[index]:
        starting_point_emoji = starting_point_emoji + GREEN_BOX
    else: 
        guessed_character: bool = False
        index_of_character: int = 0
        while index_of_character < secret_word_length:
            if secret_word[index_of_character] == guess[index]:
                guessed_character = True
            index_of_character = index_of_character + 1
        if guessed_character:
            starting_point_emoji = starting_point_emoji + YELLOW_BOX
        else:
            starting_point_emoji = starting_point_emoji + WHITE_BOX
    index = index + 1
print(starting_point_emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print(" Not quite. Play again soon!")