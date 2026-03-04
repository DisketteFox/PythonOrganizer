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
        self.icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "icon.png"))
        self.root.iconphoto(False, self.icon)

        self.path = path

        self.label = tk.Label(self.root, text="Manage your backups", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)

        self.button_backup = tk.Button(self.root, text="Create backup", font=("Arial", 12), width=12)
        self.button_backup.bind("<Button-1>", self.backup)
        self.button_backup.pack()

        self.button_restore = tk.Button(self.root, text="Restore backup", font=("Arial", 12), width=12)
        self.button_restore.bind("<Button-1>", self.restore)
        self.button_restore.pack()

        self.button_exit = tk.Button(self.root, text="Return", font=("Arial", 12), width=12, command=self.root.destroy)
        self.button_exit.pack()

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