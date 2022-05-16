def greet():
    print("~~~~~~~~~~~~~~~~~~~")
    print(" Добро пожаловать  ")
    print("      в игру       ")
    print("  Крестики-Нолики  ")
    print("~~~~~~~~~~~~~~~~~~~")
    print(" формат ввода: X Y ")
    print(" X - номер строки  ")
    print(" Y - номер столбца ")
    print("~~~~~~~~~~~~~~~~~~~")
    print("Разработчик Гладков")
    print("~~~~~~~~~~~~~~~~~~~")
    print()


def show():
    print(" +" + "---+" * 4)
    row_header = [str(i+1) for i in range(3)]
    print(f" | \\ | {' | '.join(row_header)} |")
    print(" +" + "---+" * 4)
    for i, row in enumerate(field):
        print(f" | {i+1} | {' | '.join(row)} |")
        print(" +" + "---+" * 4)
    print()


def ask():
    while True:
        cords = input("     Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты!")
            continue

        x_ask, y_ask = cords

        if not x_ask.isdigit() or not y_ask.isdigit():
            print(" Введите числа!")
            continue

        x_ask, y_ask = int(x_ask) - 1, int(y_ask) - 1

        if not (0 <= x_ask <= 2 and 0 <= y_ask <= 2):
            print(" Координаты вне диапазона!")
            continue

        if field[x_ask][y_ask] != " ":
            print(" Клетка занята!")
            continue

        return x_ask, y_ask


def check_win():
    def check_list():
        return "XXX" in check or "OOO" in check

    for i in range(3):
        check = ""
        for j in range(3):
            check += field[i][j]
        if check_list():
            return True

    for i in range(3):
        check = ""
        for j in range(3):
            check += field[j][i]
        if check_list():
            return True

    check = ""
    for i in range(3):
        check += field[i][i]
        if check_list():
            return True

    check = ""
    for i in range(3):
        check += field[2 - i][i]
        if check_list():
            return True

    return False


def game():
    num_step = 0
    while True:
        num_step += 1

        show()

        if num_step % 2 == 1:
            print(" Ходит X!")
        else:
            print(" Ходит O!")

        x, y = ask()

        if num_step % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "O"

        if check_win():
            show()
            print(f" Победил {'X' if (num_step % 2 == 1) else 'O'} !!!")
            break

        if num_step == 9:
            show()
            print(" Победила дружба!")
            break


def reload():
    while True:
        print(" Хотите поиграть ещё?")
        reply = input("  Y - да! N - нет: ").lower()
        if reply != "y" and reply != "n":
            print(" Ответьте Y или N!")
            continue

        return reply == 'y'


greet()
while True:
    field = [[" "] * 3 for i in range(3)]
    game()

    if not reload():
        break
