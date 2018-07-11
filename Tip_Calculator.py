# tip calculator
from tkinter import *

# calculates the tip amount
def tip_amount(total, percentage):
    total = int(total)
    percentage = int(percentage)
    tip = total * (percentage / 100.0)
    tip_amount_label = Label(frame, text="tip amount is $" + str(tip)).pack()
    return "$" + str(tip)


# function added to use in enter_button for redirecting to tip_amount
# This also takes care of the invalid input case
def read_values():
    while 1==1:
        if str(total_amount.get()).isdigit() and str(tip_percent.get()).isdigit():
            break
        else:
            # gives a message to the user to enter a valid entry
            invalid_label = Label(frame, text="Invalid input...Please enter a number only").pack()
            return "invalid input"  # breaks out of the function
    # takes the entries to the tip_amount function to get the final tip amount
    print (tip_amount(total_amount.get(), tip_percent.get()))


frame = Tk()
total_amount = StringVar()
tip_percent = StringVar()
frame.geometry("500x500")
frame.title("Tip Calculator")
total_label = Label(frame, text="Final amount").pack()
total_textbox = Entry(frame, textvariable=total_amount).pack()
tip_label = Label(frame, text="Tip percentage %").pack()
tip_textbox = Entry(frame, textvariable=tip_percent).pack()
# For button, another function "read_values" was created which redirected to the function "tip_amount" because ...
# command could only take a function without "()" or a function without any arguments
enter_button = Button(frame, text="Enter", command=read_values, fg="white", bg="black").pack()
frame.mainloop()