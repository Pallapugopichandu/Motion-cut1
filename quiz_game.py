# quiz_game.py

# Define the questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
}

def ask_question(question, correct_answer):
    """
    Function to ask a question and check if the user's answer is correct.
    """
    user_answer = input(question + " ").strip()
    return user_answer.lower() == correct_answer.lower()

def run_quiz():
    """
    Function to run the quiz, ask each question, and calculate the score.
    """
    score = 0
    total_questions = len(questions)
    
    for question, answer in questions.items():
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {answer}")
    
    print(f"Your final score is {score}/{total_questions}")

# Entry point for the script
if _name_ == "_main_":
    run_quiz()