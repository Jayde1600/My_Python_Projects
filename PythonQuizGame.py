questions = [
    {
        "prompt": "Which of the following is not a valid Python variable name?",
        "options": ["A. my_variable", "B. _my_variable", "C. 1st_variable", "D. MyVariable"],
        "answer": "C"
    },
    {
        "prompt": "What does the 'print()' function do in Python?",
        "options": ["A. Reads input from the user", "B. Displays output to the console",
                    "C. Performs mathematical operations", "D. Creates a new file"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following data types is mutable in Python?",
        "options": ["A. int", "B. float", "C. tuple", "D. list"],
        "answer": "D"
    },
    {
        "prompt": "What will be the output of '3 * 4 + 5' in Python?",
        "options": ["A. 17", "B. 27", "C. 32", "D. 15"],
        "answer": "A"
    },
    {
        "prompt": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    }
]


def UserChecks(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").upper()
        if answer == question["answer"]:
            print("You're Correct!\n")
            score += 1
        else:
            print("Incorrect, The correct answer is:", question["answer"] + "\n")

    print(f"You got {score} out of {len(questions)}")
    if score == len(questions):
        print("Wow, you are really smart")


UserChecks(questions)
