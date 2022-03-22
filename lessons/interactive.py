"""My own wordle."""

__author__ = "730482406"


def contains_char(any_length: str, single_character: str) -> bool:
    """Generates a bool expression for a character search."""
    assert len(single_character) == 1
    i: int = 0
    while i < len(any_length):
        if single_character == any_length[i]:
            return True
        else:
            i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str: 
    """Generates a string of emojis based on character."""
    assert len(guess) == len(secret)
    index: int = 0
    emoji_build: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_build += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_build += YELLOW_BOX
        else:
            emoji_build += WHITE_BOX
        index += 1
    return emoji_build


def input_guess(expected_length: int) -> str:
    """Prompt user for guess until guessed word is expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_wordle: str = "codes"
    length_of_secret = len(secret_wordle)
    n: int = 1
    turn: str = ""
    while n < 6:
        print(f"=== Turn {n}/6 ===")
        turn = input_guess(length_of_secret)
        print(emojified(turn, secret_wordle))
        if turn == secret_wordle:
            print(f"You won in {n}/6 turns!")
            exit()
        elif n == 6:
            print("X/6 - Sorry, try again tomorrow!")
        n += 1


if __name__ == "__main__":
    main()