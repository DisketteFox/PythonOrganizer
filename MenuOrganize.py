import os
import tkinter as tk
import shutil
from tkinter import ttk
from tkinter import messagebox as ms

class MenuOrganize:

    def divideXtipos(self):
        ruta = "C:\\Users\\Usuario\\Downloads\\"
        busquedaRuta = os.listdir(ruta + self.input_box.get())
        tk.Label(self.root, text=f"Tus archivos y carpetas de {self.input_box.get()} son:", font=("Helvetica", 25),
                 fg="#0833a2").pack()
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

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Administrador de descargas")

        self.label = tk.Label(self.root, text="Introduce la carpeta que quieras ver", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.input_box = tk.Entry(self.root)
        self.input_box.pack(padx=20, pady=20)

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



        tk.Button(self.root, text="Aplicar", command=mostrar_seleccion).pack(pady=10)
        self.salir = tk.Button(self.root, text="Volver", font=("Arial", 12), command=self.root.destroy)
        self.salir.pack()


        self.root.mainloop()