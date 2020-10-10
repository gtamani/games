

import random
import time
import os


os.system("cls")
print("Bienvenidos a Muertos y Heridos!")
time.sleep(2)
print("Yo pensaré un número de 4 digitos y usted tendrá que adivinarlo")
time.sleep(3)
print("Le daré pistas cuando haya muertos o heridos")
time.sleep(2)
print("Qué es un muerto? Un número que esta en la posición correcta y digito correcto")
time.sleep(4)
print("Y un herido? Un digito que es correcto pero que no está en la posición correcta")
time.sleep(4)
print("Deberá escribir un numero de 4 digitos DISTINTOS y le daré la devolución")
time.sleep(4)
print("Son 15 intentos. Buena Suerte!")
time.sleep(2)
print("Enter para empezar")


input()
os.system("cls")

numero = []
intento = 1
opc = ""
salir = False
intentos = []
#Creamos el número random de 4 digitos sin repetir
while len(numero) < 4:
    switch = "on"
    a = random.randint(0,9)
    for i in range(len(numero)):
        if a == numero[i]:
            switch = "off"
    if switch == "on":
        numero.append(a)


print("Ya tengo un número en mente")


while intento <16 or opc == numero or salir == "on":
    print()
    print("N para salir".center(50))
    print()
    muertos = 0
    heridos = 0
    while True or salir !="on": #Obtener número con las condiciones dadas
        switch = "on"
        opc = list(input("Intento nº{}: Introduzca un número de 4 dígitos sin repetir: ".format(intento)))
        if opc[0].lower() != "n":
            comp = list(opc)
            if len(opc) == 4:
                for i in opc:
                    if i.isnumeric() == False:
                        switch = "off"
                for x in range(len(opc)):
                    count = 0
                    for z in range(len(comp)):
                        if comp[x] == opc[z]:
                            count += 1
                    if count != 1:
                        switch = "off"
            else:
                switch = "off"
        else:
            salir = True
            break
        if switch != "on" or switch == True:
            os.system("cls")
            print("Número no válido. ",end="")
        else:
            break

    if switch == True:
        break
    else:

        os.system("cls")

        for i in range(len(opc)):
            opc[i] = int(opc[i])

        for m in range(len(numero)):
            for n in range(len(opc)):
                if numero[m] == opc[n]:
                    if m==n:
                        muertos += 1
                    else:
                        heridos += 1

        intentos.append([opc,muertos,heridos])
        if muertos != 4:
            print()
            print("----------INTENTOS----------".center(50))
            for i in range(len(intentos)):
                print("Intento {}= {}{}{}{}  {} muerto(s), {} herido(s)".format(i+1,intentos[i][0][0],intentos[i][0][1],intentos[i][0][2],intentos[i][0][3],intentos[i][1],intentos[i][2]).center(50))
                print("----------------------------".center(50))
        else:
            break

        intento +=1



    #print("se acabó")

if opc == numero:
    print()
    print("Ganaste en {} intentos. Excelente! ".format(intento))
else:
    print()
    print("Te quedaste sin intentos. El número era {}.".format(numero[0],numero[1],numero[2],numero[3]))
