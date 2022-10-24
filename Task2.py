# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random

print ('Это программа, для игры в 2021 канфету. Все конфеты оппонента достаются сделавшему последний ход.')
choosing_an_opponent = int(input('Введите цифру если \n1 - хотите сыграть с 2-ым человеком\n2 - если с ботом\n3 - если с интелектуальным ботом \n : '))

def find_opponent(x):
    if x == 1:
        game_1on1()

def game_1on1():
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга')
    print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет')
    print('Все конфеты оппонента достаются сделавшему последний ход')
    rand_opponent = random.randint(1, 2)
    print(f'Первый ход делает игрок №{rand_opponent}')
   

def check_win ():
    flag = False
    if num == 0:
        print(' Вы Выиграли, поздравляем!!!' )
        flag = True
        return flag
        
         

game_1on1()
# def game (rand_opponent):
#     print('')
num  = 100
player1 = 0
total_player1 = 0

player2 = 0
total_player2 = 0
while num > 1:
    print(f'На столе конфет {num}, у первого игрока {total_player1} конфет, у второго игрока {total_player2} конфет')
    player1 = int(input('Ходит первый игрок, введите число от 1 до 28 :'))
    if player1 > 28 or player1 < 1:
        while player1 > 28 or player1 < 1:
            player1 = int(input('Ходит первый игрок, введите ПРАВИЛЬНОЕ число от 1 до 28 :'))
    check_win()
    if flag == True:
        num  = 100
        player1 = 0
        total_player1 = 0

        player2 = 0
        total_player2 = 0
        print(f' Все конфеты достаются Player1  а это целых {num} конфет. Поздравляю!!!')
    num -= player1
    total_player1 += player1
    print(f'На столе конфет {num}, у первого игрока {total_player1} конфет, у второго игрока {total_player2} конфет')
    player2 = int(input('Ходит ВТОРОЙ игрок, введите число от 1 до 28 :'))
    if player2 > 28 or player2 < 1:
        while player2 > 28 or player2 < 1:
            player2 = int(input('Ходит ВТОРОЙ игрок, введите ПРАВИЛЬНОЕ число от 1 до 28 :'))
    check_win()
    if flag == True:
        num  = 100
        player1 = 0
        total_player1 = 0

        player2 = 0
        total_player2 = 0
        print(f' Все конфеты достаются Player2  а это целых {num} конфет. Поздравляю!!!')
    num -= player1
    total_player1 += player1
    num -= player2
    total_player2 += player2
    
