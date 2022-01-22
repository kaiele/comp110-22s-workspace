"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730482406"

word: str = input("Enter a 5-character word: ")
if 5 != len(word):
    print("Error: Word must contain 5 characters ")
    exit()
character: str = input("Enter a single character: ")
if 1 != len(character):
    print("Error: Character must be a single character. ")
    exit()
print("Searching for " + character + " in " + word)
instances: int = 0

if word[0] == character:
    print(character + " found at index 0")
    instances = instances + 1
if word[1] == character:
    print(character + " found at index 1")
    instances = instances + 1
if word[2] == character:
    print(character + " found at index 2")
    instances = instances + 1
if word[3] == character:
    print(character + " found at index 3")
    instances = instances + 1
if word[4] == character:
    print(character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + character + " found in " + word)
elif instances == 1:
    print("1 instance of " + character + " found in " + word)
else:
    instances_occured = str(instances)
    print(instances_occured + "instance of " + character + " found in " + word)