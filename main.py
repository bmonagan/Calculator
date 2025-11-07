import calculations
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Calculator")
    
    # Create and configure the main frame with padding
    frm = tk.Frame(root, padx=10, pady=10)
    frm.grid()
    
    # Secondary and main display variables and labels
    current_number = tk.StringVar()
    label = tk.Label(frm, textvariable=current_number, font=('Arial', 24), anchor='e', width=12)
    label.grid(column=0, row=1, columnspan=4, padx=5, pady=10, sticky='ew')
    current_number.set("0") 

    secondary_number = tk.StringVar()
    secondary_label = tk.Label(frm, textvariable=secondary_number, font=('Arial', 12), anchor='e', width=12)
    secondary_label.grid(column=0, row=0, columnspan=4, padx=5, sticky='ew')
    secondary_number.set("")

    def format_display(value):
        if value is None or value == "":
            return "0"
        s = str(value)
        # normalize leading zeros (keep "0" if empty)
        if s != "0":
            s = s.lstrip("0") or "0"
        # limit max length for UI (example)
        return s[:12]

    def update_display(current_var, secondary_var=None, current_value=None, secondary_value=None):
        # Single place to set StringVars (side effects centralized)
        if current_value is not None:
            current_var.set(format_display(current_value))
        if secondary_var is not None and secondary_value is not None:
            secondary_var.set(format_display(secondary_value))
    
    def on_digit(d):
        cur = current_number.get()
        # Replace initial "0" otherwise append
        if cur == "0":
            new = d
        else:
            new = cur + d
        update_display(current_number, current_value=new)

    # Create number buttons in a grid (calculator layout)
    digit_buttons = [
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
        ('4', 5, 0), ('5', 5, 1), ('6', 5, 2),
        ('1', 6, 0), ('2', 6, 1), ('3', 6, 2),
        ('0', 7, 1)
    ]
    for (digit, row, col) in digit_buttons:
        tk.Button(
            frm, 
            text=digit,
            width=5,
            height=2,
            command=lambda d=digit: on_digit(d)
        ).grid(row=row, column=col, padx=2, pady=2)
    
    function_buttons = [
        # (digit, row, col, function_reference, [args])
        ('⌫',2, 3, calculations.backspace, [current_number]), 
        ('AC', 2, 1, calculations.clear, [current_number, secondary_number]), 
        ('-', 4, 3, calculations.subtraction, [current_number, secondary_number]),
        ('/', 4, 1, calculations.division, [current_number, secondary_number]), 
        ('x', 4, 2 , calculations.multiplication, [current_number, secondary_number]), 
        ('+', 5, 3, calculations.addition, [current_number, secondary_number]),
        ('+/-', 7,0, calculations.negation, current_number),
        ('.', 7, 2, calculations.decimal_point, [current_number]),
        ('=', 7, 3, calculations.equals, [current_number, secondary_number]),
        
    ]
    for (digit, row, col, func_ref, args) in function_buttons:
        tk.Button(
            frm,
            text=digit,
            width=5,
            height=2,
            # Use lambda to call the function reference with its arguments
            command=lambda f=func_ref, a=args: f(*a)
        ).grid(row=row, column=col, padx=2, pady=2)

    root.mainloop()

if __name__ == "__main__":
    main()
