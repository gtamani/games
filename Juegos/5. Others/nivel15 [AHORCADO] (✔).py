import random
import os
import time

palabras = ["armario","escalera","relampago","sal","azucar","bateria","salame","puerta",
            "latigo","sanatorio","bandera","ladrillo","espada","recinto","bicicleta","baldosa",
            "asterisco","corneta","diente","elite","fogata","garganta","hemisferio","interino",
            "jabali","karate","lampara","monitor","nauseas","ostra","parlante","quimera",
            "laberinto","marmota","narciso","reliquia","serpiente","tractor","ultimo","velero",
            "zimbabwe","artrosis","bendicion","cascara","daltonico","eufemismo","fantasia","geografia",
            "historia","kerosene","idolo","jauria","lustro","mentira","necio","pendulo",
            "diagnostico","infantil","ligamento","miembro","nervio","artritis","coyuntura",
            "cirugia","dosis","herencia","higiene","vegija","toxico","rotula","procedimiento",
            "postura","vacuna","corona","protesis","adn","electrocardiograma","transportista",
            "transgresor","caleidoscopio","idioma","jerga","cientifico","trampa","torpeza"
            "estimacion","persona","mecanismo","responsable","articulacion","imagen","verbo"]

pal = [letra.upper() for letra in random.choice(palabras)]
pal_mostrar = ["_" for i in pal]
intentos = 0
conf = ""
acierto = False
elegidas = []


while True:
    acierto = False
    if intentos == 0:
        print("           _____        ")
        print("                \       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    if intentos == 1:
        print("           _____        ")
        print("          O     \       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    elif intentos == 2:
        print("           _____        ")
        print("        __O     \       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    elif intentos == 3:
        print("           _____        ")
        print("        __O__   \       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    elif intentos == 4:
        print("           _____        ")
        print("        __O__   \       ")
        print("          |     N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    elif intentos == 5:
        print("           _____        ")
        print("        __O__   \       ")
        print("          |     N       ")
        print("           \    N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")
    elif intentos == 6:
        print("           _____        ")
        print("        __O__   \       ")
        print("          |     N       ")
        print("         / \    N       ")
        print("                N       ")
        print("                N       ")
        print("                N       ")
        print("          ______N__     ", end="")


    print("   PALABRA:  ",end ="")
    for i in pal_mostrar:
        print(i,end=" ")
    print()
    print("      ",end="")

    print()
    letra = input("          Inserte una letra: ").upper()
    if letra.isalpha() and len(letra) == 1:
        if letra not in elegidas:
            if letra in pal:
                acierto = True
                for orden in [i for i in range(len(pal)) if pal[i] == letra]:
                    pal_mostrar[orden] = letra
            elegidas.append(letra)
        else:
            print("         Ya elegiste esa letra!")
            time.sleep(1)
            acierto = True



    #print(elegidas)
    #print(pal)
    #print(pal_mostrar)


    os.system("cls")



    if acierto is False:
        intentos +=1
    if all([False for i in pal_mostrar if i == "_"]):
        print("\n"*4)
        print("                      Ganaste!")
        print()
        print("                       ",end="")
        for i in pal:
            print(i,end="")
        print()

        time.sleep(2)
        os.system("cls")
        intentos = 0
        pal = [letra.upper() for letra in random.choice(palabras)]
        pal_mostrar = ["_" for i in pal]
        elegidas = []

    if intentos == 7:
        print("\n" * 4)
        print("            Perdiste! La palabra era ",end="")
        for i in pal:
            print(i,end="")
        print()

        time.sleep(2)
        os.system("cls")
        intentos = 0
        pal = [letra.upper() for letra in random.choice(palabras)]
        pal_mostrar = ["_" for i in pal]
        elegidas = []
