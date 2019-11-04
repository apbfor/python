# Created by apbfor on 04.11.20
import random

def guess():
    """Угадайка"""
    number = random.randint(0, 100)
    while True:
        answer = input('Угадайте число: ')
        if answer == 'exit':
            print('Правильный ответ - ', number)
            break
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
        if answer == 'exit':
            break
        else:
            print('Сам ты ', answer.upper(), '. И не кричи на меня.')


def calc():
    ent = input('Введите выражение ')
    while not ent == 'exit':
        try:
            a, b = ent.split('+')
            result = int(a) + int(b)
            print(result)
        except ValueError:
            print('Вы ввели неверное выражение')
        ent = input('Введите выражение ')
    print('Программа завершилась')


def group_parser(group):
    if not group.startswith('733'):
        print('Это не группа 3 курса')
        return

    if group.endswith('3'):
        print('%s - Третья группа' % group)
    elif group.endswith('4'):
        print('%s - Четверная группа' % group)
    elif group.endswith('5'):
        print('%s - Пятая группа' % group)
    else:
        print('%s - Непонятная группа' % group)


def main():
    """Определятор"""
    answer = input('Выберите функцию для запуска: ')
    while not answer == 'exit':
        if answer.upper() == 'УГАДАЙКА':
            guess()
        elif answer.upper() == 'КАЛЬКУЛЯТОР':
            calc()
        elif answer.upper() == 'ПОКРИЧИ':
            shout_on_me()
        else:
            group_parser('abc')
            for group_num in range(7331, 7336):
                group = str(group_num)
                group_parser(group)
        answer = input('Выберите функцию для запуска: ')



if __name__ == '__main__':
    main()
