from data import question_data
from question_model import Question
len=len(question_data)
i=1
date=["q_1","q_2","q_3","q_4","q_5","q_6","q_7","q_8","q_9","q_10","q_11","q_12"]
for item in question_data:
    date[i]=Question(question_data[item]["text"], question_data[item]["answer"])
    i+=1
