#  Create a module (calculator.py) that contains:

# A function for addition
# A function for subtraction
# A function for multiplication
# A function for division
# 2️⃣ Import this module into another script and use it to perform calculations.

import Day7_Module as D7

x = 1
y = 2

x = D7.multi(D7.add(x, y), D7.multi(D7.add(x, y), D7.add(y, y)))
print(x)

