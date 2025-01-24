"""
Quiz game where user answers a number of multiple choice questions.
Following the quiz their score is displayed.
"""
import random
import time
from inputimeout import inputimeout

if __name__ == "__main__":
    
    question_library = [
        {
            "question": "What is the capital of France?",
            "options": ["Madrid", "Berlin", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["Python", "JavaScript", "C++", "Java"],
            "answer": "JavaScript"
        },
        {
            "question": "What is 7 multiplied by 8?",
            "options": ["54", "56", "64", "72"],
            "answer": "56"
        },
        {
            "question": "Who wrote the novel '1984'?",
            "options": ["George Orwell", "Aldous Huxley", "J.K. Rowling", "Ernest Hemingway"],
            "answer": "George Orwell"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "HO"],
            "answer": "H2O"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1905", "1912", "1920", "1931"],
            "answer": "1912"
        },
        {
            "question": "Which organ in the human body is responsible for pumping blood?",
            "options": ["Brain", "Lungs", "Heart", "Liver"],
            "answer": "Heart"
        },
        {
            "question": "What does CPU stand for in computers?",
            "options": ["Central Processing Unit", "Computer Processing Unit", "Central Programming Unit", "Core Programming Unit"],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "Thailand", "South Korea"],
            "answer": "Japan"
        }
    ]

    # gameplay
    while True:
        score = 0
        guesses = []

        # get 5 random questions
        random.shuffle(question_library)
        questions = question_library[:5]

        # display title
        print("\nWelcome to Quiz Game!\n")

        # display each question
        for question in questions:
            print(f'{question["question"]}\n')

            # display answer options
            letters = ["A", "B", "C", "D"]
            letter_iter = iter(letters)
            answer = ""
            for option in question["options"]:
                letter = next(letter_iter)
                print(f"{letter}). {option}")
                if option == question["answer"]:   # store correct letter 
                    answer = letter
            print()

            # get user input
            print("You have 10 seconds to answer.\n(Enter A, B, C, or D)")
            start_time = time.time()
            try:
                guess = inputimeout(prompt="Answer: ", timeout=10).upper()  # sets input timer to 10 seconds
            except Exception:
                guess = "Timed Out"

            # validate input
            while guess not in letters and guess != "Timed Out":
                try:
                    print("Invalid answer. Try Again.")
                    print("\n(Enter A, B, C, or D)")
                    guess = inputimeout(prompt="Asnwer: ", timeout=max(10-(time.time()-start_time), 0)).upper() # update timer for time passed since 10 second countdown started
                except Exception:
                    guess = "Timed Out"

            # store guess
            try:
                guesses.append(question["options"][letters.index(guess)])
            except Exception:
                guesses.append(guess)

            # check guess
            if guess ==  answer:
                score += 1
                print("Correct!")
            else:
                if guess == "Timed Out":
                    print("You ran out of time!")
                else:
                    print("Incorrect!")
                print(f"The correct answer was {answer}: {question["answer"]}")

            # ask to move on
            if len(guesses) == 5:
                input("Press 'Enter' to see your score.")
            else:
                input("Press 'Enter' to go to the next question.")
            print()
        
        # display result
        print(f"You scored a {score / 5 * 100}%!\n")

        # ask to review answers
        review = input("Would you like to review your answers? (Enter 'Y' or 'N'):").lower()
        while review not in ["y", "n"]:
            print("Invalid entry. Please try again.")
            review = input("Would you like to review your answers? (Enter 'Y' or 'N'):").lower()
        print()
        # display review
        if review == "y":
            guess_iter = iter(guesses)
            for question in questions:
                print(question["question"])
                print(f"Your Answer: {next(guess_iter)}")
                print(f"Correct Answer: {question["answer"]}\n")
                
        # play again?
        play_again = input("Play Again? (Enter 'Y' or 'N'): ").lower()
        while play_again not in ["y", "n"]:
            print("Invalid entry. Please try again.")
            play_again = input("Play Again? (Enter 'Y' or 'N'): ")
        # exit game
        if play_again == "n":
            exit()
        print("\n")
