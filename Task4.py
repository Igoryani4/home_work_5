# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

text = 0
with open("uncode1.txt", "r") as file:
    for i in file:
        text = i
count =0
symbol = []
b = 0
for i in text:
    
    if i != b:
        if count == 0:
            b = i
            count = 1
        if count == 1:
            symbol.append(i)
            b = i
            count = 1
        else:
            symbol.append(count)
            symbol.append(i)
            b = i
            count = 1
    else:
        count += 1
        b = i
symbol.append(count)


with open('code.txt', 'w') as f:
    for i in symbol:
        f.write(str(i))



#####

code_list = []
code = 0
with open("code.txt", "r") as file:
    for i in file:
        code = i




for i in range(len(code)):
    if code[i] in '1234567890':
        if i == len(code)-1:
            continue
        elif code[i-1] in '1234567890':
            for j in range(int(code[i])):
                code_list.append(code[i])
                continue
        else:
            for j in range(int(code[i])):
                code_list.append(code[i-1])


print(''.join(code))

with open('uncode.txt', 'w') as f:
    for i in code_list:
        f.write(str(i))

print(''.join(code_list))

