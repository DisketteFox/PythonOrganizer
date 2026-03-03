import os
import subprocess

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd

import requests


class MenuDownload:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title("Administrador de descargas")

        self.path = path

        self.label = tk.Label(self.root, text="Introduce la URL", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)

        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=10)

        self.button_download = tk.Button(self.root, text="Descargar", font=("Arial", 12))
        self.button_download.bind("<Button-1>", self.download)
        self.button_download.pack()

        self.button_download = tk.Button(self.root, text="Volver", font=("Arial", 12), command=self.root.destroy)
        self.button_download.pack()

        self.root.mainloop()

    def show_message(self, event):
        print(self.entry.get())

    def download_WGET(self, event):
        subprocess.run(['wget', self.entry.get()])

    def download(self, event):
        url = self.entry.get()

        if url == "":
            mb.showerror("Error", "Introduce una URL")
        else:
            # To use
            # folder = fd.askdirectory()
            try:
                file_name = url.split("/")[-1]

                response = requests.get(url)
                response.raise_for_status()

                with open(os.path.join(self.path, file_name), "wb") as f:
                    f.write(response.content)
                mb.showinfo("Exit", f"File downloaded in: {os.path.join(os.getcwd(), file_name)}")
            except Exception as e:
                mb.showerror("Error", f"Couldn't download: {e}")