import xlsxwriter # Это модуль Python для записи файлов в формате Excel 2007+ XLSX

try:
 array = ['Zbrush', 'Maya', 'Blender', '3DMax']
 arrayn = ['5', '6', '7', '8']
 my_file = 'ZEA.xlsx' # Имя файла
 book = xlsxwriter.Workbook(my_file) # Создание файла
 sheet = book.add_worksheet() # Добавление в него книги
 sheet.set_column('A:A', 35) # Установка ширины колонки
 bold = book.add_format({'bold': True}) # Формат жирного текста
 sheet.write('A1', '3D Character artist - Zhenis Elaman', bold) # Выдача текста в ячейку
 itr = 1
 for i in array:
  sheet.write(itr, 0, i)  # Выдача значения в ячейку 3 строка 1 столбец [2,0]
  sheet.write(itr, 1, arrayn[itr - 1] + ' лет')  # Выдача значения в ячейку 3 строка 1 столбец [2,0]
  itr += 1
 sheet.insert_image('C1', 'skull2.jpg', {'x_scale': 0.08, 'y_scale': 0.08}) # Вставка в ячейку картинки
 sheet.insert_image('E1', 'skull1.jpg', {'x_scale': 0.08, 'y_scale': 0.08}) # Вставка в ячейку картинки
 sheet.insert_image('G1', 'skull.jpg', {'x_scale': 0.08, 'y_scale': 0.08}) # Вставка в ячейку картинки
 book.close() # Закрытие файла
except Exception as a: # Обработка ошибок
 print("Error!")
 print(a)