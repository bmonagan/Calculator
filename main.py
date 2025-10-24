from calculations import calculate
def main():
    print("Calculator, Press Q to quit")
    prev = None 
    while True:
        equation = input("Enter Equation:")
        if equation.lower() == "q":
            print("Closing program")
            break
        if prev:
            output = equation + prev
            calculate(output)
        else:
            output = calculate(equation)

        
        prev = output
        print(output)


if __name__ == "__main__":
    main()
2