
# String Integers Bool Float 

# Functions 
#greet() # not going to work because function greet does not exist

# function with no arguments 
def greet(name):
    print(f"Hello {name}!")

# calling the greet function 
#greet("Mary") 

#my_name = input("Enter your name: ")
#print(my_name) 

# adding two numbers 
#first_number = input("Enter first number: ")
#second_number = input("Enter second number: ")

# sssasdasdsadasdasdasd 

# 3.75 

# "34" + "6" = "346"
# 34 + 6

#result = float(first_number) + float(second_number) 
#print(result)

# Activity: 
# ask the user for two inputs for dollar amount
# add them together and then print them on screen 
# 23.45 + 12.75 = 36.20

# SRP Single Responsiblity Principle    s 
def calculate_tip(total_cost, percentage):
    tip = total_cost * (percentage/100)
    
    return tip
    # code after the return statement is NEVER executed 
    
# this is calculate tip function 
tip = calculate_tip(100,2)
print(tip)

if tip >= 10:
    print("YOU ARE VERY GENEROUS")
elif tip < 10 and tip >= 5: 
    print("THANKS")
else: 
    print("YOU ARE BAD TIPPER!")

## Conditions



    



