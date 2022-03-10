'''
Created on Mar 9, 2022

@author: 1526331
'''
def multiple_question(question, maybeanswer1, correctanswer1, correctanswer2, correctmessage, wrongmessage, scoreboard):
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
        
def true_false_question(question, correctanswer1, correctanswer2, correctmessage, wrongmessage, scoreboard):
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
        
#if __name__ == '__main__':
    # Defining Score variables 
x = 0
score = x

# Question One 
question1 = "What is 1 + 1"
maybeanswer1 = "a)1\nb)2\nc)3\nd)4\n:"
correctanswer1 = "b"
correctanswer2 = "2"
wrongmessage= "Incorrect, 1 + 1 is 2"
correctmessage = "Test"
multiple_question(question1, maybeanswer1, correctanswer1, correctanswer2, correctmessage, wrongmessage, score)


question1_3 = "True or False... The Toronto Maple Leafs have won 13 Stanley Cups?"
correctanswer1_3  = "true"
correctanswer2_3  = "t"
wrongmessage_3 = "Incorrect, 1 + 1 is 2"
correctmessage_3  = "Test"
true_false_question(question1_3, correctanswer1_3, correctanswer2_3, correctmessage_3, wrongmessage_3, score)



#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")