import os
import shutil

print(os.path.exists("read_file.py"))  # проверка существует ли файл

if os.path.exists("read_file.py"): 
    print("Файл существует")

# os.mkdir("reports/2026") # создает директории(папки)это две папки
print(os.listdir("data"))
print(os.listdir(".")) # точка ук на текущую директорию выводит спиcoк файлов и папок

path = "reports/2026"
print(os.path.isdir(path)) # проверка папка ли это
print(os.path.isfile(path)) # явл ли файлом 

# os.rmdir("reports/2026") # уд папку 2026
shutil.rmtree(path)
