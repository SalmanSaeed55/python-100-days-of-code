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

        user_answer = input(f"{self.question_number}. {current_question.question}? (true/false)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
            print(f"The correct answer was: {answer}.")
        print(f"You're current score is {self.score}/{self.question_number}")
