from DAY17_questionmodel import Question
from Project17_data import question_data
from DAY17_quizbrain import QuizBrain

# creating question bank of Question Objects
question_bank = []
  # question bank will be a list  & we will be storing objects new question in it
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    # adding Question object into[new_question] into question_bank list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()
