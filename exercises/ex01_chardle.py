"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730482406"

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")

i = 0
for c in word:
    if c == character:
        print(str(character) + "found at index" + str(i))
    i = i + 1 