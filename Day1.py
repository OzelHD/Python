name = input("Hello user, what is your name? \n")

print("Hey, " + name + ". I hope you will have a nice stay here. Do you wana know your age in x years?\n")
if (input("y/n\n") == "y"):
    age = int(input("Please enter your Age.\n"))
    x = int(input("Please enter the years you wanna have passed.\n"))
    print("In " + str(x) + " years, you will be " + str(age + x) + " years old.\n")
else:
    print("Bye.\n")
