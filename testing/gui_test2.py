import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Updating Label Example")

# 1. Create a Tkinter variable to hold the label's text
current_text = tk.StringVar()
current_text.set("Starting...") # Initial value

# 2. Create the Label and link it to the StringVar
# The textvariable option is key for automatic updates
label = ttk.Label(root, textvariable=current_text, font=('Arial', 24))
label.pack(padx=20, pady=20)

# A simple counter variable for demonstration
counter = 0

# 3. Define the function to update the variable (and thus the label)
def update_label():
    global counter
    counter += 1
    
    # Update the StringVar's value
    current_text.set(f"Count: {counter}")
    
    # Schedule this function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_label) 

# Start the periodic update
# The .after() method is the standard way to schedule recurring tasks in Tkinter
root.after(1000, update_label) 

# Start the main event loop
root.mainloop()