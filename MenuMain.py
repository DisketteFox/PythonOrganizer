from MenuOrganize import *
from MenuDownload import *
from MenuBackups import *

import tkinter as tk
from tkinter import filedialog as fd

class MenuMain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Download manager")
        self.icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        print(self.root.title)
        print(os.path.join(os.path.dirname(__file__), "icon.png"))
        self.icon = tk.PhotoImage(file=self.icon_path)
        self.root.iconphoto(False, self.icon)

        self.root.configure(background="white", pady=40)
        self.root.geometry("600x500")

        # self.path = fd.askdirectory(parent=self.root)
        self.path = "/home/miles/Documents/example"

        self.image_label = tk.Label(self.root, image=self.icon, background="white")
        self.image_label.pack()

        self.label = tk.Label(self.root, text="Download manager", font=("Arial", 28, "bold"), background="white")
        self.label.pack(padx=20, pady=30)

        self.button_downloads = tk.Button(self.root, text="Download files", font=("Arial", 16), width=18, bg="white", relief="solid", command=lambda: MenuDownload(self.path))
        self.button_downloads.pack(padx=10, pady=2)

        self.button_organizer = tk.Button(self.root, text="Organize files", font=("Arial", 16), width=18, bg="white", relief="solid", command=lambda: MenuOrganize(self.path))
        self.button_organizer.pack(padx=10, pady=2)

        self.button_backups = tk.Button(self.root, text="Manage backups", font=("Arial", 16), width=18, bg="white", relief="solid",command=lambda: MenuBackups(self.path))
        self.button_backups.pack(padx=10, pady=2)

        self.button_exit = tk.Button(self.root, text="Exit", font=("Arial", 16), width=18, bg="white", relief="solid", command=self.root.destroy)
        self.button_exit.pack(padx=10, pady=2)

        self.root.mainloop()