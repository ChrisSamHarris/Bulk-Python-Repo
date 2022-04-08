from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Note the openTrivia DB API responds with dictioanry, redact the first two values and transform into a list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question) #question objects now stored in memory

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the Quiz! Your final score was {quiz.score}/{quiz.qn}.")
# Question, why do we use double and single underscore before attributes in Classes?
# Single leading underscores are generally used in classes to define 'internal' attributes. I.e. attributes that are not meant to be accessed from the outside of the class - used for intermediate computations
# double underscore is used for name mangling, this fixes a attribute value does not get over-written in subclasses
# https://towardsdatascience.com/whats-the-meaning-of-single-and-double-underscores-in-python-3d27d57d6bd1