import os
import requests
import tkinter as tk
from tkinter import filedialog,messagebox


def menu0():
    print("Administrador de descargas")
    print("1. Descargar archivo")
    print("2. Organizar descargas")
    print("3. Administrar copias de seguridad")
    print("4. Salir")

def menu1():
    label.config(text="Introduce la URL a descargar")

def menu2():
    print("1. Orden alfabético")
    print("1. Orden de descarga")

def menu3():
    print("1. Realizar copia de seguridad")
    print("2. Recuperar archivo corrupto")

def logic1():
    url = entry.get()
    if url == "":
        messagebox.showerror("Error", "Introduce una URL")
        return
    carpeta=filedialog.askdirectory(title="Selecciona la carpeta de destino")
    if not carpeta:
        messagebox.showwarning("cancelado","No seleccionaste ninguna carpeta")
        return

    try:
        nombre_archivo=url.split("/")[-1]
        ruta_completa=os.path.join(carpeta,nombre_archivo)
        respuesta=requests.get(url)
        respuesta.raise_for_status()
        with open(ruta_completa,"wb") as f:
            f.write(respuesta.content)
        messagebox.showinfo("Exito", f"Descarga exitosa en:\n{ruta_completa}")
    except Exception as e:
        messagebox.showerror("Error", f"No se puede descargar:\n{e}")


ventana=tk.Tk()
ventana.title("Administrador de descargas")
ventana.geometry("400x200")
ventana.config(cursor="pirate")

label=tk.Label(ventana,text="")
label.pack(pady=10)

entry=tk.Entry(ventana,width=50)
entry.pack(pady=5)

boton=tk.Button(ventana,text="Descargar", command=logic1)
boton.pack(pady=10)
menu1()
ventana.mainloop()

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

