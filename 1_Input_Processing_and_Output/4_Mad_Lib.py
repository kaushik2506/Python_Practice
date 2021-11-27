def take_input():
    # nested dictionary
    user_input_dict = {
        "noun": {
            "input": "Enter a noun: ",
            "error_message": "Please enter a noun"
        },
        "verb": {
            "input": "Enter a verb: ",
            "error_message": "Please enter a verb"
        },
        "adjective": {
            "input": "Enter an adjective: ",
            "error_message": "Please enter an adjective"
        },
        "adverb": {
            "input": "Enter an adverb: ",
            "error_message": "Please enter an adverb"
        }
    }

    # list for storing the values orderwise --> noun, verb, adjective, adverb
    user_input_values = []

    # this for loop removes redundancy by taking in values from the nested dictionary
    for value in user_input_dict:
        while(True):
            print(" ")
            user_input = input(user_input_dict[value]["input"])
            if len(user_input) == 0:
                print(" ")
                print(user_input_dict[value]["error_message"])
                continue
            # appending the values that has been inputted by the user
            user_input_values.append(user_input)
            break
    # return the values as a list
    return user_input_values


def print_paragraph(func):
    user_input_values = func()
    #user_input_values_new = list(map(lambda x: x, user_input_values))
    print(" ")
    print(
        f"Do you {user_input_values[1]} your {user_input_values[2]} {user_input_values[0]} {user_input_values[3]}? That's hilarious!")


# first function takes a list as a parameter from the take_input function...Here, take_input is a helper function
print_paragraph(take_input)