# Write a program that:
# 1️⃣ Creates a Person class with attributes name and age.
# 2️⃣ Has a method to display the person's details.
# 3️⃣ Creates a Student class (inherits from Person) and adds an extra attribute for grade.
# 4️⃣ Overrides the method to also display the student's grade.

class person:
    name = str(input("name"))
    age = int(input("Age"))

print(person.name)

# def fkt(x, y):
#     x = x+2
#     y= y+1
#     z = x+y
#     a = z + y + x
#     return x, y, z, a

# x,y =int(input("x ")), int(input("y "))
# X, Y, Z, A = fkt(x,y)
# print(str(X), str(Y), str(Z), str(A))