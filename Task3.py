from tkinter import *
import random
root = Tk()
root.title('Крестики-нолики')
game_run = True
field = []
cross_count = 0


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()



# from tkinter import *
# from tkinter import ttk

# class FeetToMeters:

#     def __init__(self, root):

#         root.title("Feet to Meters")

#         mainframe = ttk.Frame(root, padding="3 3 12 12")
#         mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)
       
#         self.feet = StringVar()
#         feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
#         feet_entry.grid(column=2, row=1, sticky=(W, E))
#         self.meters = StringVar()

#         ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
#         ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

#         ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#         ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#         ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#         for child in mainframe.winfo_children(): 
#             child.grid_configure(padx=5, pady=5)

#         feet_entry.focus()
#         root.bind("<Return>", self.calculate)
        
#     def calculate(self, *args):
#         try:
#             value = float(self.feet.get())
#             self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#         except ValueError:
#             pass

# root = Tk()
# FeetToMeters(root)
# root.mainloop()