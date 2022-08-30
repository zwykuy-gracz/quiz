class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}: {current_question.text} (T/F): ").upper()
        self.check_answer(users_answer, current_question.answer)

    def check_answer(self, users_answer, correct_answer):
        if users_answer == correct_answer[0]:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()

    def end_of_game(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")