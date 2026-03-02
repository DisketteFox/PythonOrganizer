import os
import tkinter as tk
from tkinter import filedialog as fd


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

# Obtiene la ruta base del usuario
usuario=os.getcwd()
div=[""+usuario.split("\\")[i]+"\\" for i in range(3)]
ruta=""
for dato in div:
    ruta+=dato


ventana=tk.Tk()
ventana.geometry("700x700")
ventana.config(bg="#ffffff",cursor="man")

tk.Label(ventana,text="Introduzca la carpeta que quiera ver",font=("Serif",25)).pack()
textoEtRt=tk.StringVar()
entradaRuta=tk.Entry(ventana,textvariable=textoEtRt)
entradaRuta.pack()
ventana.bind("<Return>",onClick)
ventana.bind("<Button-3>",borrame)


ventana.mainloop()