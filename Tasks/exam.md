Необходимо отписаться в [теме](http://gitlabnto/anetto/python/issues/2) о виде сдаваемой работы.

1. Файл с решением должен быть назван exam.py.
2. Файл exam.py pylint должен оценивать на 10 баллов.
3. Для каждой функции должны быть реализованы тесты, обеспечивающие покрытие более 80%.
1. Реализовать функцию is\_palindrome(). Для заданной строки str is_palindrome(str) должна возвращать 
    * True, если строка str является палиндромом (читается слева направо также, как и справо налево)
    * False в любом другом случае

    Например, is\_palindrome('Шалаш') == True, is_palindrome('python') == False
1. Реализовать функцию get\_most\_frequent\_value(max\_num, list\_of\_values). В переменной list\_of\_values хранятся натуральные числа от 0 до max\_num. Функция get\_most\_frequent\_value должна возвращать самое часто встречающееся число (если частота у двух чисел одинакова, то любое из этих чисел). Если в list\_of\_values есть число, превышающее max\_num, генерировать исключение ValueError.

    Например, get\_most\_frequent\_value(10, [2, 2, 2, 6]) == 2, get\_most\_frequent_value(10, [2, 2, 6, 6]) == 2 или 6 (вывести одно любое число).
1. Реализовать функцию is\_prime():
    * is\_prime(num) == True, если num - простое число.
    * is\_prime(num) == False в обратном случае.
    * генерировать исключение ValueError для num <= 0
    Например, is\_prime(7) == True, is\_prime(8) == False.
1. Реализовать класс Human. В конструкторе нужно принимать имя, вес и возраст Human(name, weight, age), все значения хранить в соответствующих полях. Поля необходимо валидировать на разумные значения (неотрицательный вес, неотрицательный возраст). Реализовать методы 
    * change\_name(new\_name) - меняет name на новое,
    * add\_weight(weight) - изменяет вес на указанную величину. Аргумент weight может быть отрицательным,
    * happy\_birthday() - прибавляет один год.

    ```python
    alex = Human('alex', 60, 20)
    print(alex.weight)  # == 60
    alex.add_weight(5)
    print(alex.weight)  # == 65
    alex.add_weight(-15)
    print(alex.weight)  # == 50
    alex.happy_birthday()
    alex.happy_birthday()
    print(alex.age)  # == 22
    ```
1. После спасения принцессы Марио решил заняться строительством замков. Следуя своей непознаваемой логике, Марио строит замки только в низинах и на высотах. Реализуйте функцию count\_castles(landscape), которая возвращает число замков, которые построит Марио для заданного списка высот landscape. То есть в любой локальной низине, в любой локальной возвышенности должен быть замок. Считать, что на краю карты всегда есть резкое изменение высоты.

    ![castles](castles.PNG)

    ```python
    count_castles([1, 2, 3]) == 2  # замки на 1 и 3
    count_castles([1, 1, 1]) == 1  # замок на 1
    count_castles([1, 2, 3, 2, 1]) == 3  # замки на 1, 3 и 5
    ```