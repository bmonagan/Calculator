from calculations import calculate, append_digit
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Calculator")
    
    # Create and configure the main frame with padding
    frm = tk.Frame(root, padx=10, pady=10)
    frm.grid()
    
    # Secondary and main display variables and labels
    secondary_number = tk.StringVar()
    secondary_label = tk.Label(frm, textvariable=secondary_number, font=('Arial', 12), anchor='e', width=12)
    secondary_label.grid(column=0, row=0, columnspan=3, padx=5, sticky='ew')
    secondary_number.set("")

    current_number = tk.StringVar()
    label = tk.Label(frm, textvariable=current_number, font=('Arial', 24), anchor='e', width=12)
    label.grid(column=0, row=1, columnspan=3, padx=5, pady=10, sticky='ew')
    current_number.set("0")
    
    # Create number buttons in a grid (calculator layout)
    buttons = [
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2),
        ('0', 6, 1)
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
        ('<x|', 2, 0), ('AC', 2, 1), ('-', 2, 2),
        ('/', 3,   3), ('x', 4, 3 ), ('+', 5, 3),
        
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
