"""
В этом модуле реализована функция,
позволяющая пользователю посмотреть
список файлов и папок, находящихся
по пути, указанном этим пользователем
"""
import os


def listdir():
    """
    Shows files on path

    Returns:
        "None" if path not exists or is parent dir

    Raises:
        ValueError: Raises an exception while args
        or operation is not correct.
    """
    while True:
        startpath = "/home/apbfor"
        foldername = input("Введите название папки: ")
        if foldername == '0exit':
            break
        foldername.replace(" ", r"\ ")
        path = os.path.join(startpath, foldername)
        path = os.path.abspath(path)
        if startpath not in path:
            print("Вы пытаетесь получить доступ к родительскому каталогу")
            return
        try:
            files = os.listdir(path)
            print(files)
        except FileNotFoundError as error:
            print("Не существует", error)
            return


if __name__ == '__main__':
    listdir()
