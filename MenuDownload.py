import os
import requests
import tkinter as tk
from tkinter import messagebox as mb

class MenuDownload:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title("Download manager")

        self.root.configure(background="white", pady=40)
        self.root.geometry("600x500")

        self.path = path

        self.label = tk.Label(self.root, text="Insert URL to download", font=("Arial", 28, "bold"), background="white")
        self.label.pack(padx=20, pady=20)

        self.entry = tk.Entry(self.root, width=50, relief="solid")
        self.entry.pack(pady=30)

        self.button_download = tk.Button(self.root, text="Download", font=("Arial", 16), width=18, bg="white",relief="solid")
        self.button_download.bind("<Button-1>", self.download)
        self.button_download.pack(pady=5)

        self.button_exit = tk.Button(self.root, text="Return", font=("Arial", 16), width=18, bg="white",relief="solid", command=self.root.destroy)
        self.button_exit.pack(pady=5)

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