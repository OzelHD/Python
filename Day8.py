# Write a program that: 
# 1️⃣ Creates a dictionary of a person’s details (name, age, city).
# 2️⃣ Saves this data to a person.json file.
# 3️⃣ Reads back the data from the file and prints it.


import json
Input = list(map(str, input("Please enter the following Data in Order: Name, age, city separated by space:\n").split()))
while len(Input) != 3:
    Input = list(map(str, input(f"{Input} is no valid Input. Please enter the following Data in Order: Name, age, city separated by space:\n").split()))



data = {
    "name": Input[0],
    "age": int(Input[1]),
    "city": Input[2]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


with open("data.json", "r") as file:
    loaded_data = json.load(file)


type = input("What do you wanna know? (name, city or age) => ")

while type not in ["name", "city", "age"]:
    type = input(f"{type} is no valid type. WHat do you wanna know? (name, city or age) => ")


print(loaded_data[type])
