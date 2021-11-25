def take_input():
    # dictionary to be used for input quote and person
    input_dict = {
        "quote": "What is the quote: ",
        "person": "Who said it: "
    }

    # this while loop is only for input_quote
    while(True):
        print(" ")
        # this variable calls the dictionary method to get the value of quote
        input_quote = input(input_dict.get("quote"))
        if len(input_quote) == 0:
            print(" ")
            print("Please enter quote/something")
            print(" ")
            continue
        else:
            # this while loop is only for input_person
            while(True):
                # this variable calls the dictionary method to get the value of person who said that quote
                input_person = input(input_dict.get("person"))
                if len(input_person) == 0:
                    print(" ")
                    print("Please enter person/ something")
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
