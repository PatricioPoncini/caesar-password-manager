import os
from tabulate import tabulate

SHIFT = 2
FILE_NAME = "securePasswordData.txt"
SEPARATOR = ";|"

def cipher(data, shift):
    result = ""
    for char in data:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    return result


while True:
    menu = input("\n1. New password\n2. View passwords\n3. Exit\n>> ")

    if menu == "1":
        raw_inputs = [
            input("Software: "),
            input("Username: "),
            input("Password: ")
        ]

        encrypted_line = SEPARATOR.join([cipher(item, SHIFT) for item in raw_inputs])

        with open(FILE_NAME, "a") as file:
            file.write(encrypted_line + "\n")

        print("Password saved successfully!")

    elif menu == "2":
        if not os.path.exists(FILE_NAME):
            print("The file does not exist yet...")
            continue

        table_data = []
        with open(FILE_NAME, "r") as file:
            for line in file:
                encrypted_data = line.strip().split(SEPARATOR)
                decrypted = [cipher(item, -SHIFT) for item in encrypted_data]
                table_data.append(decrypted)

        print(tabulate(table_data, headers=["Software", "Username", "Password"], tablefmt="grid"))

    elif menu == "3":
        break
    else:
        print("Invalid option")