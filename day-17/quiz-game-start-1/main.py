from data import question_data
from question_model import Question
len=len(question_data)

for item in question_data:
    first=Question(question_data["text"], question_data["answer"])


