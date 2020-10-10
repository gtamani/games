#JUEGO PIEDRA PAPEL O TIJERA

import time
import os
import random

def bienvenida():
    """
    Cartel al iniciar el juego
    """
    print("*************************************************")
    print()
    print("*************************************************")
    print()
    print()
    print("                 BIENVENIDOS!                ")
    print()
    print("             Piedra, Papel o Tijeras           ")
    print()
    print()
    print()
    print()
    print()
    print("          Presione Enter para empezar...         ")
    print()
    print("*************************************************")
    print()
    print("*************************************************")


    input()

    os.system("cls")

def dibujos(jugador,pc,resultado):
    """
    Muestra los dibujos de las elecciones realizadas tanto por el usuario como de la pc
    """
    sum = 0
    while True:
        puntuacion(punt_jug, punt_pc)
        jugada = [jugador,pc]
        print()
        for i in range(len(jugada)):
            if jugada[i] == 1:
                print("                               @@@")
                print("             PIEDRA           @@@@")
                print("                             @@@@@")
            elif jugada[i] == 2:
                print("                              ___ ")
                print("             PAPEL           |   |")
                print("                             |___|")
            elif jugada[i] == 3:
                print("                              | /")
                print("             TIJERAS          |/")
                print("                             O O")
            if i == 0:
                print()
                print("              VS.  ")
                print()
        print()
        if resultado == 0:
            res = "GANASTE!"
        elif resultado == 1:
            res = "PERDISTE!"
        elif resultado == 2:
            res = "EMPATE!"

        left = (len("*************************************************") - len(res) + 1)-12

        print("*************************************************")
        print(" "*6," "*sum,end ="")
        print(res)

        print("*************************************************")
        sum += 1

        time.sleep(2/left)
        os.system("cls")
        if sum == left:
            break



def puntuacion(punt_jug,punt_pc):
    """
    Tablero que marca las puntuaciones
    """
    print("*************************************************")
    print("                       PUNTUACIÓN: TU {} | PC {} ".format(punt_jug,punt_pc))
    print("*************************************************")

def elegir():
    print("\n"*4)
    print("                      Elegí                        ")
    print()
    print("       1. Piedra | 2. Papel | 3. Tijera           ")
    print("\n"*4)
    print("*************************************************")
    print(" Tu turno!          ")
    print("*************************************************")


def eleccion_pc(jugador,jugador_ant,jugador_ant_ant,punt_ant,punt_ant_ant):
    if resultado_ant == 0:
        if resultado_ant_ant == None:
            posible = jugador_ant
        else:
            posible = random.choice((jugador_ant_ant,jugador_ant))

        if posible == 1:
            el = 2
        elif posible == 2:
            el = 3
        elif posible == 3:
            el = 1
    elif resultado_ant == 1:
        if jugador_ant == 1:
            posible = random.choice((2,3))
        elif jugador_ant == 2:
            posible = random.choice((1,3))
        elif jugador_ant == 3:
            posible = random.choice((1,2))

        if posible == 1:
            el = 2
        elif posible == 2:
            el = 3
        elif posible == 3:
            el = 1
    elif resultado_ant == 2 or resultado_ant is None:
        el = random.randint(1,3)


    return el




def comprobar_ganador(jugador,pc):
    """
    Comprueba quien es el ganador de la partida
    return 0 = gana jugador
    return 1 = gana pc
    return 2 = empate
    """
    if jugador == pc:
        return 2
    elif jugador == 1 and pc == 2:
        return 1
    elif jugador == 1 and pc == 3:
        return 0
    elif jugador == 2 and pc == 1:
        return 0
    elif jugador == 2 and pc == 3:
        return 1
    elif jugador == 3 and pc == 1:
        return 1
    elif jugador == 3 and pc == 2:
        return 0


os.system("cls")
bienvenida()
punt_jug,punt_pc = 0, 0
jugador_ant,jugador_ant_ant,resultado_ant,resultado_ant_ant = None, None, None, None
jugadas = []
results = []
jugador = 1

while True:

    puntuacion(punt_jug, punt_pc)
    elegir()
    while True:
        jugador = int(input())
        if jugador == 1 or jugador == 2 or jugador == 3:
            break


    pc = eleccion_pc(jugador,jugador_ant,jugador_ant_ant,resultado_ant,resultado_ant_ant)



    resultado = comprobar_ganador(jugador,pc)
    if resultado == 1:
        punt_pc += 1
    elif resultado == 0:
        punt_jug += 1
    os.system("cls")
    dibujos(jugador,pc,resultado)
    os.system("cls")



    jugadas.insert(0,jugador)
    results.insert(0,resultado)




    jugador_ant, resultado_ant = jugadas[0],results[0]
    if len(jugadas)>1:
        jugador_ant_ant,resultado_ant_ant = jugadas[1],results[1]





    if punt_jug == 10 or punt_pc == 10:
        break
