from openpyxl import load_workbook
from lecture import Lecture
from day import Day

wb = load_workbook('rasp.xlsx')
sheet_ranges = wb['Фамилия Имя Отчество']


def main():
    lecture_value = sheet_ranges['M27'].value
    lecture = Lecture(lecture_value)
    # print(lecture)
    day = Day()
    day.lectures[0] = lecture
    lecture_value = sheet_ranges['Q14'].value
    lecture = Lecture(lecture_value)
    day.lectures[1] = lecture
    lecture_value = sheet_ranges['O14'].value
    lecture = Lecture(lecture_value)
    day.lectures[2] = lecture
    lecture_value = sheet_ranges['M20'].value
    lecture = Lecture(lecture_value)
    day.lectures[3] = lecture
    print(day.lectures)


if __name__ == '__main__':
    main()
