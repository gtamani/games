#JUEGO NIM

import time
import os
import random

def bienvenida():
    """
    Cartel al iniciar el juego
    """
    print("*************************************************")
    print()
    print("                BIENVENIDOS A NIM                ")
    print()
    print()
    print()
    print("          Presione Enter para empezar...         ")
    print()
    print("*************************************************")

    input()

    os.system("cls")

    print("*************************************************")
    print()
    print("                 Elige un nivel                  ")
    print()
    print()
    print()
    print("         1. Fácil       |       2. Díficil       ")
    print()
    print("*************************************************")



    while True:
        opt = int(input())
        if opt == 1:
            facil = True
            break
        elif opt == 2:
            facil = False
            break
        else:

            print("*************************************************")
            print()
            print("                 Elige un nivel                  ")
            print()
            print("                Prueba de nuevo...              ")
            print()
            print("         1. Fácil       |       2. Díficil       ")
            print()
            print("*************************************************")

    os.system("cls")
    return facil

def bienvenida2(palillos,max_palillos):
    print("*************************************************")
    print()
    print("                Habra {} palillos                ".format(palillos))
    print("        Puedes sacar entre 1 y {} palillos       ".format(max_palillos))
    print("               Empiezas moviendo tu              ")
    print()
    print("               Enter para empezar.               ")
    print()
    print("*************************************************")
    input()

def sorteo():
    """
    Se realiza un sorteo tanto del número de palillos como del máximo de palillos a sacar
    """
    return random.randint(16, 23),random.randint(3, 5)


def palillos_screen(palillos):
    """
    Muestra la cantidad de palillos en pantalla
    """
    os.system("cls")
    a = ("   |") * palillos
    for i in range(5):
        print(a)
        print()

def random_palillos(max_palillos):
    """
    Nivel Fácil: Aleatoriamente saca entre 1 y 3 palillos
    """
    return random.randint(1,max_palillos)

def turno_pc(dif,palillos,max_palillos):
    """
    Devuelve la cantidad de palillos que saca la pc en función del nivel de dificultad
    """
    time.sleep(1.5)
    os.system("cls")
    palillos_screen(palillos)
    print("Estoy pensando...".center(15))
    time.sleep(1.5)

    if dif == True:
        saca = random_palillos(max_palillos)
    elif dif == False:
        resto = palillos%(max_palillos+1)
        if palillos > max_palillos:
            if resto == 0:
                saca = random_palillos(max_palillos)
            else:
                saca = resto
        else:
            saca = palillos

    palillos_screen(palillos)
    if saca == 1:
        print("Voy a sacar un palillo".center(15))
    else:
        print("Voy a sacar {} palillos".format(saca).center(15))
    time.sleep(1)



    pal = palillos - saca


    return pal

def final(ganador):
    if ganador == True:
        print("*************************************************")
        print()
        print()
        print("                    GANASTE!!!                ")
        print()
        print()
        print("*************************************************")
    else:
        print("*************************************************")
        print()
        print()
        print("                    PERDISTE!!!                ")
        print()
        print()
        print("*************************************************")


os.system("cls")
dificultad = bienvenida()

palillos = random.randint(16,23)
max_palillos = random.randint(3,5)
palillos,max_palillos = sorteo()

bienvenida2(palillos,max_palillos)
palillos_screen(palillos)
while True:

    #TURNO DE LA PERSONA

    while True:
        print("Tu turno: Elige la cantidad de palillos entre 1 y {}".format(max_palillos).center(15))
        pal_menos = int(input())
        if pal_menos < (max_palillos+1):
            break

    palillos -= pal_menos
    if palillos <= 0:
        ganador = True
        break
    palillos_screen(palillos)
    print("Sacaste {} palillos".format(pal_menos).center(15))

    #TURNO DE LA PC

    palillos = turno_pc(dificultad,palillos,max_palillos)

    palillos_screen(palillos)
    if palillos <= 0:
        ganador = False
        break

os.system("cls")
final(ganador)