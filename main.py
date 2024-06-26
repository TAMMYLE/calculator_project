from art import logo

print(logo)

# Basis Calculator takes 2 inputs

# Add Func
def add(n1, n2):
    return n1 + n2

# Subtract Func
def subtract(n1, n2):
    return n1 - n2

# Multiply Func
def multiply(n1, n2):
    return n1 * n2

# Divide Func
def divide(n1, n2):
    return n1 / n2


# Create a Dictionary that store these above functions
## TRICK: use the value of a variable to connect to a funnction

arithmetic_operations = {}

arithmetic_operations["+"] = add
arithmetic_operations["-"] = subtract
arithmetic_operations["*"] = multiply
arithmetic_operations["/"] = divide

# to retrieve a function in the dictionary --- > arithmetic_operations['+']()

## Better Task: Create a loop asking if user STiLL wants to use the calculator?

start_again = False


while not start_again:

    num1 = int(input("Choose your first number: \n"))
    num2 = int(input("Choose your second number: \n"))

    # Print out list of operations 

    for op in arithmetic_operations:
        print(op)

    # Let user choose --> Print out their choice
    user_choice = input("Pick one of the above arithmetic operations please ^^.\n")

    print(f"You have chosen {user_choice}.")

    # Present the result of 2 nums based on the chosen operation

    result = arithmetic_operations[user_choice](num1, num2)

    print(f"The result is: \n {num1} {user_choice} {num2} = {result}.")

    # Last enquiry: set a last question to confirm if user wants to use the calculator again or not

    last_enquiry = input("You want to try this again? Type yes(Yes) or no(Exit)\n").lower()

    if last_enquiry == "yes":
        start_again = False
    elif last_enquiry == "no":
        print("GoodBye")
        start_again = True





    







