#•	Design Counter App (This app has a button that increments a counter displayed on the screen every time the button is clicked)

import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Counter App")
root.geometry("250x150")

# Initialize counter variable
counter = tk.IntVar(value=0)

# Function to increment the counter
def increment():
    counter.set(counter.get() + 1)

# Label to display the counter
label = tk.Label(root, textvariable=counter, font=("Helvetica", 32))
label.pack(pady=20)

# Button to increase counter
button = tk.Button(root, text="Click Me", command=increment, font=("Helvetica", 14))
button.pack()

# Start the Tkinter loop
root.mainloop()

#•Text Input App (This app allows users to type in a text field and display the typed text on the screen when a button is pressed.)

import tkinter as tk

def display_text():
    user_input = entry.get()        # Get text from input field
    label.config(text=user_input)   # Display it on the label

# Create main window
root = tk.Tk()
root.title("Text Input App")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Display Text", command=display_text)
button.pack(pady=5)

# Label to show text
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
