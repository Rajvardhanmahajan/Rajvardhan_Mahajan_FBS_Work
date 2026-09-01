# Import Tkinter library
import tkinter as tk

# Import messagebox for displaying popup messages
from tkinter import messagebox


# Store quiz questions, options and correct answers
questions = [
    {
        "question": "Which language is used for Tkinter?",
        "options": ["Python", "Java", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "$"],
        "answer": "#"
    }
]

# Store the index of the current question
current_question = 0


# Function to display the current question and its options
def show_question():

    # Display the current question
    question_label.config(
        text=questions[current_question]["question"]
    )

    # Display all four options on the buttons
    for i in range(4):
        option_buttons[i].config(
            text=questions[current_question]["options"][i]
        )


# Function to check the selected answer
def check_answer(selected):

    # Get the correct answer of the current question
    correct_answer = questions[current_question]["answer"]

    # Check whether selected answer is correct
    if selected == correct_answer:
        messagebox.showinfo("Result", "Correct Answer! ✅")
    else:
        messagebox.showerror("Result", "Incorrect Answer! ❌")

    # Move to the next question
    next_question()


# Function to move to the next question
def next_question():

    # Use the global current_question variable
    global current_question

    # Increase the question number by 1
    current_question += 1

    # Check if more questions are available
    if current_question < len(questions):
        show_question()

    # If all questions are completed
    else:
        messagebox.showinfo("Quiz", "Quiz Completed!")

        # Close the quiz window
        window.destroy()


# Main Window
window = tk.Tk()

# Set the title of the window
window.title("Quiz Game")

# Set the size of the window
window.geometry("500x350")


# Question
question_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)

# Place the question label in the window
question_label.pack(pady=30)


# Create an empty list to store option buttons
option_buttons = []


# Create four option buttons
for i in range(4):

    # Create an option button
    button = tk.Button(
        window,
        width=25,

        # Call check_answer() when the button is clicked
        command=lambda i=i: check_answer(
            questions[current_question]["options"][i]
        )
    )

    # Place the button in the window
    button.pack(pady=5)

    # Add the button to the option_buttons list
    option_buttons.append(button)


# Display the first question
show_question()

# Keep the GUI window running
window.mainloop()