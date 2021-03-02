import random,os,time

#Funciones
def move(visible,oculto,flags,jugador,mov,ancho,alto):
    """
    Desplaza al jugador por el tablero
    :param jugador: Posición del jugador
    :param movimiento: w/a/s/d
    :return: Nueva posición
    """
    admitted = False
    v_temp = jugador

    if mov.lower() == "w":
        if jugador > ancho:
            v_temp = jugador
            jugador -= ancho
            admitted = True
    elif mov.lower() == "a":
        if jugador % ancho != 1:
            v_temp = jugador
            jugador -= 1
            admitted = True
    elif mov.lower() == "s":
        if jugador <= ancho*(alto-1):
            v_temp = jugador
            jugador += ancho
            admitted = True
    elif mov.lower() == "d":
        if jugador % ancho != 0:
            v_temp = jugador
            jugador += 1
            admitted = True

    #print(v_temp)
    #print(jugador)
    #print(visible)


    #Intercambio de valores
    if admitted:
        visible[jugador] = "X"
        if v_temp in bloques:
            # bloques.append(pos_jugador)
            if oculto[v_temp] == 0:
                visible[v_temp] = " "
            else:
                visible[v_temp] = oculto[v_temp]
        else:
            visible[v_temp] = "_"

        if v_temp in flags:
            print(flags,visible[v_temp] is True,visible[v_temp],v_temp)
            # bloques.append(pos_jugador)
            if visible[jugador] == "F":
                visible[v_temp] = "_"
            else:
                visible[v_temp] = "F"

    #print(visible)

    return jugador, visible

def boom(jugador,bombas):
    """
    Verifica si en la selección había una bomba
    :param jugador: Posición jugador
    :param bombas: Posición Bombas
    :return:
    """
    if jugador in bombas:
        return True
    if jugador not in bloques:
        bloques.append(jugador)
    return False

def flag(visible,jugador,flags):
    """
    Plantar una bandera
    :return:
    """
    print("flags: ", flags)
    if jugador in flags:
        flags.remove(jugador)
    else:
        flags.append(jugador)
    print("flags: ", flags)

    return visible,flags

def settings(cant_minas,alto, ancho):
    """
    Configuraciones de juego
    :param cant_minas:
    :param alto:
    :param ancho:
    :return:
    """
    alto,ancho,minas = alto,ancho,cant_minas
    os.system("cls")
    print("*************************************************")
    print("                  Buscaminas")
    print("*************************************************")
    print()
    print()
    print("                   SETTINGS                ")
    print()
    print("          Ancho del tablero: {}".format(ancho_tab))
    print("          Alto del tablero: {}".format(alto_tab))
    print("          Cantidad de minas: {}".format(cant_minas))
    print()
    print()
    print()
    print("           Desea Configurarlo? (y/n)        ")
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
        print("                  Buscaminas")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("          Alto del tablero?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        alto = int(input())
        os.system("cls")

        print("*************************************************")
        print("                  Buscaminas")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("          Ancho del tablero?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        ancho = int(input())
        os.system("cls")

        print("*************************************************")
        print("                  Buscaminas")
        print("*************************************************")
        print()
        print()
        print("                   SETTINGS                ")
        print()
        print()
        print("          Cantidad de minas?")
        print()
        print()
        print()
        print()
        print("                   ")
        print()
        print("*************************************************")
        print()
        print("*************************************************")

        minas = int(input())
    os.system("cls")
    return minas,alto,ancho



    pass

def loose():
    """
    Tablero al perder
    """
    os.system("cls")

    print("*************************************************")
    print("                  Buscaminas")
    print("*************************************************")
    print()
    print()
    print("                    PERDISTE!                ")
    print()
    print("            ")
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
    time.sleep(3)
    os.system("cls")

def win():
    """
        Tablero al perder
        """
    os.system("cls")

    print("*************************************************")
    print("                  Buscaminas")
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
    print("          Presione Enter para empezar...         ")
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
    print("                  Buscaminas")
    print("*************************************************")
    print()
    print()
    print("                 BIENVENIDOS!                ")
    print()
    print("            ")
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

def menu():
    print("*************************************************")
    print("                  Buscaminas")
    print("*************************************************")
    print()
    print()
    print("                 BIENVENIDOS!                ")
    print()
    print("              1. Iniciar Juego")
    print("              2. Configuraciones")
    print("              3. Salir")
    print()
    print()
    print()
    print("            Seleccione una opción...         ")
    print()
    print("*************************************************")
    ask = input("")
    return ask

def pistas(screen,pixel_mezcla,alto, ancho):
    """
    De una lista de bombas, sale un diccionario con las pistas, bombas
    screen = Crea dos diccionarios, uno oculto y uno visible
    """

    pistas = {}
    pos_jugador = random.choice(pixeles)


    if screen == "oc":

        for i in range(1, ((alto_tab * ancho_tab) + 1)):
            pistas.setdefault(i, 0)

        for i in pixel_mezcla:

            if i > ancho: #arriba
                arriba = i-ancho
                pistas[arriba] += 1
                if i%ancho != 0: #arriba derecha
                    pistas[i-ancho+1] += 1

            if i%ancho != 0: #derecha
                pistas[i+1] += 1
                if i < ancho* (alto-1): #derecha abajo
                    pistas[i+ancho+1] +=1

            if i < ancho* (alto-1): #abajo
                pistas[i+ancho] += 1
                if i % ancho != 1: #abajo izquierda
                    pistas[i + (ancho -1)] += 1

            if i%ancho != 1: #izquierda
                pistas[i-1] += 1
                if i > ancho: #izquierda arriba
                    pistas[i - (ancho + 1)] +=1

        print()
        for i in pixel_mezcla:
            pistas[i] = 9

    else:
        for i in range(1, ((alto_tab * ancho_tab) + 1)):
            pistas.setdefault(i, "_")
        pistas[pos_jugador] = "X"
        return pistas, pos_jugador
    return pistas

def sort_minas(alto,ancho,minas,pixeles):
    """
    Sortea la posicion de las minas según los parametros
    :return:
    """
    pixel_mezcla = list(pixeles)  # MINASSSS!!!!
    random.shuffle(pixel_mezcla)
    for times in range((alto_tab * ancho_tab) - cant_minas):
        pixel_mezcla.pop()
    pixel_mezcla.sort()
    #print(pixel_mezcla)
    return pixel_mezcla




# Configuración tablero
alto_tab, ancho_tab = 10,10
cant_minas = 15

















#Tablero Visible
bloques = []
flags = []

pixel_mezcla = None



intro()
while True:
    opc = menu()
    validas = [1,2,3]
    if int(opc) in validas:
        if int(opc) == 3:
            break
        elif int(opc) == 2:
            cant_minas,alto_tab,ancho_tab = settings(cant_minas,alto_tab,ancho_tab) #Configuraciones


        elif int(opc) == 1:
            #Settings before starting the main loop
            pixeles = list(range(1, (alto_tab * ancho_tab) + 1))
            pixel_mezcla = sort_minas(alto_tab, ancho_tab, cant_minas,pixeles)
            oculto = pistas("oc", pixel_mezcla, alto_tab, ancho_tab)
            visible, pos_jugador = pistas("vis", pixel_mezcla, alto_tab, ancho_tab)

            left = len(pixeles)-len(pixel_mezcla)

            while True:
                os.system("cls")
                print("*************************************************")
                print("                  Buscaminas   Faltan barrer: {}".format(left))
                print("*************************************************")

                print(" (w/a/s/d)  -  move ")
                print("     b      -  barrer ")
                print("     f      -  plantar bandera ")
                print("     q      -  salir ")
                print()

                matriz_oculta = []

                #print("OCULTO:")

                count = 0
                for i in range(alto_tab):
                    matriz_oculta.append([])
                    for e in range(ancho_tab):
                        count += 1
                        matriz_oculta[i].append(oculto[count])

                #for i in matriz_oculta:
                #    for a in i:
                #        print(a, " ", end="")
                #    print()
                #print()

                matriz_visible = []


                count = 0
                for i in range(alto_tab):
                    matriz_visible.append([])
                    for e in range(ancho_tab):
                        count += 1
                        matriz_visible[i].append(visible[count])

                print("VISIBLE:")
                for i in matriz_visible:
                    print(" "*(len("*************************************************")-(ancho_tab*3)),end="")
                    for a in i:
                        print(a," ",end="")
                    print()
                print()
                #print(pos_jugador,pixel_mezcla,bloques)

                print("Seleccione un movimiento",end="")
                while True:
                    try:
                        mov = input("")
                    except ValueError:
                        print("Introduzca una letra .")
                    else:
                        break

                bomba = None
                bandera = None
                if mov.lower() == "b":
                    bomba = boom(pos_jugador,pixel_mezcla)
                    if bomba is True:
                        os.system("cls")
                        loose()
                        bloques = []
                        flags = []
                        break
                    left -= 1
                    if pos_jugador % ancho_tab != 1:
                        pos_jugador, visible = move(visible, oculto,flags, pos_jugador, "a", ancho_tab, alto_tab)
                    else:
                        pos_jugador, visible = move(visible, oculto,flags, pos_jugador, "d", ancho_tab, alto_tab)
                elif mov.lower() == "q":
                    break
                elif mov.lower() == "f":
                    visible, flags = flag(visible,pos_jugador,flags)
                    if pos_jugador % ancho_tab != 1:
                        pos_jugador, visible = move(visible, oculto,flags, pos_jugador, "a", ancho_tab, alto_tab)
                    else:
                        pos_jugador, visible = move(visible, oculto,flags, pos_jugador, "d", ancho_tab, alto_tab)
                else:
                    pos_jugador ,visible = move(visible,oculto,flags,pos_jugador,mov,ancho_tab,alto_tab)

                flags.sort()
                #print(flags,pixel_mezcla)
                if left == 0:
                    win()
                    bloques = []
                    flags = []
                    break




#DEF FUNCION SI TOCA EN UN LUGAR QUE NO HAY UNA BOMBA
#DEF FUNCION QUE SALVA BOMBAS
#DEF FUNCION GANADORA