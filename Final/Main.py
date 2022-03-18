#import
import random

#global variables
scoreboard = 0
question_counter = 0

#dictorary list
multiple_question_list = {
        1: {
            "question": "1) What is 1 + 1: \na)1\nb)2\nc)3\nd)4\n",
            "answer_1": "b",
            "answer_2": "2"
        },
        2: {
            "question": "2) What is 36 + 90: \na)3\nb)128\nc)389\nd)126\n",
            "answer_1": "d",
            "answer_2": "126"

        },
        3: {
            "question": "3) What is (202 / 4) - 69:  \na)3242\nb)133\nc)389\nd)126\n",
            "answer_1": "b",
            "answer_2": "133"
        },
        4: {
            "question": "4) There are 49 dogs signed up for a dog show. There are 36 more small dogs than large dogs. How many small dogs have signed up to compete?:    \na)34.7\nb)42.5\nc)3.6\nd)12.8\n",
            "answer_1": "b",
            "answer_2": "42.5"
        },
        5: {
            "question": "5) Add 8.563 and 4.8292.:   \na)13,394\nb)1.345\nc)27.123\nd)13.3922",
            "answer_1": "d",
            "answer_2": "13.3922"
        }
}

true_false_question_list = {
        1: {
            "question": "6) True or False... The Toronto Maple Leafs have won 13 Stanley Cups?",
            "answer_1": "true",
            "answer_2": "t"
        },
        2: {
            "question": "7) True or False...  Electrons move faster than the speed of light.",
            "answer_1": "false",
            "answer_2": "f"
        },
        3: {
            "question": "8) True or False... Light travels in a straight line.",
            "answer_1": "true",
            "answer_2": "t"
        },
        4: {
            "question": "9) True or False.... The Mona Liza was stolen from the Louvre in 1911.",
            "answer_1": "true",
            "answer_2": "t"
        }
}

written_question_list = {
        1: {
            "question": "10) The word starts with an A and ends with an E",
            "answer": "apple"
        },
        2: {
            "question": "11) Who is often called the father of the computer?",
            "answer": "charles babbage"
        },
        3: {
            "question": "12) What does “HTTP” stand for?",
            "answer": "hyper text transfer protocol"
        }
}

correct_message_list = {
        1: "Good Job! \n"
}

wrong_message_list = {
        1: "Better next time :( \n"
}
#import
def introduce_message():
    print('''Welcome to the test applcation! You will be asked alot of questions from different areas of your knowlege!
    There will be a total of 12 question you will have to answer!''')
    input("Press Enter!")
    return True
    
def multiple_question(question, choice):
    '''
        Multiple question setup, It will ask for a question, and two maybe answers as well two correct answers and wrong message.
    '''
    # adding to the
    global question_counter
    question_counter += 1


    if multiple_question_list[question]['answer_1'] == choice.lower() or multiple_question_list[question]['answer_2'] == choice:
        #randomize some cool correct message
        random.shuffle(correct_message_list.keys())
        for key in correct_message_list:
            print(correct_message_list[key])
        #addes the to the global scoreboard
        global scoreboard
        scoreboard += 1
        return True
    else:
        # randomize some cool wrong message
        random.shuffle(wrong_message_list.keys())
        for key in wrong_message_list:
            print(wrong_message_list[key])
        return False
        
def true_false_question(question, choice):
    '''
    True and false question setup. It will ask if the question is true or false.
    '''
    global question_counter
    question_counter += 1

    if true_false_question_list[question]['answer_1'] == choice.lower() or true_false_question_list[question]['answer_2'] == choice:
        # randomize some cool correct message
        random.shuffle(correct_message_list.keys())
        for key in correct_message_list:
            print(correct_message_list[key])
        # addes the to the global scoreboard
        global scoreboard
        scoreboard += 1
        return True
    else:
        # randomize some cool wrong message
        random.shuffle(wrong_message_list.keys())
        for key in wrong_message_list:
            print(wrong_message_list[key])
        return False

def written_questions(question, choice):
    '''
    Just written question: short or long answers
    '''
    global question_counter
    question_counter += 1

    if written_question_list[question]['answer'] == choice.lower():
        # randomize some cool correct message
        random.shuffle(correct_message_list.keys())
        for key in correct_message_list:
            print(correct_message_list[key])
        # addes the to the global scoreboard
        global scoreboard
        scoreboard += 1
        return True
    else:
        # randomize some cool wrong message
        random.shuffle(wrong_message_list.keys())
        for key in wrong_message_list:
            print(wrong_message_list[key])
        return False





if __name__ == '__main__':
    introduce_message()
    while True:
        counter = 0
        for counter in multiple_question_list:
            print(multiple_question_list[counter]['question'])
            choice = input("Enter answer: ")
            multiple_question(counter, choice)
        for counter in true_false_question_list:
            print(true_false_question_list[counter]['question'])
            choice = input("Enter answer: ")
            true_false_question(counter, choice)
        for counter in written_question_list:
            print(written_question_list[counter]['question'])
            choice = input("Enter answer: ")
            written_questions(counter, choice)
        break



    Test = float(scoreboard / question_counter) * 100
    print(f"{scoreboard}, out of {question_counter}, that is {Test}%")
