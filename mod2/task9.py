# Человек вводит на сайте номер телефона, ему позволено для удобства использовать
# кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.
# Пример
# Ввод
# +7 (812) 134-12-324
# Вывод
# +781213412324
#
user_input = "+7 (812) 134-12-324"

cleaned_number = ''

for char in user_input:
        # Добавляем в новую строку только цифры и плюс
    if char.isdigit() or char == '+':
        cleaned_number += char

print (cleaned_number)
