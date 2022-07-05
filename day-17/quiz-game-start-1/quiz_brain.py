class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_qestion(self, ):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        answer_q = input(
            f"Q.{self.question_number} - {current_q.text} :True/False :? ")
        return answer_q

    def check_answer(self, ask):
        if self.question_list[self.question_number - 1].answer == ask:
            print("You got it right!")
            return True
        else:
            return False
    def still_has_question(self):
        return self.question_number<len(self.question_list)
