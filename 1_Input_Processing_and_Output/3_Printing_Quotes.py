def take_input():
    input_dict = {
        "quote": "What is the quote: ",
        "person": "Who said it: "
        }

    while(True):
        print(" ")
        input_quote = input(input_dict.get("quote"))
        if len(input_quote) == 0:
            print(" ")
            print("Please enter quote/something")
            print(" ")
            continue
        else:
            while(True):
                input_person = input(input_dict.get("person"))
                if len(input_person) == 0:
                    print(" ")
                    print("Please enter person/ something")
                    print(" ")
                    continue
                break
        break
    return [input_quote, input_person];


def print_quotes(input_quote, input_person):
    print(" ")
    print(input_person + ' says, \"'+input_quote + '\".')


returned_value = take_input()
print_quotes(returned_value[0], returned_value[1])


