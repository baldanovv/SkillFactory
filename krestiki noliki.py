def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
greet()
field = [[' ']* 3 for i in range(3)]
#vyvod polya func
def show():
    print(f' 0 1 2')
    for i in range(3):
        row_info = ' '.join(field[i])
        print(f'{i}{row_info}')

#sprashivaem igroka
def ask():
    while True:
        cords = input('Vash khod: ').split()
        if len(cords) != 2:
            print('Vvedite 2 coordinaty! ')
            continue
        x,y = cords
        if not(x.isdigit()) or not (y.isdigit()):
            print('Vvedit chsila! ')
            continue
        x,y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Koordinaty vne diapozona! ')
            continue
        if field[x][y] != ' ':
            print('Kletka zanyata! ')
            continue
        return x, y
#proverka
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Won X! ')
            return True
        if symbols == ['0', '0', '0']:
            print('Won 0! ')
            return True
    return False
#Usloviya pobedy
num = 0
while True:
    num +=1
    show()
    if num%2 == 1:
        print('Go X')
    else:
        print('Go O')
    x, y = ask()
    if num%2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    if check_win():
        break
    if num == 9:
        print('Nichya')
        break

