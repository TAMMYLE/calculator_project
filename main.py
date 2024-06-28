from itertools import chain
from art import logo



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

# Calculate another number:

# Para: result: result of previous calculation and user_choice: the operation that user have chose

def third_num_cal(result, user_choice):
    num3 = int(input("Enter your third num: "))
    second_result = arithmetic_operations[user_choice](result, num3)
    print(f"the result of this calculation is {result} {user_choice} {num3} = {second_result}")

# Function LAST ENQUIRY
def last_enquiry_func():
    my_enquiry = input("You want to try this again? Type yes(Yes) or no(Exit)\n").lower()

    return my_enquiry

# Decoration Chain
def deco_chain():
    chain = ""

    chain_range = range(1,20)

    for i in chain_range:
        chain = chain + "~"
    
    print(chain)
# Create a Dictionary that store these above functions
## TRICK: use the value of a variable to connect to a funnction

arithmetic_operations = {}

arithmetic_operations["+"] = add
arithmetic_operations["-"] = subtract
arithmetic_operations["*"] = multiply
arithmetic_operations["/"] = divide

# to retrieve a function in the dictionary --- > arithmetic_operations['+']()

## Better Task: Create a loop asking if user STiLL wants to use the calculator?

### SCENARIOS:

## 1: User can start THE WHOLE PROGRAM again
## 2: User can start again WITH ANOTHER NUMBER (num3) but SAME OPERATION
## 3: User can EXIT the program


# 1st Scenario: start THE WHOLE PROGRAM again
### when start_again is still FALSE --> run the loop, user chooses to NO to exit --> start_again changes to TRUE --> end program
start_again = False

# next_num_cal : is a trigger ONLY happened after third_num_cal function is called. Its initial condition is FALSE --> loop will end when user choose to exit or all, next_num_cal changes to TRUE
next_num_cal = False

while not start_again:

    num1 = int(input("Choose your first number: \n"))
    num2 = int(input("Choose your second number: \n"))

    # Print Decoration chain

    deco_chain()

    # Print out list of operations 

    for op in arithmetic_operations:
        print(op)

    # Print Decoration chain

    deco_chain()

    # Let user choose --> Print out their choice
    user_choice = input("Pick one of the above arithmetic operations please ^^.\n")


    # Present the result of 2 nums based on the chosen operation

    result = arithmetic_operations[user_choice](num1, num2)

    print(f"The result is: \n {num1} {user_choice} {num2} = {result}")

    

    while not next_num_cal:

        # Last enquiry: set a last question to confirm if user wants to use the calculator again or not

        my_enquiry = input("You want to try this again? Type yes(Yes) or no(Exit)\n").lower()


        if my_enquiry == "yes":

            # user choose to start the whole program again or exit -- > ask them if they want to start the whole thing or choose another number
            sub_last_enquiry = input("Would you like to start all over or choose a next number? Type all(ALL OVER AGAIN) or next(NEXT NUMBER)\n").lower()

            if sub_last_enquiry == "all":
                start_again = False
                next_num_cal = True
            elif sub_last_enquiry == "next":
                third_num_cal(result, user_choice)
                start_again = False
                next_num_cal = False  

        else:
            print("GoodBye")
            start_again = True
            next_num_cal = True





    







