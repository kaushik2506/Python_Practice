def take_input():
    # nested dictionary to be used for quote name, error and person name, errors
    input_dict = {
        "quote": {
            "name": "What is the quote: ",
            "error_message": "Please enter quote/something"
        },
        "person": {
            "name": "Who said it: ",
            "error_message": "Please enter person/ something"
        }
    }

    # this while loop is only for input_quote
    while(True):
        print(" ")
        # this variable gets the value of quote from the nested dictionary
        input_quote = input(input_dict["quote"]["name"])
        if len(input_quote) == 0:
            print(" ")
            print(input_dict["quote"]["error_message"])
            print(" ")
            continue
        else:
            # this while loop is only for input_person
            while(True):
                # this variable gets the value of person who said that quote from the nested dictionary
                input_person = input(input_dict["person"]["name"])
                if len(input_person) == 0:
                    print(" ")
                    print(input_dict["person"]["error_message"])
                    print(" ")
                    continue
                break
        break
    # here, we return a list with two values
    return input_quote, input_person


# The expression func() means "call the function assigned to the variable func."
# For more details, refer --> https://realpython.com/primer-on-python-decorators/

def print_quotes(func):
    input_quote, input_person = func()
    print(" ")
    print(input_person + ' says, \"'+input_quote + '\".')


# this function takes two values that is returned from the list....Here, take_input is a helper function
print_quotes(take_input)
