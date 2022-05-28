class Question:

    def __init__(self, text, answer):
        self.question = text
        self.answer = answer


new_q = Question('where do you live?', 'Atlanta')
print(new_q)