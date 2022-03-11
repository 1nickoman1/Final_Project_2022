class Text_questions():
    '''
    This is where the questions functions are going to be!
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def multiple_question(self, question, maybeanswer1, correctanswer1, correctanswer2, correctmessage, wrongmessage, scoreboard):
        '''
        Multiple question setup, It will ask for a question, and two maybe answers as well two correct answers and wrong message.
        '''
        print(question)
        maybeanswer1 = input(maybeanswer1)
        if maybeanswer1.lower() == correctanswer1 or maybeanswer1.lower() == correctanswer2:
            print(correctmessage)
            scoreboard  += 1
        else:
            print(wrongmessage)

    def true_false_question(self, question, correctanswer1, correctanswer2, correctmessage, wrongmessage, scoreboard):
        '''
        True and false question setup. It will ask if the question is true or false.
        '''
        print(question)
        maybeanswer1 = input(":")
        if maybeanswer1.lower() == correctanswer1 or maybeanswer1.lower() == correctanswer2:
            print(correctmessage)
            scoreboard += 1
        else:
            print(wrongmessage)
                