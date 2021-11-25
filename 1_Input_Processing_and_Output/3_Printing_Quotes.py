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
    return [input_quote, input_person]


def print_quotes(input_quote, input_person):
    print(" ")
    print(input_person + ' says, \"'+input_quote + '\".')


# here, we store the values the returned function in the variable
returned_value = take_input()
# this function takes two values that is returned from the list
print_quotes(returned_value[0], returned_value[1])
