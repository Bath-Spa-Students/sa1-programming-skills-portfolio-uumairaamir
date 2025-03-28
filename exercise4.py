# Function to ask a question and evaluate the answer
def ask_question(question, correct_answer):
    user_answer = input(question).strip()  # Get user input and remove any leading whitespace
    if user_answer.lower() == correct_answer.lower():  # Compare answers ignoring case
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", correct_answer)

# Main program
def main():
    # List of questions and their correct answers
    quiz = {
        "What is the capital of France? ": "Paris",
        "What is the capital of Germany? ": "Berlin",
        "What is the capital of Italy? ": "Rome",
        "What is the capital of Spain? ": "Madrid",
        "What is the capital of Portugal? ": "Lisbon",
        "What is the capital of Netherlands? ": "Amsterdam",
    }

    # Loop the quiz questions
    for question, correct_answer in quiz.items():
        ask_question(question, correct_answer)

# Run the program
if __name__ == "__main__":
    main()