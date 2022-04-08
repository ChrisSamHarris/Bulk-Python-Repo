class QuizBrain:
    def __init__(self, question_list):
        self.qn = 0
        self.score = 0
        self.ql = question_list

    def still_has_questions(self):
        return self.qn < len(self.ql)

    def next_question(self):
        current_question = self.ql[self.qn]
        self.qn += 1
        user_answer = input(f"Q.{self.qn}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's Wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.qn}")
        print("\n")

    #def __repr__(self):
        #return f"{self.__class__.__name__}, {self.ql.text}, {self.qn}"
        # note the .text after the self.ql on the next question input, is there a way to do this automatically?
        # The above refers to the dictionary values of the question_list
        # __repr__ and __str__ ?
        # https://www.pythontutorial.net/python-oop/python-__repr__/
        # the goal of __str__ is to be readable
        # The goal of __repr__ is to be unambiguous - default is to return the memory address of the object, you can customise the string representation of the object for humans
        #   def __repr__(self):
        #         return f'Person("{self.first_name}","{self.last_name}",{self.age})'
