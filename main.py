import os
import requests
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox



def onClick(evento):
    eliminaCosas()
    carpeta=""
    if textoEtRt.get().lower()in ["musica","música"]:
        carpeta="Music"
    elif textoEtRt.get().lower() in ["videos","video"]:
        carpeta="Videos"
    elif textoEtRt.get().lower() in ["imagenes", "imágenes"]:
        carpeta = "Pictures"
    elif textoEtRt.get().lower() in ["documentos", "documento"]:
        carpeta = "Documents"
    elif textoEtRt.get().lower() in ["descargas","descarga"]:
        carpeta="Downloads"

def menu1():
    label.config(text="Introduce la URL a descargar")
    busquedaRuta=os.listdir(ruta+carpeta)
    tk.Label(ventana, text=f"Tus archivos y carpetas de {textoEtRt.get()} son:", font=("Helvetica", 25), fg="#0833a2").pack()
    for archivo in busquedaRuta:
        if archivo!="desktop.ini":
            tk.Label(ventana, text=f"{archivo}", font=("Helvetica", 20)).pack()

def eliminaCosas():
    cont=0
    for cosa in ventana.winfo_children():
        if cont>1:
            cosa.destroy()
        cont+=1

def borrame(evento):
    for cosa in ventana.winfo_children():
        cosa.destroy()

def logic1():
    url = entry.get()
    if url == "":
        messagebox.showerror("Error", "Introduce una URL")
        return

    try:
        nombre_archivo=url.split("/")[-1]
        respuesta=requests.get(url)
        respuesta.raise_for_status()
        with open(nombre_archivo,"wb") as f:
            f.write(respuesta.content)
        messagebox.showinfo("Exito", f"Descarga exitosa en:\n{os.path.join(os.getcwd(),nombre_archivo)}")
    except Exception as e:
        messagebox.showerror("Error", f"No se puede descargar:\n{e}")


# Obtiene la ruta base del usuario
usuario=os.getcwd()
div=[""+usuario.split("\\")[i]+"\\" for i in range(3)]
ruta=""
for dato in div:
    ruta+=dato


ventana.title("Administrador de descargas")
ventana.geometry("700x700")
ventana.config(bg="#ffffff",cursor="man")

tk.Label(ventana,text="Introduzca la carpeta que quiera ver",font=("Serif",25)).pack()
textoEtRt=tk.StringVar()
entradaRuta=tk.Entry(ventana,textvariable=textoEtRt)
entradaRuta.pack()
ventana.bind("<Return>",onClick)
ventana.bind("<Button-3>",borrame)


label=tk.Label(ventana,text="")
label.pack(pady=10)

entry=tk.Entry(ventana,width=50)
entry.pack(pady=5)

boton=tk.Button(ventana,text="Descargar", command=logic1)
boton.pack(pady=10)
menu1()


ventana.mainloop()
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
