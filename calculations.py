

def calculate(equation):
    # placeholder
    output = eval(equation)
    return str(output)

def append_digit(current_number, digit):
    current = current_number.get()
    if current == "0":
        current_number.set(str(digit))
    else:
        current_number.set(current + str(digit))

def clear(current_number, secondary_number):
    pass
def addition(current_number, secondary_number):
    pass
def subtraction(current_number, secondary_number):
    pass
def multiplication(current_number, secondary_number):
    pass   
def division(current_number, secondary_number):
    pass
def backspace(current_number):
    current = current_number.get()
    if len(current) > 1:
        current_number.set(current[:-1])
    else:
        current_number.set("0")
def equals(current_number, secondary_number):
    pass