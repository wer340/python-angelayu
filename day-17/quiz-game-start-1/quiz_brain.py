class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list

    def next(self,):
        for item in self.question_list:
            self.question_number+=1
            answer_q=input(f"{item.tetx} :True or False")
