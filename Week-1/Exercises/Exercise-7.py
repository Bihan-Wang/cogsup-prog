"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
import random
print("Think a number between 1 and 100, the computer will guess it.")
low = 1
high = 100 #set the initial limits
feedback = "" #to store users' feedback

while feedback != "correct": # when the answer is wrong
    guess = (low + high) // 2 #use the middle of the range
    print(f"{guess} is correct?")

    feedback = input("The answer is too high(enter 'h;), too low(enter 'l'), or is correct(enter 'correct')?") #ask the user to check

    if feedback == "correct":#when the answer is correct
        print(f"Yes, the number was indeed {guess}")
    elif feedback == "h": #when the answer is too high, adjust the high limit
        high = guess
    elif feedback == "l": #when the answer is too low, adjust the low limit
        low = guess 
    else:
        print("Please enter 'h','l' or 'correct'")