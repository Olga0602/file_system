from write_file import*
import read_file
import os

def test_func():
     pass

if os.path.exists("config.txt"):
    print("Файл существует")
else:
     with open("result.txt", "a", encoding="utf-8") as file: # создает файл
          pass 


name_folder = input("Введите имя папки: ")
name_file = input("Введите имя файла: ")

print(os.listdir("."))
if f"{name_folder}" in os.listdir("."):
     with open(f"{name_folder}/{name_file}", "a", encoding="utf-8") as file: # создает файл
           pass 
else:
       os.mkdir(f"{name_folder}")
       with open(f"{name_folder}/{name_file}", "a", encoding="utf-8") as file: # создает файл
           pass   

# if name_folder not in os.listdir("."): тоже что и выше только без повторений
#      os.mkdir(name_folder)
# with open(f"{name_folder}/{name_file}", "a", encoding="utf-8") as file: # создает файл
#            pass



# os.mkdir(f"{name_folder}")
# with open(f"{name_folder}/{name_file}", "a", encoding="utf-8") as file: # создает файл
#           pass 



# write_user_message("Привет пайтон")

# append_new_user()
# search_name = input("Какого юзера найти")
# read_file.search_user()
# print(f"Пользователь {search_name} находится на {read_file.search_user(search_name)} строчке")

# write_favorite_movie()
# show_movies()

# file = open("data.txt", "r", encoding="utf-8")
# for line in file:
#     print(line.strip())
# # content = file.read() чтение всего файла
# # print(content)

# file.close() # обязательно закрываем

# with open("data/new_data.txt", "r", encoding="utf-8") as file_data: # второй способ откр и закр файла
#     lines = file_data.readlines()
#     print(lines)

# for index, line in enumerate(lines, start = 1):
#     print(f"{index} - {line.strip()}")
# print(len(lines))

