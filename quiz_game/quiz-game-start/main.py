from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    # print(question['text'])
    # print(question['answer'])
    question_bank.append(Question(question['text'], question['answer']))


print(question_bank[0].question)