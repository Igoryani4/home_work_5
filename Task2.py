# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"


from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")







def game1on1():
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0,2) # флаг очередности
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0 
    counter2 = 0

    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")





def game_bot():
    player1 = input("Введите имя игрока: ")
    player2 = "Гай" 
    print("Привет меня зовут бот Гай я сыграю с тобой ")
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0,2) # флаг очередности
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0 
    counter2 = 0

    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = randint(1,28)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")



def game_inteleckt_bot():
    player1 = input("Как тебя зовут?: ")
    player2 = 'Эйнштейн' 
    print(f'Привет {player1} меня зовут бот Эйнштейн и я умею играть :) ')
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0,2) # флаг очередности
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0 
    counter2 = 0

    while value > 28:
        if flag:
            k = input_dat(player1)
            b = k
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            
            if value < 29:
                k = value
            else:
                delenie = value//28
                k = value - ((delenie*28)+1)
                if k == -1:
                    k = 28 -1
                if k == 0:
                    k = 28
            while k > 28 or k < 1:
                k = randint(1,28)
            
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")


who_game = int(input('Введите цифру если \n1 - хотите сыграть с 2-ым человеком\n2 - с ботом\n3 - с интелектуальным ботом \n : '))

if who_game == 1:
    game1on1()
if who_game == 2:
    game_bot()
else:
    game_inteleckt_bot()