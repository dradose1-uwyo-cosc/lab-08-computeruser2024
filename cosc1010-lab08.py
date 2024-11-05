"""
Emma Leyba
UWYO COSC 1010
11-03-24
Lab 08
Lab Section: 14
Sources, people worked with, help given to:
your
comments
here"""

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_for_int_or_float(string_to_check): 
# Break the checks down and handle them individually
    returnValue = False
    try:
        returnValue = float(string_to_check)
        returnValue = int(string_to_check)
# num+ float(string_to check)
    except:
        pass
    return returnValue
    # print invalid num
    # return False
print(check_for_int_or_float("3.2"))

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, a, an): # a = 2, an = 5
    y_arr = []
    # Check if those values are legit
    
    
# def slope_intercept(m, b, a, an): # a = 2, an = 5
#     # Check if those values are legit
#     check_for_int_or_float(m) and
#     check_for_int_or_float(b) and
#     check_for_int_or_float(a) and
#     check_for_int_or_float(an):
#     y_arr = []
#     # Solve the equation for a to an, save into y_arr
    
    

    
# #         return y_arr
#    # else:
#    # print("(One or more of your numbers are invalid)


# while True:
#     a = input("Give me an a")
#     #.. 
#     if (a == "q"):
#         break
#     if (b == "q"):
    
#         if (a == "q"):
#     slope_intercept()

# print("*" * 75)

# if (a == "q"end);
#     break
# if (b == "q"):
#     break



# #-
# # Write a function to solve the quadratic formula
# # https://en.wikipedia.org/wiki/Quadratic_formula
# # Accept inputs for a, b, c
# # Remember that this returns two values
# # Create a loop like above to prompt the user for input for the three values
# # Create a second function that just does the square root operation 
#     # If the number you are trying to take the square root of is negative, return null
 