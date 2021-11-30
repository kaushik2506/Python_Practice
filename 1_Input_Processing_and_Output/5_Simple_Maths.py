def num_user_input(value):
    print(" ")
    while True:
        number = input(f'Enter your {value} Number: ')
        try:
            number = int(number)
        except:
            print(" ")
            print("xxxxxx--Please enter only digits--xxxxxx")
            print(" ")
            continue
        if number < 1:
            print(" ")
            print("xxxxxx--Only Positive Numbers Allowed--xxxxxx")
            print(" ")
            continue
        break
    return number


def simple_maths():
    num1 = num_user_input("1st")
    num2 = num_user_input("2nd")
    print(" ")
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')


simple_maths()
