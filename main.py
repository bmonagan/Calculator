from calculations import calculate, append_digit
import tkinter as tk


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
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('0', 5, 1)
    ]
    
    for (digit, row, col) in buttons:
        tk.Button(
            frm, 
            text=digit,
            width=5,
            height=2,
            command=lambda d=digit: append_digit(current_number, d)
        ).grid(row=row, column=col, padx=2, pady=2)
    
    function_buttons = [
        ('<x|', 1, 0), ('AC', 1, 1), ('-', 1, 2),
        ('/', 2,   3), ('x', 3, 3 ), ('+', 4, 3),
        
    ]
    for (digit, row, col) in function_buttons:
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
