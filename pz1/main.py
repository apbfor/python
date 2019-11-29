import random
def main():
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

if __name__ == '__main__':
    main()