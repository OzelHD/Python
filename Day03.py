

# Asks the user for a list of numbers (separated by spaces).
# Stores them in a list.
# Asks the user for an operation (sum or average).
# Computes and prints the result using a function.

numbers = list(map(float, input("Enter the list of numbers, separated by space:\n").split()))
operator = input("Please enter either one of the operators: sum, average.\n")

def compute(n, o):
    if len(n):
        if o == 1 or o == 2:
            num = 0
            if o == 1:
                # for number in n:
                #     num += number
                num =sum(n)
            elif o == 2:
                # for number in n:
                #     num += number
                num =sum(n) / len(n)
            return num
        return "Error, illegal operator."




match operator:
    case "sum":
        operator = 1
    case "average":
        operator = 2
    case _:
        operator = 0


print(f"Your computed number is: {compute(numbers, operator)}")
