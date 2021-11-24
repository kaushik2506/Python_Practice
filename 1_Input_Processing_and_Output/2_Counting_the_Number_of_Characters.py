# takes user input and return its value only if the user has entered atleast 1 character
def take_input():
    while(True):
        print(" ")
        input_string = input('What is the input string: ')
        if len(input_string) == 0:
            print(" ")
            print("Please enter something")
            continue
        else:
            return input_string
            print(" ")
        break


# displays output that shows the input string and the number of characters the string contains.
def count_chars(input_string):
    print(" ")
    print(f"{input_string} has {len(input_string)} characters.")
    # print(f"{input_string} has {len(list(input_string))} characters.")  using list --> it break downs the string to individual chars


# first call take_input function and then pass the value to count_chars function
count_chars(take_input())
