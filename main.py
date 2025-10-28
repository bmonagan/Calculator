from calculations import calculate
import tkinter as tk

def append_digit(current_number, digit):
    current = current_number.get()
    if current == "0":
        current_number.set(str(digit))
    else:
        current_number.set(current + str(digit))

def main():
    root = tk.Tk()
    root.title("Calculator")
    
    # Create and configure the main frame with padding
    frm = tk.Frame(root, padx=10, pady=10)
    frm.grid()
    
    # Display variable and label
    current_number = tk.StringVar()
    label = tk.Label(frm, textvariable=current_number, font=('Arial', 24), anchor='e', width=12)
    label.grid(column=0, row=0, columnspan=3, padx=5, pady=10, sticky='ew')
    current_number.set("0")
    
    # Create number buttons in a grid (calculator layout)
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 1)
    ]
    
    for (digit, row, col) in buttons:
        tk.Button(
            frm, 
            text=digit,
            width=5,
            height=2,
            command=lambda d=digit: append_digit(current_number, d)
        ).grid(row=row, column=col, padx=2, pady=2)

    root.mainloop()

if __name__ == "__main__":
    main()
