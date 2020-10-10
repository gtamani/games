#Proyecto de block de notas
import os,time

notes_cant = None

def display():
    """
    Muestra las notas disponibles y el menú de opciones
    """
    notas_ind = []
    print("----------------------------------------")
    path = "files/notes/01_índice.txt"
    if os.path.exists(path):

        print("           NOTAS DISPONIBLES")
        archivo = open(path,"r",encoding="utf-8")
        notas_ind = archivo.readlines()
        for i in range(len(notas_ind)):
            notas_ind[i] = notas_ind[i].replace("\n","")
        for i in range(len(notas_ind)):

            new = notas_ind[i].replace("\n","").replace(".txt","")
            print("       Nota ",i+1,": ",new)
        notes_cant = len(notas_ind)

    else:
        print("No hay notas disponibles por el momento")
    print("----------------------------------------")


    print()
    print("          1. Crear nota!")
    print("          2. Leer nota!")
    print("          3. Cambiar nombre")
    print("          4. Eliminar Nota")
    print("          5. Salir")
    print()
    return notas_ind


def crear_nota():
    while True:
        name = input("Introduce el nombre de la nota: ")
        file_name = "files/notes/"+ name + ".txt"
        if os.path.exists(file_name):
            print("Ese nombre ya existe.")
            time.sleep(1)
        else:
            break
    os.system("cls")
    content = ""
    print("---------------",name+".py","---------------")
    print()
    while True:
        renglon = input("Introduce un renglón (q para guardar y salir): ")
        if renglon != "q":
            content += renglon
            content += "\n"

        else:
            break
    with open(file_name,"w",encoding="utf-8") as archivo:
        archivo.write(content)
    with open("files/notes/01_índice.txt","a",encoding="utf-8") as archivo:
        archivo.write(name+"\n")
    os.system("cls")

def leer_nota(lista):
    """
    :lista: Cantidad de notas en carpeta
    """
    ask = int(input("Inserte el número de nota --> "))
    if ask > 0 or ask < len(lista):
        os.system("cls")
        abrir = "files/notes/" + lista[ask-1].strip() + ".txt"
        print()
        with open(abrir,"r",encoding="utf-8") as archivo:
            print(archivo.read())

            input("Presiona una tecla para volver al menú.")
            os.system("cls")
    else:
        print("No existe esa nota")
        time.sleep(2)

def cambiar_nombre(lista):
    while True:
        switch = "off"
        nota = input("Introduce el número de nota a cambiar: ")
        for i in range(len(lista)):
            if int(nota) == (i+1):
                switch = "on"
        if switch == "on":
            nota = int(nota)
            break

    if ask > 0 or ask < len(lista):
        print("Introduce el nuevo nombre para {}".format(lista[nota-1]),end="")
        while True:
            new = input("--->")
            if os.path.exists("files/notes/"+new+".txt"):
                print("Ese nombre ya existe...")
                time.sleep(1)
            else:
                break
        print(lista[nota-1])
        os.rename("files/notes/"+lista[nota-1].replace("\n","")+".txt","files/notes/"+new+".txt")
        lista[nota - 1] = new
        with open("files/notes/01_índice.txt", "w", encoding="utf-8") as archivo:
            for i in range(len(lista)):
                archivo.write(lista[i] + "\n")

        print("Nombre cambiado!")

def eliminar(lista):
    ask = int(input("Qué nota desea eliminar? "))
    for i in range(len(lista)):
        print(i)
        if ask == int(i+1):
            path = "files/notes/" + lista[i] + ".txt"
            if os.path.exists(path):
                os.remove(path)
                lista.pop(i)
        else:
            print("No existe esa nota")

        with open("files/notes/01_índice.txt", "w", encoding="utf-8") as archivo:
            for i in range(len(lista)):
                archivo.write(lista[i] + "\n")

        print("Eliminado!")


    return lista








while True:
    os.system("cls")
    cant = display()
    ask = int(input(" Elige una opción --> "))
    if ask == 1:
        crear_nota()
    elif ask == 2:
        leer_nota(cant)
    elif ask == 3:
        cambiar_nombre(cant)
    elif ask == 4:
        cant = eliminar(cant)
    elif ask == 5:
        break





