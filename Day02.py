# Write a small program that:

# Asks the user for two numbers.
# Asks the user for an operation (+, -, *, /, //, %, **).
# Performs the operation and prints the result.

num = int(input("Please enter a number:\n"))
num2 = int(input("And another one:\n"))
operator = input("Please enter an operator (+, -, *, /, //, %, **):\n")
result = None

match operator:
    case "+":
        result = num + num2
    case "-":
        result = num - num2
    case "*":
        result = num * num2
    case "/":
        result = num / num2 if num2 != 0 else "Error: Division by 0 not allowed"
    case "//":
        result = num // num2 if num2 != 0 else "Error: Division by 0 not allowed"
    case "%":
        result = num % num2 if num2 != 0 else "Error: Division by 0 not allowed"
    case "**":
        result = num ** num2
    case _:
        print("Wrong operator.\n")
        exit()  # Exit early to avoid printing an undefined `result`

print(f"Your result is: {result}")
