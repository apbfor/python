from openpyxl import load_workbook

wb = load_workbook('rasp.xlsx')
sheet_ranges = wb['Фамилия Имя Отчество']


def main():
    try:
        for j in range(len(sheet_ranges['C2:Q33'])):
            for i in sheet_ranges['C2:Q33']:
                print(i[j].value)
    except IndexError:
        print("Чутка вышли за диапазон")


if __name__ == '__main__':
    main()

