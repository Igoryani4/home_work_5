# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст для фильтрации :').split()
find_text = input('Введите исходный текст по которому будем исключать :')
list_result = []
def find_result (a, b):
    for txt in a:
        if b in txt:
            continue
        else:
            list_result.append(txt)
    print(' '.join(list_result))


find_result(text, find_text)

# кабвак проверить не проверяемое необхабводимо добабвить какую то рыбу?