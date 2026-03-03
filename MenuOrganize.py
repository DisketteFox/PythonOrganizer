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

    def order_by_name(self):
        files = os.listdir(self.path)

        for file in files:
            if file != "desktop.ini" and not os.path.isdir(self.path + file):
                file_letter = file[0]

                # Create folder if not exists
                if not os.path.exists(self.path + file_letter):
                    os.mkdir(self.path + file_letter)

                src = self.path + file
                dst = self.path + file_letter + "/" + file

                shutil.move(src, dst)

    def order_by_date(self):
        files = os.listdir(self.path)

        for file in files:
            if file != "desktop.ini" and not os.path.isdir(self.path + file):
                unformatted_date = datetime.datetime.fromtimestamp(os.path.getctime(self.path + file)).strftime('%Y/%m/%d')
                formatted_date = unformatted_date.split('/')
                date = ""
                date += formatted_date[0] + "-" + formatted_date[1] + "-" + formatted_date[2]

                # Create folder if not exists
                if not os.path.exists(self.path + date):
                    os.mkdir(self.path + date)

                src = self.path + file
                dst = self.path + date + "/" + file

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