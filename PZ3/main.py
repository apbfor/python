# Created by apbfor on 10.11.20
import random


def guess():
    """Угадайка"""
    number = random.randint(0, 100)
    while True:
        answer = input('Угадайте число: ')
        if answer == 'exit' or answer == 'q':
            print('Правильный ответ - ', number)
            return answer
        elif not answer.isdigit():
            print('Нужно вводить число, а не символы!')
        else:
            answer = int(answer)
            if answer == number:
                print('Успех')
                break

            elif answer < number:
                print('Бери выше')
            else:
                print('Бери ниже')


def shout_on_me():
    while True:
        answer = input('Что ты сказал? ')
        if answer == 'exit' or answer == 'q':
            return answer
        print('Сам ты ', answer.upper(), '. И не кричи на меня.')


def calc():
    while True:
        ent = input('Введите выражение ')
        if ent == 'exit' or ent == 'q':
            return ent
        try:
            a, b = ent.split('+')
            result = int(a) + int(b)
            print(result)
        except ValueError:
            print('Вы ввели неверное выражение')


def print_menu():
    print("1. Угадайка")
    print("2. Калькулятор")
    print("3. Покричи")


def main():
    """Определятор"""
    funcs = {'УГАДАЙКА': guess,
             'КАЛЬКУЛЯТОР': calc,
             'ПОКРИЧИ': shout_on_me
             }
    by_num = dict(enumerate(funcs.keys()))
    print_menu()
    while True:
        func = input('Выберите функцию для запуска: ')
        if func == 'exit':
            print("До встречи!")
            return
        elif func.isdigit():
            try:
                func = by_num[int(func) - 1]
            except KeyError:
                print("Вы ввели несуществующую функцию")
                continue
        else:
            func = func.upper()
        try:
            output = funcs.get(func, 'exit')()
            if output == 'exit':
                print("Завершена подпрограмма ", func)
                break
            else:
                print_menu()
        except TypeError:
            print('Вы ввели несуществующую функцию')


if __name__ == '__main__':
    main()
