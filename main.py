# Mental Arithmetic Master is a program written in Tkinter (Python). This code creates a window with a welcome
# message and two labels. The labels are blank and will later be updated with the math problem and the answer. It
# then creates two buttons: one to display the answer, and one to generate a new math problem. The generate function
# assigns two numbers and a sign at random, and depending on the sign assigns either addition or subtraction as the
# problem. It also sets the global variable answer to the correct answer for that problem. Finally, it displays the
# window.
import tkinter as tk
from random import randint

# Initialize window
root = tk.Tk()
root.title("Mental Arithmetic Master")

# Set background color
root.configure(background='#3D3F41')

# Establish font
my_font = ('Ariel', 24)

# Create welcome message
message = tk.Label(root, text="Welcome to Mental Arithmetic Master", font=my_font, background="#3D3F41")
message.grid(row=0, column=0, columnspan=2)

# Create answers
answer1 = tk.Label(root, font=my_font, background="#3D3F41")
answer1.grid(row=1, column=0, columnspan=2)

answer2 = tk.Label(root, font=my_font, background="#3D3F41")
answer2.grid(row=2, column=0, columnspan=2)

# Create a function to generate the problem
answer = 0


def generate():
    global answer
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    op = randint(1, 2)
    if op == 1:
        answer1.configure(text=str(n1) + "+" + str(n2) + "=___")
        answer = n1 + n2
    elif op == 2:
        answer1.configure(text=str(n1) + "-" + str(n2) + "=___")
        answer = n1 - n2


# Create Answer Button
answer_button = tk.Button(root, text="Answer", font=my_font, background="#3D3F41",
                          command=lambda: answer2.configure(text="Answer: " + str(answer)))
answer_button.grid(row=3, column=0, columnspan=2)

# Create New Problem Button
new_problem_button = tk.Button(root, text="New Problem", font=my_font, background="#3D3F41",
                               command=generate)
new_problem_button.grid(row=4, column=0, columnspan=2)

# Display the window
root.mainloop()
