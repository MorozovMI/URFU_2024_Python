# На вход подается строка s и символ i. Необходимо найти количество символов i,
# расположенных в начале строки.
# Формат ввода
# xyxxyx,x
# Формат вывода
# 1

s = input("Введите строку s: ")
i = input("Введите символ i: ")

count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break  # Прерываем цикл при первом символе, отличном от i

print(count)