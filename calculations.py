# placeholder

def calculate(equation):
    output = eval(equation)
    return str(output)

def append_digit(current_number, digit):
    current = current_number.get()
    if current == "0":
        current_number.set(str(digit))
    else:
        current_number.set(current + str(digit))

def clear():
    pass
