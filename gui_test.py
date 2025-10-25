import tkinter as tk
# Create main window
window = tk.Tk()
window.title("Basic GUI Example")
window.geometry("300x200")
# Add widgets
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)
entry = tk.Entry(window, width=20)
entry.pack(pady=5)
def on_button_click():
   user_input = entry.get()
   label.config(text=f"Welcome, {user_input}!")
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack(pady=10)
# Run the application
window.mainloop()