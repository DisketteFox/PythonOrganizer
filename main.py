import os

def menu0():
    print("Administrador de descargas")
    print("1. Descargar archivo")
    print("2. Organizar descargas")
    print("3. Administrar copias de seguridad")
    print("4. Salir")

def menu1():
    print("Introduce la url a descargar")

def menu2():
    print("1. Orden alfabético")
    print("1. Orden de descarga")

def menu3():
    print("1. Realizar copia de seguridad")
    print("2. Recuperar archivo corrupto")

def logic1():
    menu1()
    url = input(">> ")

    os.system(f"wget {url}")

def logic2():
    print("")

def logic3():
    menu3()
    opt = int(input(">> "))

    if opt == 1:
        print("")
    else:
        print("")

def main():
    loop = True

    while (loop):
        menu0()
        opt = int(input(">> "))

        if opt == 1:
            logic1()
        elif opt == 2:
            logic2()
        elif opt == 3:
            logic3()
        else:
            loop = False

main()