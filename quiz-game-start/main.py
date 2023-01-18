from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data)
question_bank = []
for question in question_data["results"]: # This is a list
    # question_text = question['text']
    # question_answer = question['answer']
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) # New question object
    question_bank.append(new_question)
    # question_bank.append(Question(question['text'], question['answer']))


# print(type(question_bank))
# print(question_bank[0])
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(questions_list = question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")