# Asks the user for two numbers (numerator & denominator).
# Performs division and prints the result.
# Handles these errors properly:
# ZeroDivisionError (if denominator is 0)
# ValueError (if input is not a number)
# Prints "Thank you!" at the end, whether an error happened or not.

num, denom = input("Enter Numerator:\n") , input("And Denominator:\n")
def div(n, d):
    try:
        result = int(n)/int(d)
        print(f"{n} / {d} is {result}.")
    except ZeroDivisionError:
        print("Division by zero not allowed.\n")
    except ValueError:
        print(f'num "{n}" or denom "{d}" is not a valid value.\n')
    finally:
        print("Thank you!")

div(num, denom)
