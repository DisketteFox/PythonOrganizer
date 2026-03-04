import os
import requests
import tkinter as tk
from tkinter import messagebox as mb

class MenuDownload:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title("Download manager")
        self.icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "icon.png"))
        self.root.iconphoto(False, self.icon)

        self.path = path

        self.label = tk.Label(self.root, text="Insert the URL of the file", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)

        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=10)

        self.button_download = tk.Button(self.root, text="Download", font=("Arial", 12))
        self.button_download.bind("<Button-1>", self.download)
        self.button_download.pack()

        self.button_exit = tk.Button(self.root, text="Return", font=("Arial", 12), command=self.root.destroy)
        self.button_exit.pack()

        self.root.mainloop()

    def download(self, event):
        url = self.entry.get()

        if url == "":
            mb.showerror("Error", "URL is empty")
        else:
            try:
                file_name = url.split("/")[-1]
                dst = os.path.join(self.path, file_name)

                response = requests.get(url)
                response.raise_for_status()

                with open(dst, "wb") as f:
                    f.write(response.content)
                mb.showinfo("Successful", f"File downloaded in {dst}")
            except Exception as e:
                mb.showerror("Error", f"Couldn't download ({e})")