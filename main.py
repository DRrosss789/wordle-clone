import random
import json

length = input("Word Length (5): ")
if not length:
    length = 5

while int(length) < 1 or int(length) > 15:
    print("The length must be between 1-15")
    length = input("Word Length (5): ")

with open(f"words/{int(length)}.json", "r") as file:
    data_dict = json.load(file)

wordlist = [obj["word"] for obj in data_dict]

word = list(random.choice(wordlist).lower())
guess = ""
guesses = 0
revealed = ["_"] * len(word)


while not guess == word:
    if (guesses > 6):
        print(f"Nice try, the word was \"{"".join(word)}\"")
        break

    guess = list(input("Guess: ").lower())

    while not len(guess) == len(word):
        print(f"Your guess must be {len(word)} letter{"s" if len(word) > 1 else ""} long.")
        guess = list(input("Guess: ").lower())

    while not "".join(guess) in wordlist:
        print(f"That word isnt in the word list.")
        guess = list(input("Guess: ").lower())


    guesses += 1

    for i in range(len(word)):
        if guess[i] == word[i]:
            revealed[i] = f"[{guess[i].capitalize()}]"
        elif guess[i] in word:
            revealed[i] = f"({guess[i]})"
        else:
            revealed[i] = f"-{guess[i]}-"

    print("".join(revealed))

print("Congratulations!")