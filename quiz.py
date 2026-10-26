def play_quiz():
    # Store questions, options, and correct answers
    questions = [
        {
            "question": "1. Which language are we using?",
            "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "answer": "B"
        },
        {
            "question": "2. Which data type stores True or False?",
            "options": ["A. int", "B. str", "C. bool", "D. list"],
            "answer": "C"
        },
        {
            "question": "3. Which keyword defines a function in Python?",
            "options": ["A. func", "B. define", "C. function", "D. def"],
            "answer": "D"
        },
        {
            "question": "4. Which symbol starts a comment in Python?",
            "options": ["A. #", "B. //", "C. /*", "D. @@"],
            "answer": "A"
        },
        {
            "question": "5. Which function displays output in Python?",
            "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
            "answer": "B"
        },
        {
            "question": "6. Which data structure stores key-value pairs?",
            "options": ["A. Tuple", "B. Set", "C. Dictionary", "D. String"],
            "answer": "C"
        },
        {
            "question": "7. Which loop repeats while a condition is true?",
            "options": ["A. if", "B. while", "C. switch", "D. class"],
            "answer": "B"
        },
        {
            "question": "8. What is the result of 3 ** 2?",
            "options": ["A. 5", "B. 6", "C. 9", "D. 8"],
            "answer": "C"
        },
        {
            "question": "9. Which method adds an item to the end of a list?",
            "options": ["A. append()", "B. add_end()", "C. insert_end()", "D. push_back()"],
            "answer": "A"
        },
        {
            "question": "10. Which module generates random numbers?",
            "options": ["A. math", "B. random", "C. time", "D. os"],
            "answer": "B"
        }
    ]

    score = 0

    print("\n================================")
    print("       PYTHON QUIZ GAME")
    print("================================")
    print("Choose the correct option: A, B, C, or D")
    print()

    # Display each question
    for item in questions:
        print(item["question"])

        for option in item["options"]:
            print(option)

        # Validate user input
        while True:
            user_answer = input("Your answer: ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid choice! Enter A, B, C, or D.")

        # Check the answer
        if user_answer == item["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct option:", item["answer"], "\n")

    # Display final results
    total = len(questions)
    percentage = (score / total) * 100

    print("================================")
    print("          QUIZ RESULTS")
    print("================================")
    print("Total questions:", total)
    print("Correct answers:", score)
    print("Wrong answers:", total - score)
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good effort! Keep practising.")
    else:
        print("Keep learning and try again!")

# Main program
while True:
    play_quiz()

    again = input("\nDo you want to play again? (yes/no): ")
    if again.strip().lower() != "yes":
        print("Thank you for playing!")
        break