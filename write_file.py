# with open("result.txt", "w", encoding="utf-8") as file:# режим перезаписи файла(старое удаляет)
#     file.write("Привет, мир\n") # перенос на другую строку
#     file.write("Hello world\n")

# with open("result.txt", "a", encoding="utf-8") as file:
#     file.write("Новая запись\n")
#     file.write("Новая запись\n")
#     file.write("Новая запись\n")

def write_user_message(message):
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(f"Письмо от юзера: {message}")
    print("Сообщение добавлено")

def append_new_user():
    count_user = int(input("Сколько юзеров добавить: "))
    
    with open("data/users.txt", "a", encoding="utf-8") as file:
        for i in range(count_user):
            name = input("Введите имя:")
            file.write(name + "\n")

def write_favorite_movie():
    with open("data/favorite_movie.txt", "a", encoding="utf-8") as file:
        favorite_movie = input("Введите название любимого фильма: ")
        file.write(favorite_movie + "\n")
        print("Фильм успешно добавлен")

def show_movies():
    with open("data/favorite_movie.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for index, line in enumerate(lines, start = 1):
            print(f"{index} - {line.strip()}")
        


# def search_films():
#     with open("data/movies.txt", "r", encoding="utf-8") as file:
#         lines = file.readlines()

#         for index, line in enumerate(lines, start=1):

#             movie_data = line.split(",")
#             movie = movie_data[0].strip()
#             raiting = movie_data[1].strip()
#             print(movie, "рейтинг:",  raiting)
#             movie_dict = {
#                 "movie": movie,
#                 "raiting": raiting
#             }

        