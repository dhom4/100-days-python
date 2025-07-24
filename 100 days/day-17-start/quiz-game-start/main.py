from question_model import Question
from data import question_data, question_data_2
from quiz_brain import QuizBrain


question_bank = [] # putting the question into list of objects each one contain Q&A.
# for q in question_data:
#     question_text = q['text']
#     question_answer = q['answer']
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

for q in question_data_2:
    question_text = q['question']
    question_answer = q['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.quiz_still_has_questions():
    quiz.next_question()

print(f"you've complete the quize\nyou final score is {quiz.score}/{quiz.question_number}")
