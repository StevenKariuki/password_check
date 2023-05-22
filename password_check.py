# Python Password Checker:
# At least 8 characters
# have a lower case
# Have an Uppercase
# HAve a digit
# Have a symbole.g $$ @

# Regular expretions :used to check for patters in values

import re

def checkPassword(password):
    if (len(password) < 8 ):
        print("Password should have at least 8 characters!!!")
        print("Try Again!!!!")

    if not re.search("[a-z]", password):
        print("Should have a Lowercase value ")    
        print("Try Agin!!!")
        
    elif not re.search("[A_Z]",password):
        print("Should have an Uppercase")
        print("Try Again")

    elif not re.search("[0-9]"):
        print("Should have a Digit")
        print("Try Again")

    elif not re.search("[#@$_!&*]", password):
        print("Should have a symbols")
        print("Try Again")


    else:
        print("OK")
        print("=====PROCEED TO SAVE")


while True:
    checkPassword(input("Enter Your Password:  "))        



