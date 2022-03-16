scoreboard = 0 



#import



#function
def correct_question(score):    
    if score == "Correct":
        global scoreboard
        scoreboard = scoreboard + 1
        
def wrong_question(score):
    if score == "Wrong":
        global scoreboard
        scoreboard = scoreboard - 1
    
def multiple_question(question, choice, first_correct, second_correct, correct_message, wrong_message):
    '''
        Multiple question setup, It will ask for a question, and two maybe answers as well two correct answers and wrong message.
    '''
    print(question)
    choice = input(choice)
    if choice.lower() == first_correct or choice.lower() == second_correct:
        print(correct_message)
        correct_question("Correct")
    else:
        print(wrong_message)    
        wrong_question("Wrong")
        
        
def true_false_question(question, first_correct, second_correct, correct_message, wrong_message):
    '''
    True and false question setup. It will ask if the question is true or false.
    '''
    print(question)
    choice = input(":")
    if choice.lower() == first_correct or choice.lower() == second_correct:
        print(correct_message)
        correct_question("Correct")
    else:
        print(wrong_message)    
        wrong_question("Wrong")

def written_questions(question, ):


if __name__ == '__main__':
# Defining Score variables

    


    # Question One 
    question1 = "What is 1 + 1"
    maybeanswer1 = "a)1\nb)2\nc)3\nd)4\n:"
    correctanswer1 = "b"
    correctanswer2 = "2"
    wrongmessage = "Incorrect, 1 + 1 is 2"
    correctmessage = "Test"
    multiple_question(question1, maybeanswer1, correctanswer1, correctanswer2, correctmessage, wrongmessage)

    question1_3 = "True or False... The Toronto Maple Leafs have won 13 Stanley Cups?"
    correctanswer1_3 = "true"
    correctanswer2_3 = "t"
    wrongmessage_3 = "Incorrect, 1 + 1 is 2"
    correctmessage_3 = "Test"
    true_false_question(question1_3, correctanswer1_3, correctanswer2_3, correctmessage_3, wrongmessage_3)

# Total Score

    Test = float(scoreboard / 5) * 100
    print(scoreboard, "out of 5, that is", Test, "%")
