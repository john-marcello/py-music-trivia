import json, random, string
from html import unescape

def load_data():
    # load 5 randon questions and answers from json file
    with open("data_pkg/source.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        results = random.sample(data['results'], 5)

    # cleans data to ensure html entitites and unicode render as plain text
    for result in results:
        result['question'] = unescape(result['question'])
        result['correct_answer'] = unescape(result['correct_answer'])
        result['incorrect_answers'] = [unescape(answer) for answer in result['incorrect_answers']]
        # Repeat this process for other fields as needed

    return results
    
def play_game():
    # set up variable for tracking score and loads data
    correct_answers = 0
    queries = load_data()

    # concatenate and enurate both correct and incorrect answers, then shuffle
    for question_number, query in enumerate(queries, start=1):
        question = query['question']    
        correct_answer = query['correct_answer']
        answers = [query['correct_answer']] + query['incorrect_answers']
        random.shuffle(answers)

        # set up enumerated (by letter) possible answers and print
        print(f"\n{question_number}: {question}")
        print("Options:")
        for index, answer in enumerate(answers, start=0):
            letter = string.ascii_uppercase[index]
            print(f"{letter}. {answer}")

        # prompt user for an answer
        while True:
            user_choice = input("\nEnter your answer (A, B, C, or D): ").upper()[0]
            if user_choice in ('A', 'B', 'C', 'D'):
                break
            else:
                print("Try again. Please enter A, B, C, or D.")

        selected_index = ord(user_choice) - ord('A')
        selected_answer = answers[selected_index]

        # check if selected answer is correct and update score
        if selected_answer == correct_answer:
            correct_answers += 1
            print(f"\nCorrect! You answered: {selected_answer}")
            print("Keep up the good work...\n")
            print(f"Your score is: {correct_answers} out of {question_number}.")
        else:
            print(f"\nWrong! You answered: {selected_answer}")
            print(f"The correct answer is: {correct_answer}\n")
            print(f"Your score is: {correct_answers} out of {question_number}.")
    
        if question_number == len(queries):
            percent = (correct_answers / question_number) * 100
            score = "{:.2f}%".format(percent)
            print("You've completed all the questions!\n")
            print(f"Your score is: {score}\n")
            break