from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
still_has_questions = quiz_brain.still_has_questions()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    
quiz_brain.end_of_game()