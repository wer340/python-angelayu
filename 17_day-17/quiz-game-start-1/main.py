from trivia import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    ask = quiz.next_qestion()
    if not quiz.check_answer(ask):
       break

    print(f"your correct score :{quiz.question_list[quiz.question_number-1].answer}")
    print(f"your  score :{quiz.question_number}")
