class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        n = self.question_number
        user_answer = input(f"Q.{n+1} {question.text} Type(True/False)? ").lower()

        if user_answer == "true" or user_answer == "false":
            self.check_answer(user_answer, question.answer)
            self.question_number += 1
        else:
            print("Please type (true or false) only.")


    ## this function only used here, not in the main file. wow
    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            print("Correct ✔")
            self.score += 1
        else:
            print("Wrong ❌")
        print(f"the answer is :{answer}")
        print(f"Your score is {self.score}.")
        print("\n")


    def quiz_still_has_questions(self):
        question_length = len(self.questions_list)
        return self.question_number < question_length

