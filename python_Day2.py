# 012
# Ask for two numbers. If the first one is larger than the second,
# display the second number
# first and then the first number, 
# otherwise show the first number first and then the second.

# ## asking for two inputs and converting them to integer
# first_number = int(input("Enter your first number: "))

# second_number = int(input("Enter the second number: "))

# ## test for the condition and make a decision
# if (first_number > second_number):
#     print(second_number, first_number)
# else:
#     print(first_number, second_number)

# 013
# Ask the user to enter a number that is under 20. 
# If they enter a number that is 20 or more,
# display the message “Too high”, otherwise display “Thank you”.

# ## take an input from a user 
# user_input = int(input("Enter a number that is less than 20: "))

# ## check if the number is equal to or greater than 20
# if (user_input >= 20):
#     print("Too High")
# else:
#     print("Thank you")

# 014
# Ask the user to enter a number between 10 and 20 (inclusive).
# If they enter a number within
# this range, display the message “Thank you”, 
# otherwise display the message “Incorrect Answer”.

# user_input = int(input("Enter a number b/n 10 and 20: "))

# if ((user_input >= 10) and (user_input <= 20) ):
#     print("Thank you")
# else:
#     print("Incorrect Answer")


user_input = input("Enter a color: ")

if ((user_input == "Red") or (user_input == "RED") or (user_input == "red")):
    print("I like red too")
else:
    print("I dont like the color")