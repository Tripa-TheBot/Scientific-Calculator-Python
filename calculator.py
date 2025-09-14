# Ask the user's name
name = print("What's your name? ")  # print() displays something on the screen, but here it only prints, does not store
name = input()  # input() reads what the user types and stores it in the variable 'name'

# Greeting using f-string
print(f"Hello {name}, welcome to the calculator!")  
# f-string allows you to insert variable values inside strings: {name}

# Pi constant
P = 3.141592653589793  # approximate Pi number

# List to store the history of operations
history = []  # [] creates an empty list

# Function definition to read numbers
def read_number(message):  # def defines a function called 'read_number' that receives a parameter 'message'
    while True:  # infinite loop that only ends with 'return' (or break)
        value = input(message)  # reads the user's input
        if value.strip().upper() == "P":  
            # .strip() removes spaces before/after
            # .upper() transforms everything to uppercase
            return P  # return gives the value P to whoever called the function
        try:  
            # try tries to execute something that may fail
            return float(value)  # converts the typed string to a decimal number
        except ValueError:  
            # except catches the specific 'ValueError' (when the conversion fails)
            print(f"{name}, invalid value! Try again.")  

# Function to show the operations menu
def show_menu():  
    print(
        "\nChoose the desired operation:\n"
        "1) + for addition\n"
        "2) - for subtraction\n"
        "3) * for multiplication\n"
        "4) / for division\n"
        "5) r for root\n"
        "6) % for remainder\n"
        "7) // for integer division\n"
    )

# Function to calculate the operations
def calculate(x, operation, y):  
    if operation == "+":  
        z = x + y  # addition operator
        print(f"{name}, the sum of {x} + {y} is {z}")
    elif operation == "-":  
        z = x - y  # subtraction
        print(f"{name}, the subtraction of {x} - {y} is {z}")
    elif operation == "*":  
        z = x * y  # multiplication
        print(f"{name}, the multiplication of {x} * {y} is {z}")
    elif operation == "/":  
        if y == 0:  
            # Checks division by zero
            print(f"{name}, it's not possible to divide by zero!")
            return None  # return None indicates that there is no valid result
        z = x / y  # normal division
        print(f"{name}, the division of {x} / {y} is {z}")
    elif operation == "r":  
        if y == 0:  
            print(f"{name}, it's not possible to calculate root with index zero!")
            return None
        z = x ** (1/y)  # y-th root of x
        print(f"{name}, the {y} root of {x} is {z}")  
    elif operation == "%":  
        z = x % y  # remainder of division
        print(f"{name}, the remainder of {x} % {y} is {z}")
    elif operation == "//":  
        z = x // y  # integer division
        print(f"{name}, the integer division of {x} // {y} is {z}")    
    else:
        print(f"Sorry {name}. But, the operation is invalid!")
        return None
    history.append(f"{x} {operation} {y} = {z}")  
    # adds the performed operation to the 'history' list
    return z  # returns the result of the operation

# Main program loop
while True:  
    x = read_number("Enter the first number (or P for Pi): ")  # calls function to read number
    show_menu()  # shows operations menu
    operation = input("Enter the symbol of the operation you want to perform: ")  # reads operation
    y = read_number("Enter the second number (or P for Pi): ")  # reads second number

    z = calculate(x, operation, y)  # calculates and stores result

    if z is not None:  # if valid result
        see_hist = input("Do you want to see the operation history? (y/n): ").lower()  
        # .lower() transforms to lowercase
        if see_hist == "y":
            print("Operation history:")
            print("\n".join(history))  
            # "\n".join(list) joins all elements of the list with line breaks

    while z is not None:  # loop to continue with previous result
        add_more = input("Do you want to add another operation to the result? (y/n): ").lower()
        if add_more == "y":
            x = z  # uses previous result as new x
            show_menu()
            operation = input("Enter the symbol of the operation you want to perform: ")
            y = read_number("Enter the second number (or P for Pi): ")
            z = calculate(x, operation, y)
            if z is not None:
                see_hist = input("Do you want to see the operation history? (y/n): ").lower()
                if see_hist == "y":
                    print("Operation history:")
                    print("\n".join(history))
        else:
            break  # exits the loop if you don't want to continue

    repeat = input("Do you want to make a new calculation? (y/n) (n will close the program!): ").lower()
    if repeat != "y":  # if you don't type 'y', it ends
        print(f"Thank you, {name}, for using Tripa's calculator <3!")
        break  # ends the main loop, closing the program
