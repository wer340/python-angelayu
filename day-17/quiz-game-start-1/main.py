from data import question_data
from question_model import Question
len=len(question_data)
question_bank=[]
for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))

print(question_bank[10].text)
print(question_bank[10].answer)