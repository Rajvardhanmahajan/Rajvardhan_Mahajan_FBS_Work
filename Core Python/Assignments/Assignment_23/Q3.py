# Import Tkinter library
import tkinter as tk


# Function to perform calculation
def calculate():

    # Get first number from entry box
    num1 = float(first_entry.get())

    # Get second number from entry box
    num2 = float(second_entry.get())

    # Get operator from entry box
    operator = operator_entry.get()

    # Perform addition
    if operator == "+":
        result = num1 + num2

    # Perform subtraction
    elif operator == "-":
        result = num1 - num2

    # Perform multiplication
    elif operator == "*":
        result = num1 * num2

    # Perform division
    elif operator == "/":
        result = num1 / num2

    # Handle invalid operator
    else:
        result = "Invalid Operator"

    # Display result in result label
    result_label.config(text=f"Result = {result}")


# Create the main window
window = tk.Tk()

# Set window title
window.title("Basic Calculator")

# Set window size
window.geometry("300x300")


# Create First Number label
tk.Label(window, text="First Number").pack(pady=5)

# Create entry box for first number
first_entry = tk.Entry(window)
first_entry.pack()


# Create Second Number label
tk.Label(window, text="Second Number").pack(pady=5)

# Create entry box for second number
second_entry = tk.Entry(window)
second_entry.pack()


# Create Operator label
tk.Label(window, text="Operator (+, -, *, /)").pack(pady=5)

# Create entry box for operator
operator_entry = tk.Entry(window)
operator_entry.pack()


# Create Calculate button
# command=calculate calls calculate() when button is clicked
tk.Button(
    window,
    text="Calculate",
    command=calculate
).pack(pady=15)


# Create label to display result
result_label = tk.Label(window, text="Result = ")
result_label.pack()


# Keep the GUI window running
window.mainloop()