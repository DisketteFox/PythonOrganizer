from MenuOrganize import *
from MenuDownload import *
from MenuBackups import *

import tkinter as tk
from tkinter import filedialog as fd

class MenuMain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Download manager")
        self.icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "icon.png"))
        self.root.iconphoto(False, self.icon)

        self.path = fd.askdirectory(parent=self.root)

        self.label = tk.Label(self.root, text="Download manager", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)

        self.button_downloads = tk.Button(self.root, text="Download files", font=("Arial", 12), width=14, command=lambda: MenuDownload(self.path))
        self.button_downloads.pack(padx=10, pady=2)

        self.button_organizer = tk.Button(self.root, text="Organize files", font=("Arial", 12), width=14, command=lambda: MenuOrganize(self.path))
        self.button_organizer.pack(padx=10, pady=2)

        self.button_backups = tk.Button(self.root, text="Manage backups", font=("Arial", 12), width=14,command=lambda: MenuBackups(self.path))
        self.button_backups.pack(padx=10, pady=2)

        self.button_exit = tk.Button(self.root, text="Exit", font=("Arial", 12), width=14, command=self.root.destroy)
        self.button_exit.pack(padx=10, pady=2)

        self.root.mainloop()