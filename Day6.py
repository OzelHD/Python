# Write a program that:
# 1️⃣ Creates a Person class with attributes name and age.
# 2️⃣ Has a method to display the person's details.
# 3️⃣ Creates a Student class (inherits from Person) and adds an extra attribute for grade.
# 4️⃣ Overrides the method to also display the student's grade.


class Person:
    def __init__(self, name, age, attributes):
        self.name = name
        self.age = age
        self.attributes = attributes
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Attributes: {self.attributes}")


class Student(Person):
    def __init__(self, name, age, attributes, grade):
        super().__init__(name, age, attributes)     #inherit from Person.
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Attributes: {self.attributes}, Grade: {self.grade}")  

my_person = Person("S1", 21, "Likes Bananas")
my_person.display_info()

my_student2 = Student("S2", 22, "Likes Pineapples", 4.8)
my_student2.display_info()



# def fkt(x, y):
#     x = x+2
#     y= y+1
#     z = x+y
#     a = z + y + x
#     return x, y, z, a

# x,y =int(input("x ")), int(input("y "))
# X, Y, Z, A = fkt(x,y)
# print(str(X), str(Y), str(Z), str(A))