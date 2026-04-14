def search_user(user):
    with open("data/users.txt", "r", encoding="utf-8") as file:
        lines = file.readlines() # cписок

        for number,line in enumerate(lines, start=1):
            if user == line.strip():
                # print(number, line.strip())
                return number
