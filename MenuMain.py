from MenuOrganize import *
from MenuDownload import *

import tkinter as tk

class MenuMain:
    def __init__(self):
        self.root = tk.Tk()
        self.path = fd.askdirectory()

        self.root.title("Administrador de descargas")

        self.label = tk.Label(self.root, text="Administrador de descargas", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)

        self.button_downloads = tk.Button(self.root, text="Descargar Archivos", font=("Arial", 12), width=14, command=lambda: MenuDownload(self.path))
        self.button_downloads.pack(padx=10, pady=2)

        self.button_organizer = tk.Button(self.root, text="Organizar archivos", font=("Arial", 12), width=14, command=lambda: MenuOrganize(self.path))
        self.button_organizer.pack(padx=10, pady=2)

        self.button_exit = tk.Button(self.root, text="Salir", font=("Arial", 12), width=14, command=self.root.destroy)
        self.button_exit.pack(padx=10, pady=2)

        self.root.mainloop()