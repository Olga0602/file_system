with open("data/users.txt", "r", encoding = "utf-8") as file_data:
    lines = file_data.readlines()
    print(lines)

name = input("Введите имя:")

for index, line in enumerate(lines, start = 1):
    if name in line.strip():
        print(f"{index} - {line.strip()}")
        break

   





