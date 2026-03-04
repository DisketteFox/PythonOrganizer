import os
import requests
import shutil
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class MenuBackups:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title("Download manager")

        self.root.configure(background="white", pady=40)
        self.root.geometry("600x500")

        self.path = path

        self.label = tk.Label(self.root, text="Manage your backups", font=("Arial", 28, "bold"), background="white")
        self.label.pack(padx=20, pady=10)

        self.button_backup = tk.Button(self.root, text="Create backup ⮺", font=("Arial", 16), width=18, bg="white", relief="solid")
        self.button_backup.bind("<Button-1>", self.backup)
        self.button_backup.pack(pady=5)

        self.button_restore = tk.Button(self.root, text="Restore backup ⮺", font=("Arial", 16), width=18, bg="white", relief="solid")
        self.button_restore.bind("<Button-1>", self.restore)
        self.button_restore.pack(pady=5)

        self.button_exit = tk.Button(self.root, text="Return", font=("Arial", 16), width=18, bg="white", relief="solid", command=self.root.destroy)
        self.button_exit.pack(pady=5)

        self.root.mainloop()

    def backup(self, event):
        files = fd.askopenfilenames(parent=self.root, initialdir=self.path)

        for file in files:
            file_name = file.split("/")[-1]
            print(file_name)
            shutil.copy(file, file + ".bak")

    def restore(self, event):
        files = fd.askopenfilenames(parent=self.root, initialdir=self.path, filetypes=[("Backup Files", "*.bak")])

        for file in files:
            file_name = file.split("/")[-1]
            original_file = file.rstrip(".bak")
            print(file_name)
            shutil.copy(file, original_file)