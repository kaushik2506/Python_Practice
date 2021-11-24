#take user input and return its value
def take_input():
    return input('What is your name? ')

#greet user by the input that is returned by the above function
def greet_user(name):
    print(f"Hello, {name}, nice to meet you!")

print(" ")
#call the greet_user function that will first call the take_input function
greet_user(take_input())