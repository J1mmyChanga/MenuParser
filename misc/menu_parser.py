from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

def get_menu(filename):
    categories = {}
    table = load_workbook(filename)
    sheet = table['меню для кассы']
    for i in range(1, len(list(sheet))):
        weight = sheet['A' + str(i)].value
        name = sheet['B' + str(i)].value
        price = sheet['C' + str(i)].value
        person = sheet['D' + str(i)].value
        try:
            if weight is None and name:
                title = name
                categories[title] = []
        except AttributeError:
            continue
        if None not in (weight, name, price):
            position = {'weight':str(weight), 'name':str(name), 'price':str(price), 'person':str(person)}
            categories[title] += [position]
    return categories