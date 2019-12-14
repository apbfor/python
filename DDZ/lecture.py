"""
Данный модуль содержит описание занятия
"""


class Lecture:
    """
    Каждый объект класса содержит поля:
    * полная запись из ячейки таблицы
    * вид занятия
    * номер занятия (если есть)
    * номер группы слушателей
    * аудитория
    * признак, яляется ли аудитория компьютерной
    """
    def __init__(self, lecture):
        self.lecture = lecture  # полная строка с записью
        self.lecture_type = ""
        self.lecture_number = ""
        self.classroom = ""
        self.group_number = ""
        self.is_computer = False
        # self.subject_name = ""
        # self.lecture_types = {'ПЗ': 'ПЗ',
        #                       'лаб.раб': 'ЛР',
        #                       'сем': 'Семинар',
        #                       'лекция': 'Лекция',
        #                       'зачет': 'Зачёт'}
        self.computer_list = [122, 113, 103, '20_УНЦ', '15_УНЦ',
                              '17_УНЦ', 'КВАНТ-КК']
        self.parse()
        if self.classroom in str(self.computer_list):
            self.is_computer = True
        # self.lecture_type = self.lecture_types[self.lecture_type]

    def parse(self):
        """
        Производит парсинг полей занятия из строки,
        полученной из ячейки таблицы
        :return:
        """
        step1 = self.lecture.split(':')
        if len(step1) == 3:
            pass
        else:
            # self.subject_name = step1[0]
            splited_lecture = step1[1].split('\n')
            if splited_lecture[0] == '' or splited_lecture[0] == ' ':
                lecture_desk = splited_lecture[1]
                self.lecture_type = lecture_desk.split('-')[0]
                if self.lecture_type[0] == ' ':
                    self.lecture_type = self.lecture_type.replace(' ', '')
                self.lecture_number = lecture_desk.split('-')[1].split(' ')[0]
                if len(splited_lecture) == 4:
                    self.classroom = splited_lecture[2].split(' ')[1]
                    self.group_number = splited_lecture[3].split(' ')[1]
                    if len(splited_lecture[3].split(' ')) == 3:
                        self.group_number += ' '
                        self.group_number += splited_lecture[3].split(' ')[2]
                else:
                    if splited_lecture[1][0] != ' ':
                        self.classroom = splited_lecture[1].split(' ')[2]
                    else:
                        self.classroom = splited_lecture[1].split(' ')[3]
                    self.group_number = splited_lecture[2].split(' ')[1]
                    for i in range(2, len(splited_lecture[2].split(' '))):
                        self.group_number += ' '
                        self.group_number += splited_lecture[2].split(' ')[i]
            else:
                lecture_desk = splited_lecture[0]
                self.lecture_type = lecture_desk.split('-')[0]
                self.lecture_type = self.lecture_type.replace(' ', '')
                if len(splited_lecture) == 2:
                    self.lecture_number = lecture_desk.split('-')[1].split(' ')[0]
                    self.classroom = splited_lecture[0].split(' ')[3]
                    self.group_number = splited_lecture[1].split(' ')[1]
                else:
                    self.classroom = splited_lecture[1].split(' ')[1]
                    self.lecture_number = lecture_desk.split('-')[1]
                    self.group_number = splited_lecture[2].split(' ')[1]
                    for i in range(2, len(splited_lecture[2].split(' '))):
                        self.group_number += ' '
                        self.group_number += splited_lecture[2].split(' ')[i]

    def __str__(self):
        """
        Выводит в удобном виде информацию о занятии при print(lecture)
        :return:
        """
        # print("Subject name:   ", self.subject_name)
        printer = "\n\nLecture type:   "
        printer += str(self.lecture_type)
        printer += "\nLecture number: "
        printer += str(self.lecture_number)
        printer += "\nClassroom:      "
        printer += str(self.classroom)
        printer += "\nGroup_number:   "
        printer += str(self.group_number)
        printer += "\nIs computer:    "
        printer += str(self.is_computer)
        return printer

    def __repr__(self):
        """
        Выводит информацию о занятии в итерируемых объектах
        :return:
        """
        if self.lecture is None:
            return None
        return self.__str__()
