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
    startpath = "/home/user/"
    foldername = input("Введите название папки: ")
    if ".." in foldername:
        print("Сочетание \"..\", предполагает доступ к "
              "родительскому каталогу, оно является запрещенным")
        return
    foldername.replace(" ", r"\ ")
    path = os.path.join(startpath, foldername)
    try:
        files = os.listdir(path)
        print(files)
    except FileNotFoundError as error:
        print("Не существует", error)
        return


if __name__ == '__main__':
    listdir()
