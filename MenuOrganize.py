from MenuMain import *

import os
import shutil
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms

class MenuOrganize:

    def __init__(self, path):
        self.root = tk.Tk()
        self.root.geometry("400x250")

        self.path = path

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
            file_path = os.path.join(self.path, file)
            if file != "desktop.ini" and not os.path.isdir(file_path):
                file_extension = file.split(".")[len(file.split(".")) - 1]

                # Create folder if not exists
                folder_path = os.path.join(self.path, file_extension)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                src = file_path
                dst = os.path.join(folder_path, file)

                shutil.move(src, dst)

    def order_by_name(self):
        files = os.listdir(self.path)

        for file in files:
            file_path = os.path.join(self.path, file)
            if file != "desktop.ini" and not os.path.isdir(file_path):
                file_letter = file[0]

                # Create folder if not exists
                folder_path = os.path.join(self.path, file_letter)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                src = file_path
                dst = os.path.join(folder_path, file)

                shutil.move(src, dst)

    def order_by_date(self):
        files = os.listdir(self.path)

        for file in files:
            file_path = os.path.join(self.path, file)
            if file != "desktop.ini" and not os.path.isdir(file_path):
                unformatted_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y/%m/%d')
                formatted_date = unformatted_date.split('/')
                date = ""
                date += formatted_date[0] + "-" + formatted_date[1] + "-" + formatted_date[2]

                # Create folder if not exists
                folder_path = os.path.join(self.path, date)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                src = file_path
                dst = os.path.join(folder_path, file)

                shutil.move(src, dst)

    def order(self):
        option = self.combo.get()
        if option == "":
            ms.showwarning("Atención", "Selecciona una opción")
            return
        if option == "Por extensión (pdf, png, etc.)":
            self.order_by_extension()
        if option == "Por fecha":
            self.order_by_date()
        if option == "Orden alfabético":
            self.order_by_name()
        ms.showinfo("Atención", "Se han distribuidos los archivos de manera exitosa")