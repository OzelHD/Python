# Ask the user for a filename (e.g., "notes.txt").
# Ask whether they want to read or write.
# If reading, print the file’s content.
# If writing, take input from the user and save it to the file.

filename, RoW = input("Please enter the file name: "), input("Read (r), append (a) or overwrite (w)\n")
while RoW not in ["r", "w", "a"]:
    RoW = input(f"{RoW} is an illegal operator. Please enter (r) for Read, (a) for append or (w) for write.\n")
match RoW:
    case "r":
        try:
            with open(filename, "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
    case "w":
        WriteInput = input("What do you wana overwrite in the file? Enter it on the next line.\n")
        with open(filename, "w") as file:
            file.write(WriteInput + "\n")
    case "a":
        WriteInput = input("What do you wana write in the file? Enter it on the next line.\n")
        with open(filename, "a") as file:
            file.write(WriteInput + "\n")
    case _:
        pass
