from data import question_data
from question_model import Question

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_answer = q["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

print(question_bank)