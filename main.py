def main():
    print("Calculator, Press Q to quit")
    while True:
        equation = input("Enter Equation:")
        if equation.lower() == "q":
            print("Closing program")
            break

if __name__ == "__main__":
    main()
