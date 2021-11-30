import datetime

def takeInput():
    questions = ["What is your current age: ", "At what age would you like to retire: "]
    answers = []
    for question in questions:
        while True:
            print(" ")
            user_input = input(question)
            try:
                user_input = int(user_input)
            except:
                print(" ")
                print("xxxxxx--Please enter only digit--xxxxxx")
                continue
            if user_input < 1:
                print(" ")
                print("xxxxxx--Only Positive Numbers Allowed--xxxxxx")
                continue
            break
        #appending the values to the answers list
        answers.append(user_input)
    #return the answers list
    return answers



def retirement_calculator(func):
    answers = func()
    #current datetime
    currentDatetime = datetime.datetime.now()
    #current year converted to integer
    currentYear = int(currentDatetime.strftime('%Y'))
    #difference between the two values provide by the user
    diff = answers[1] - answers[0]
    if diff <= 0:
        print(" ")
        print("You can already retire.")
    else:
        print(" ")
        print(f"It's {currentYear}, so you can retire in {currentYear + diff}.")


#call the function
retirement_calculator(takeInput)
