import os,time,random

def clean():
    """
    Borrar pantalla
    """
    os.system("cls")

def login():
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        1. Iniciar Sesión")
    print("        2. Registrarse")
    print()
    print("        3. Salir")
    print()
    while True:
        ask = int(input(""))
        poss = [1,2,3]
        if ask not in poss:
            print("No existe esa opción")
        else:
            return ask

def iniciar_sesion():
    """
    Entrar en sistema con datos guardados
    :return: True/False (acceso denegado)
    """
    user = input("Usuario: ")
    password = input("Contraseña: ")
    path_users = "files/test_game/users.txt"
    path = "files/test_game/" + user + ".txt"
    if os.path.exists(path_users):
        with open(path_users,"r",encoding="utf-8") as archivo:
            users = archivo.readlines()
            asd = 0
            for i in range(len(users)):
                users[i] = users[i].replace("\n","")
                if user == users[i]:
                    with open(path,"r",encoding="utf-8") as archivo:
                        datos = archivo.readlines()
                        pass_ver = datos[0].replace("\n","")
                        if pass_ver == password:
                            return user, True
                        else:
                            asd = 1
            if asd == 1:
                print("No coincide usuario y contraseña.")
            else:
                print("No existe ese usuario. Pruebe con registrarse.")
            time.sleep(3)
            os.system("cls")
            return None, False
    else:
        print("No existe ese usuario. Pruebe con registrarse.")
        time.sleep(3)
        return None, False



def registrarse():
    """
    Crear usuario y contraseña

    Archivo creado:
    renglón 1: contraseña
    renglón 2: partidas jugadas
    renglón 3: puntaje máximo
    renglón 4: promedio puntuación
    """
    while True:
        user = input("Usuario: ")
        path = "files/test_game/" + user + ".txt"
        if os.path.exists(path):
            print("'{}' ya existe. Intente con otro...".format(user))
        else:
            break
    path_users = "files/test_game/users.txt"
    while True:
        password = input("Contraseña: ")
        if len(password) > 5:
            break
        else:
            print("Prueba con una contraseña de al menos 6 caracteres")

    with open(path,"w",encoding="utf-8") as archivo:
        archivo.write(password+"\n"+"0"+"\n"+"0"+"\n"+"0")
    with open(path_users,"a",encoding="utf-8") as archivo:
        archivo.write(user+"\n")
    print("Usuario creado!")
    time.sleep(2)


    pass

#------------------------------------------------------------
def game_screen():
    """
    Mostrar el menú de juego
    :return: Opción elegida
    """
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        1. Jugar!")
    print("        2. Ver Puntuaciones")
    print()
    print("        3. Volver")
    print()
    while True:
        ask = int(input("--> "))
        poss = [1,2,3]
        if ask not in poss:
            print("No existe esa opción")
        else:
            return ask


def play(user):
    """
    Hacer el desarrollo del juego
    :return:
    """
    os.system("cls")
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        ")
    print("       Preparando preguntas...")
    print()
    print()
    print()
    time.sleep(2)
    os.system("cls")
    score = 0
    for veces in range(10):
        win = False
        num1,signo = random.randint(0,100),random.choice(["+","-"])
        if signo == "-":
            num2 = random.randint(0,num1)
            respuesta = num1 - num2
        elif signo == "+":
            num2 = random.randint(0, 100)
            respuesta = num1 + num2

        print("------------------------------------")
        print(" PREGUNTA {}/10           SCORE {}  ".format(veces + 1, score))
        print("------------------------------------")
        print()
        print("        ")
        print("        {}  {}  {} =  ?".format(num1, signo, num2))
        print()
        print()

        while True:
            resp = input()
            if resp.isdigit():
                resp = int(resp)
                break

        print(respuesta,resp)

        if respuesta == resp:
            win = True

        os.system("cls")

        print("------------------------------------")
        print("            MATH TEST")
        print("------------------------------------")
        print()
        print()

        if win is True:
            print("              CORRECTO!                 ")
            print()
            score += 1
        else:
            print("             INCORRECTO!                 ")
            print("         La respuesta era {}".format(respuesta))
        print()
        print()

        time.sleep(2)
        os.system("cls")


    os.system("cls")
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        ")
    print("        Obtuviste {} puntos!".format(score))
    print()
    print()
    print()
    time.sleep(2)
    os.system("cls")
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        ")
    print("      Guardando datos en sistema...".format(score))
    print()
    print()
    print()
    time.sleep(2)

    path = "files/test_game/" + user + ".txt"
    contraseña, intentos, puntaje, media = datos(path)
    if score > puntaje:
        puntaje = score
    media = ((media*intentos)+score)/(intentos+1)
    intentos += 1

    with open(path,"w",encoding="utf-8") as archivo:
        archivo.write(contraseña+"\n"+str(intentos)+"\n"+str(puntaje)+"\n"+str(media)+"\n")











def seguir_jugando():
    """
    Establecer si sigue en el loop de juego o no
    :return: Respuesta True/Fale
    """
    os.system("cls")
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        ")
    print("       Desea seguir jugando?")
    print("              (Y/N)")
    print()
    print()
    opciones = ["y","Y","n","N"]
    while True:
        ask = input()
        if ask in opciones:
            if ask.lower() == "y":
                return True
            if ask.lower() == "n":
                return False






def scoring(user):
    """
    Mostrar en pantalla los puntajes del usuario
    * Intentos
    * Máximo Puntaje
    * Promedio puntos
    :return:
    """
    os.system("cls")
    path = "files/test_game/" + user + ".txt"
    contraseña,intentos,puntaje,media = datos(path)
    print("------------------------------------")
    print("             PUNTAJES")
    print("------------------------------------")
    print()
    print("        Jugadas:",intentos)
    print("        Máximo Puntaje:",puntaje)
    print("        Promedio Puntaje:",media)
    print()
    print(" Presione una tecla para salir ( ... )")
    input()
    os.system("cls")

def datos(path):
    """
    Recolecta los datos personales
    """
    with open(path,"r",encoding="utf-8") as archivo:
        datos = archivo.readlines()
        contraseña = datos[0].replace("\n","")
        intentos = int(datos[1].replace("\n",""))
        puntaje = int(datos[2].replace("\n", ""))
        media = float(datos[3].replace("\n", ""))
        return contraseña,intentos,puntaje,media

def adios():
    os.system("cls")
    print("------------------------------------")
    print("            MATH TEST")
    print("------------------------------------")
    print()
    print("        ")
    print("           Vuelva Pronto!        ")
    time.sleep(3)




#Estructura de funciones
while True:
    clean()
    opc = login()
    if opc == 1:
        user, log_in = iniciar_sesion()
        if log_in:
            while True:
                clean()
                opc = game_screen()
                if opc == 1:
                    clean()
                    while True:

                        play(user)
                        ask = seguir_jugando()
                        if ask is False:
                            break
                if opc == 2:
                    scoring(user)
                if opc == 3:
                    break
    elif opc == 2:
        registrarse()
    elif opc == 3:
        adios()
        break

