import random

words = ['PYTHON', 'JAVA', 'SWIFT', 'RUBY', 'CSHARP', 'JAVASCRIPT']
randomChoice = random.choice(words)

display = ['_' for _ in randomChoice]
attempt_limit = 8

print("Welcome To HANGMAN")

attempts = 0

while attempts is not attempt_limit and '_' in display:
    print("\n" + ' '.join(display))
    user_guess = input("Guess what letter is in the mystery word: ").upper()

    if user_guess in randomChoice:
        for index, guess in enumerate(randomChoice):
            if user_guess == guess:
                display[index] = guess

    else:
        attempts += 1
        left = attempt_limit - attempts
        print(f"Guess is incorrect, you have {left} attempts left")


if attempts == attempt_limit:
    print(f"The word was {randomChoice}...")
    print("YOU LOSE")

else:
    print(randomChoice)
    print("You figured it out, Congratulations")
