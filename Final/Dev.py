class Text_questions():
    '''
    This is where the questions functions are going to be!
    '''


    def __init__(self, username, password):
        '''
        login
        '''
        self.username = username
        self.password = password
        
    def multiple_question(self, question, first_correct, second_correct, correct_message, wrong_message, scoreboard):
        '''
        test values
        '''
        self.question = question
        self.first_correct = first_correct
        self.second_correct = second_correct
        self.correct_message = correct_message
        self.wrong_message = wrong_message
        self.scoreboard = scoreboard

        choice = input(question)
        if choice.lower() == first_correct or choice.lower() == second_correct:
            print(correct_message)
        else:
            print(wrong_message)    
