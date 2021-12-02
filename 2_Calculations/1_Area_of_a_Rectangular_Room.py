print(" ")
print("Area of a Rectangular Room")
print("------------------------------")
print(" ")


# this function prompts user to choose between feet or meters
def userInputUnit():
    while True:
        print(" ")
        print("Press 1 to register your input in feet \nPress 2 to register your input in meter")
        print(" ")
        user_input_unit = input("Enter 1 or 2: ")
        try:
            user_input_unit = int(user_input_unit)
        except:
            print(" ")
            print("xxxxxx--Please enter only digit--xxxxxx")
            continue
        if user_input_unit not in [1, 2]:
            print(" ")
            print("xxxxxx--Please choose from 1 or 2--xxxxxx")
            continue
        if user_input_unit < 1:
            print(" ")
            print("xxxxxx--Only Positive Value Allowed--xxxxxx")
            continue
        break
    return user_input_unit


# this function takes dimension value and the unit and return the value of the unit
def user_input_dimensions(dimensions, unit):
    print(" ")
    while True:
        user_input = input(f'What is the {dimensions} of the room in {unit}: ')
        try:
            user_input = int(user_input)
        except:
            print(" ")
            print("xxxxxx--Please enter only digits--xxxxxx")
            print(" ")
            continue
        if user_input < 1:
            print(" ")
            print("xxxxxx--Only Positive Numbers Allowed--xxxxxx")
            print(" ")
            continue
        break
    return user_input


# main function
def areaCalculator(value):
    if value == 1:
        length = user_input_dimensions("length", "feets")
        width = user_input_dimensions("width", "feets")
        area = length * width
        print(" ")
        print(
            f"The area is: \n{area} square feet\n{area * 0.09290304} square meters")
    elif value == 2:
        length = user_input_dimensions("length", "meters")
        width = user_input_dimensions("width", "meters")
        area = length * width
        print(" ")
        print(
            f"The area of your room is: \n{area} square meters\n{area / 0.09290304} square feet")


# calling the final function
areaCalculator(userInputUnit())
