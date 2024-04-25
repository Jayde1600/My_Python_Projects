import random

rockpaperscissors = ["rock", "paper", "scissors"]


def game():
    rounds = int(input("How many rounds do you want play (1, 3 or 5)? "))

    user_rounds = 0

    global user_score
    user_score = 0

    global comp_score
    comp_score = 0

    while user_rounds is not rounds:
        if user_score == 0 and comp_score == 3:
            print("Wow...you are not good at this are you?")
            break

        user_pick = input("Rock, Paper or Scissors: ").lower()
        comp_pick = random.choice(rockpaperscissors)

        # The user winning (scenario)

        if user_pick == "rock" and comp_pick == "scissors":
            user_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick == "scissors" and comp_pick == "paper":
            user_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick == "paper" and comp_pick == "rock":
            user_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick == comp_pick:
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        # The computer winning (scenario)

        elif user_pick == "rock" and comp_pick == "paper":
            comp_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick == "scissors" and comp_pick == "rock":
            comp_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick == "paper" and comp_pick == "scissors":
            comp_score += 1
            user_rounds += 1
            print(f"The computer entered: {comp_pick}\nThe score is: {user_score}:{comp_score}")

        elif user_pick not in rockpaperscissors:
            print("Incorrect Input")


game()

if user_score > comp_score:
    print("Congratulations, you won!")

elif user_score < comp_score:
    print("hehe...I WIN ;)")

elif user_score == comp_score:
    print("Aww, it's a draw")
