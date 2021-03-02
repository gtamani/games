import random
import os
import time

class Hipodromo:

    def __init__(self,nombre,cantidad,largo,estilo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.largo = largo
        self.estilo = estilo

        self.caballos = list()
        self.rapidos = list()

        for i in range(cantidad):
            nombre = random.choice(list("abcdefghijklmnopqrstuvwxyz"))
            velocidad = random.choice([2,3,3,3,4,4,4,5])
            if velocidad in [4,5]:
                self.rapidos.append(nombre)

            self.caballos.append(Caballo(nombre,velocidad))

    def __str__(self):
        return "{}, {} caballos, {} metros.".format(self.nombre,self.cantidad,self.largo)

class Caballo:

    def __init__(self,nombre,velocidad,posicion = 1):
        self.nombre = nombre
        self.velocidad = velocidad
        self.posicion = posicion
        self.puesto = None

    def __str__(self):
        return self.nombre

    def avanzar(self,largo):
        avanza = random.choice([self.velocidad-1,self.velocidad,self.velocidad+1])
        if self.posicion + avanza >= largo-1:
            self.posicion = largo-1
        else:
            self.posicion += avanza

def menu():
    print("Seleccione el estadio                Disponible: $",money)
    print()
    for i in range(len(estadios)):
        print("--> ",i+1,". ",estadios[i])
    print()
    while True:
        opcion = input("___")
        if opcion in ["1","2","3","4","q"]:
            break
    os.system("cls")
    return opcion

def mostrar_estadio(estadio,apuesta=None,apostado=None):
    global estadios,money
    hip = estadios[estadio]
    puesto = 1
    winner = None


    while True:
        print("                                     Disponible: $",money)
        for i in range(len(hip.caballos)):
            for a in range(hip.largo):
                if a == hip.caballos[i].posicion:
                    print(hip.caballos[i].nombre,end=" ")
                elif a == (hip.largo - 2):
                    print("| ",end="")
                else:
                    print(hip.estilo,end=" ")
            if hip.caballos[i].puesto is not None:
                print("Puesto nº{}".format(hip.caballos[i].puesto),end="")
            print()
        print()
        print("Los caballos favoritos de hoy son: ",end="")
        for i in estadios[estadio].rapidos:
            print(i,end=" ")
        print()

        while apuesta == None:
            apuesta = input("Haga sus apuestas: ")
            if apuesta in estadios[estadio].caballos:
                break
        while apostado == None:
            apostado = int(input("Cuanto apuesta? "))
            if apostado <= money:
                break

        time.sleep(0.75)
        os.system("cls")


        for i in hip.caballos:
            if i.posicion >= hip.largo-1:
                if i.puesto is None:
                    if puesto == 1:
                        winner = i.nombre
                    i.puesto = puesto
                    puesto += 1
            i.avanzar(hip.largo)

        if puesto == hip.cantidad+1:
            puesto += 1
            if winner == apuesta:
                apostado *= (hip.largo / 40)
                print("Ha ganado la apuesta!!! +${}".format(apostado))

                money += int(apostado)
            else:
                print("Ha perdido la apuesta!!! -${}".format(apostado))
                money -= int(apostado)
            time.sleep(2)
            break

money = 2000
estadios = list()

os.system("mode 160")

while True:
    if money == 0:
        print("No tiene más dinero, vuelva pronto!")

    estadios = [Hipodromo("Hipodromo de La Plata", 6, 40, "."), Hipodromo("Hipodromo de Palermo", 8, 50, "-"),
                Hipodromo("Hipodromo Independencia", 10, 60, ","), Hipodromo("Hipodromo San Isidro", 12, 70, "'")]
    opcion = menu()
    if opcion == "q":
        break
    mostrar_estadio(int(opcion)-1)



