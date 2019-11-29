"""В этом модуле реализована функция,
    позволяющая пользователю посмотреть
    список файлов и папок, находящихся
    по пути, указанном этим пользователем"""
import os


def listdir():
    """Функция реализует чтение пути
     с клавиатуры и вывод информации
     о содержании каталога"""
    startpath = "/home/apbfor/"
    foldername = input("Введите название папки")
    if ".." in foldername:
        print("Сочетание \"..\", предполагает "
              "доступ к родительскому каталогу,"
              "оно является запрещенным")
        return
    foldername.replace(" ", r"\ ")
    path = os.path.join(startpath, foldername)
    try:
        files = os.listdir(path)
        print(files)
    except FileNotFoundError as error:
        print("Не существует", error)


if __name__ == '__main__':
    listdir()
