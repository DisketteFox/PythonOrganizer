import os
import shutil
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

class MenuOrganize:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")

        # self.path = "C:\\Users\\Usuario\\Downloads\\"
        self.path = "/home/miles/Documents/example/"

        tk.Label(self.root, text="¿Cómo quieres organizar los archivos?", font=("Arial", 16)).pack(pady=20)
        opciones = [
            "Por extensión (pdf, png, etc.)",
            "Por fecha",
            "Orden alfabético"
        ]

        self.combo = ttk.Combobox(self.root, values=opciones, state="readonly", width=30)
        self.combo.pack(pady=10)

        self.button = tk.Button(self.root, text="Aplicar", command=self.order)
        self.button.pack(pady=10)

        self.button_exit = tk.Button(self.root, text="Volver", font=("Arial", 12), command=self.root.destroy)
        self.button_exit.pack()

        self.root.mainloop()

    def order_by_extension(self):
        files = os.listdir(self.path)

        for file in files:
            if file != "desktop.ini" and not os.path.isdir(self.path + file):
                file_extension = file.split(".")[len(file.split(".")) - 1]

                # Create folder if not exists
                if not os.path.exists(self.path + file_extension):
                    os.mkdir(self.path + file_extension)

                src = self.path + file
                dst = self.path + file_extension + "/" + file

                shutil.move(src, dst)
        ms.showinfo("Atención", "Se han distribuidos los archivos de manera exitosa")

    def ordenAlfabetico(self):
        self.borraFrames()
        busqueda_ruta = os.listdir(self.path)
        respuesta=tk.LabelFrame(self.root)
        for archivo in busqueda_ruta:
            if archivo != "desktop.ini":
                tk.Label(respuesta, text=f"{archivo}", font=("Arial", 18)).pack(pady=10)
        respuesta.pack()

    def ordenXFecha(self):
        self.borraFrames()
        busqueda_ruta = os.listdir(self.path)
        respuesta=tk.LabelFrame(self.root)
        # bucle con un if que agrega fecha y el nombre del archivo, medio volado andava creando esto y creativo
        lista_fechas=[datetime.datetime.fromtimestamp(os.path.getctime(self.path + archivo)).strftime('%Y/%m/%d %H:%M')+" "+archivo for archivo in busqueda_ruta if archivo!="desktop.ini"]
        lista_fechas.sort(reverse=True)
        for archivo in lista_fechas:
            tk.Label(respuesta, text=f"{archivo}", font=("Arial", 18)).pack(pady=10)
        respuesta.pack()

    def borraFrames(self):
        for hijo in self.root.winfo_children():
            if hijo.widgetName=="labelframe":
                hijo.destroy()

    def order(self):
        option = self.combo.get()
        if option == "":
            ms.showwarning("Atención", "Selecciona una opción")
            return
        if option == "Por extensión (pdf, png, etc.)":
            self.order_by_extension()
        if option == "Por fecha":
            self.ordenXFecha()
        if option == "Orden alfabético":
            self.ordenAlfabetico()