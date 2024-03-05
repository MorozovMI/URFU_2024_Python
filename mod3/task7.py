phone_number = input()
cleaned_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(cleaned_number)

# Человек вводит на сайте номер телефона, ему позволено для удобства использовать
# кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.
# Пример
# Ввод
# +7 (812) 134-12-324
# Вывод
# +781213412324