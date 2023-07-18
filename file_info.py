# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def file_extension(file):
    path, filename = os.path.split(file)
    name, extension = os.path.splitext(filename)
    return path, name, extension


file_path = "/users/Desktop/Big/258465_21.jpg"

print(file_extension(file_path))
