import os
import shutil
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

class MenuOrganize:

    def divideXtipos(self):
        self.borraFrames()
        ruta = "C:\\Users\\Usuario\\Downloads\\"
        busquedaRuta = os.listdir(ruta)
        respueta=tk.LabelFrame(self.root)
        for archivo in busquedaRuta:
            if archivo != "desktop.ini":
                tipoArchivo = archivo.split(".")[len(archivo.split(".")) - 1]
                src = os.path.join(ruta, archivo)  # origen
                print("ruta de inicio ", src)
                dst = os.path.join(os.getcwd() + "\\" + f"archivos de tipo {tipoArchivo}")  # destino
                print("ruta de destino ", dst)
                if not os.path.exists(ruta + archivo + tipoArchivo):
                    try:
                        # esta vaina crea directamente en el python toca que se cree en el lugar especificado.
                        os.mkdir(f"archivos de tipo {tipoArchivo}")
                    except Exception:
                        print()
                shutil.copy(src, dst)
        tk.Label(respueta, text="Se han distribuidos los archivos de manera exitosa.", font=("Arial", 16)).pack(pady=20)
        respueta.pack()

    def ordenAlfabetico(self):
        self.borraFrames()
        ruta = "C:\\Users\\User_yo\\Downloads\\"
        busqueda_ruta = os.listdir(ruta)
        respuesta=tk.LabelFrame(self.root)
        for archivo in busqueda_ruta:
            if archivo != "desktop.ini":
                tk.Label(respuesta, text=f"{archivo}", font=("Arial", 18)).pack(pady=10)
        respuesta.pack()

    def ordenXFecha(self):
        self.borraFrames()
        ruta = "C:\\Users\\User_yo\\Downloads\\"
        busqueda_ruta = os.listdir(ruta)
        respuesta=tk.LabelFrame(self.root)
        # bucle con un if que agrega fecha y el nombre del archivo, medio volado andava creando esto y creativo
        lista_fechas=[datetime.datetime.fromtimestamp(os.path.getctime(ruta + archivo)).strftime('%Y/%m/%d %H:%M')+" "+archivo for archivo in busqueda_ruta if archivo!="desktop.ini"]
        lista_fechas.sort(reverse=True)
        for archivo in lista_fechas:
            tk.Label(respuesta, text=f"{archivo}", font=("Arial", 18)).pack(pady=10)
        respuesta.pack()

    def borraFrames(self):
        for hijo in self.root.winfo_children():
            if hijo.widgetName=="labelframe":
                hijo.destroy()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")

        '''self.root.title("Administrador de descargas")

        self.label = tk.Label(self.root, text="Introduce la carpeta que quieras ver", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)
        self.input_box = tk.Entry(self.root)
        self.input_box.pack(padx=20, pady=20)'''

        tk.Label(self.root, text="¿Cómo quieres organizar los archivos?", font=("Arial", 16)).pack(pady=20)
        opciones = [
            "Por extensión (pdf, png, etc.)",
            "Por fecha",
            "Orden alfabético"
        ]

        combo = ttk.Combobox(self.root, values=opciones, state="readonly", width=30)
        combo.pack(pady=10)

        def mostrar_seleccion():
            seleccion = combo.get()
            if seleccion == "":
                ms.showwarning("Atención", "Selecciona una opción")
                return

            if seleccion=="Por extensión (pdf, png, etc.)":
                self.divideXtipos()
            if seleccion=="Por fecha":
                self.ordenXFecha()
            if seleccion=="Orden alfabético":
                self.ordenAlfabetico()

        tk.Button(self.root, text="Aplicar", command=mostrar_seleccion).pack(pady=10)
        self.salir = tk.Button(self.root, text="Volver", font=("Arial", 12), command=self.root.destroy)
        self.salir.pack()

        self.root.mainloop()