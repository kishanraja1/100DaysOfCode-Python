class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower == correct_answer.lower:
            print('Correct')
            self.score +=1
        else:
            print('You are wrong')
        print('The correct answer was ' + correct_answer)
        print('Your current score is ' + str(self.score) + '/' + str(self.question_number))
