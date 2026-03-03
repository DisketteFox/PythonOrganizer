import os
import tkinter as tk

def onClick(event):
    print("se ha presionado ",event.widget["text"])

ventana=tk.Tk()
ventana.title("Organizador de archivos")
ventana.geometry("850x750")
frame1=tk.Frame(ventana,height=200)
frame1.config(bg="blue",cursor="pirate")
frame1.pack(side="left",anchor="nw",fill="x",expand=1)
etiquetas=[tk.Label(frame1,text=f"texto {i+1} en el frame 1") for i in range(4)]

for etiqueta in etiquetas:
    etiqueta.pack()
    etiqueta.bind("<Button-1>",onClick)



ventana.mainloop()