import random,os,time

#Funciones
def move(board,hiddenBoard,flags,player,mov,width,height):
    """
    Player's movements throughout
    """
    admitted = False
    v_temp = player

    if mov.lower() == "w":
        if player > width:
            v_temp = player
            player -= width
            admitted = True
    elif mov.lower() == "a":
        if player % width != 1:
            v_temp = player
            player -= 1
            admitted = True
    elif mov.lower() == "s":
        if player <= width*(height-1):
            v_temp = player
            player += width
            admitted = True
    elif mov.lower() == "d":
        if player % width != 0:
            v_temp = player
            player += 1
            admitted = True

    #Values exchange
    if admitted:
        board[player] = "X"
        if v_temp in blocks:
            if hiddenBoard[v_temp] == 0:
                board[v_temp] = " "
            else:
                board[v_temp] = hiddenBoard[v_temp]
        else:
            board[v_temp] = "_"

        if v_temp in flags:
            print(flags,board[v_temp] is True,board[v_temp],v_temp)
            if board[player] == "F":
                board[v_temp] = "_"
            else:
                board[v_temp] = "F"

    return player, board

def boom(player,bombs):
    """
    Check if a bomb was planted
    """
    if player in bombs:
        return True
    if player not in blocks:
        blocks.append(player)
    return False

def flag(board,player,flags):
    """
    Set a flag
    """
    print("flags: ", flags)
    if player in flags:
        flags.remove(player)
    else:
        flags.append(player)
    print("flags: ", flags)

    return board,flags

def settings(mines_quant,height, width):
    height,width,mines = height,width,mines_quant
    os.system("cls")
    
    print("*************************************************")
    print("                  Mineswheeper")
    print("*************************************************")
    print()
    print()
    print("                   SETTINGS                ")
    print()
    print("            Board's width: {}".format(board_width))
    print("            Board's height: {}".format(board_height))
    print("            Mines quantity: {}".format(mines_quant))
    print()
    print()
    print()
    print("           Want to change settings? (y/n)        ")
    print()
    print("*************************************************")
    print()
    print("*************************************************")

    while True:
        try:
            ask = input("").lower()
        except TypeError:
            print("(y/n)", end="")
        else:
            if ask in ["y","n"]:
                break
    if ask == "y":
        os.system("cls")
        print("*************************************************")
        print("                  Mineswheeper")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("                Board height?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        height = int(input())
        os.system("cls")

        print("*************************************************")
        print("                  Mineswheeper")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("                Board width?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        width = int(input())
        os.system("cls")

        print("*************************************************")
        print("                  Mineswheeper")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("               How many mines?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        mines = int(input())
    os.system("cls")
    return mines,height,width

def loose():

    os.system("cls")

    print("*************************************************")
    print("                  Mineswheeper")
    print("*************************************************")
    print()
    print()
    print("                    YOU LOOSE!                ")
    print()
    print("            ")
    print()
    print()
    print()
    print()
    print()
    print("          Press Enter to continue...         ")
    print()
    print("*************************************************")
    print()
    print("*************************************************")
    time.sleep(3)
    os.system("cls")

def win():
    """
        Tablero al perder
        """
    os.system("cls")

    print("*************************************************")
    print("                  Mineswheeper")
    print("*************************************************")
    print()
    print()
    print("                    GANASTE!                ")
    print()
    print("            ")
    print()
    print()
    print()
    print()
    print()
    print("          Press Enter to continue...         ")
    print()
    print("*************************************************")
    print()
    print("*************************************************")

    time.sleep(3)
    os.system("cls")


def intro():
    """
    Tablero al iniciar
    """
    os.system("cls")

    print("*************************************************")
    print("                  Mineswheeper")
    print("*************************************************")
    print()
    print()
    print("                   WELCOME!                ")
    print()
    print("            ")
    print()
    print()
    print()
    print()
    print()
    print("          Press Enter to continue...         ")
    print()
    print("*************************************************")
    print()
    print("*************************************************")

    input()

    os.system("cls")

def menu():
    print("*************************************************")
    print("                  Mineswheeper")
    print("*************************************************")
    print()
    print()
    print("                   WELCOME!                ")
    print()
    print("              1. Start playing!")
    print("              2. Settings")
    print("              3. Exit")
    print()
    print()
    print()
    print("            Please, select an option...         ")
    print()
    print("*************************************************")
    ask = input("")
    return ask

def clues(screen,pixels,height, width):
    clues = {}
    players_position = random.choice(pixels_list)

    if screen == "hidden":

        for i in range(1, ((board_height * board_width) + 1)):
            clues.setdefault(i, 0)

        for i in pixels:

            if i > width: 
                up = i-width
                clues[up] += 1
                if i%width != 0: 
                    clues[i-width+1] += 1

            if i%width != 0: 
                clues[i+1] += 1
                if i < width* (height-1): 
                    clues[i+width+1] +=1

            if i < width* (height-1): 
                clues[i+width] += 1
                if i % width != 1: 
                    clues[i + (width -1)] += 1

            if i%width != 1: 
                clues[i-1] += 1
                if i > width: 
                    clues[i - (width + 1)] +=1

        print()
        for i in pixels:
            clues[i] = 9

    else:
        for i in range(1, ((board_height * board_width) + 1)):
            clues.setdefault(i, "_")
        clues[players_position] = "X"
        return clues, players_position
    return clues

def sort_minas(height,width,mines,pixels_list):
    """
    Sorts mines position 
    """
    pixels = list(pixels_list) 
    random.shuffle(pixels)
    for times in range((board_height * board_width) - mines_quant):
        pixels.pop()
    pixels.sort()
    return pixels

# Board config
board_height, board_width = 10,10
mines_quant = 15

#Tablero Visible
blocks = []
flags = []

pixels = None



intro()
while True:
    opc = menu()
    validas = [1,2,3]
    if int(opc) in validas:
        if int(opc) == 3:
            break
        elif int(opc) == 2:
            mines_quant,board_height,board_width = settings(mines_quant,board_height,board_width) #Configuraciones


        elif int(opc) == 1:
            #Settings before starting the main loop
            pixels_list = list(range(1, (board_height * board_width) + 1))
            pixels = sort_minas(board_height, board_width, mines_quant,pixels_list)
            hiddenBoard = clues("hidden", pixels, board_height, board_width)
            board, players_position = clues("vis", pixels, board_height, board_width)

            left = len(pixels_list)-len(pixels)

            while True:
                os.system("cls")
                print("*************************************************")
                print("                  Mineswheeper -  Blocks to sweep: {}".format(left))
                print("*************************************************")

                print(" (w/a/s/d)  -  move ")
                print("     b      -  sweep ")
                print("     f      -  set flag ")
                print("     q      -  quit ")
                print()

                hidden_matrix = []

                count = 0
                for i in range(board_height):
                    hidden_matrix.append([])
                    for e in range(board_width):
                        count += 1
                        hidden_matrix[i].append(hiddenBoard[count])

                visible_matrix = []


                count = 0
                for i in range(board_height):
                    visible_matrix.append([])
                    for e in range(board_width):
                        count += 1
                        visible_matrix[i].append(board[count])

                for i in visible_matrix:
                    print(" "*(len("*************************************************")-(board_width*3)),end="")
                    for a in i:
                        print(a," ",end="")
                    print()
                print()

                print("Select a command --> ",end="")
                while True:
                    try:
                        mov = input("")
                    except ValueError:
                        print("Introduzca una letra .")
                    else:
                        break

                bomb = None
                bandera = None
                if mov.lower() == "b":
                    bomb = boom(players_position,pixels)
                    if bomb is True:
                        os.system("cls")
                        loose()
                        blocks = []
                        flags = []
                        break
                    left -= 1
                    if players_position % board_width != 1:
                        players_position, board = move(board, hiddenBoard,flags, players_position, "a", board_width, board_height)
                    else:
                        players_position, board = move(board, hiddenBoard,flags, players_position, "d", board_width, board_height)
                elif mov.lower() == "q":
                    break
                elif mov.lower() == "f":
                    board, flags = flag(board,players_position,flags)
                    if players_position % board_width != 1:
                        players_position, board = move(board, hiddenBoard,flags, players_position, "a", board_width, board_height)
                    else:
                        players_position, board = move(board, hiddenBoard,flags, players_position, "d", board_width, board_height)
                else:
                    players_position ,board = move(board,hiddenBoard,flags,players_position,mov,board_width,board_height)

                flags.sort()
                if left == 0:
                    win()
                    blocks = []
                    flags = []
                    break
