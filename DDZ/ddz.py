from openpyxl import load_workbook

wb = load_workbook('rasp.xlsx')
sheet_ranges = wb['Фамилия Имя Отчество']


def main():
    subject_name = ""
    lecture_type = ""
    lecture_number = ""
    classroom = ""
    group_number = ""
    lecture = sheet_ranges['Q19'].value
    print(lecture)
    step1 = lecture.split(':')
    subject_name = step1[0]
    splited_lecture = step1[1].split('\n')
    print(splited_lecture)
    if splited_lecture[0] == '' or splited_lecture[0] == ' ':
        lecture_desk = splited_lecture[1].split(' ')[0]
        lecture_type = lecture_desk.split('-')[0]
        lecture_number = lecture_desk.split('-')[1]
        classroom = splited_lecture[1].split(' ')[2]
        group_number = splited_lecture[2].split(' ')[1]
    else:
        lecture_desk = splited_lecture[0]
        lecture_type = lecture_desk.split('-')[0]
        lecture_number = lecture_desk.split('-')[1]
        lecture_type = lecture_type.replace(' ', '')
        classroom = splited_lecture[1].split(' ')[1]
        group_number = splited_lecture[2].split(' ')[1]

    print("Subject name:   ", subject_name)
    print("Lecture type:   ", lecture_type)
    print("Lecture number: ", lecture_number)
    print("Classroom:      ", classroom)
    print("Group_number:   ", group_number)


if __name__ == '__main__':
    main()
