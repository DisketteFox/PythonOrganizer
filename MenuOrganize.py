import tkinter as tk

class MenuOrganize:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Administrador de descargas")

        self.label = tk.Label(self.root, text="Introduce la carpeta que quieras ver", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.input_box = tk.Entry(self.root)
        self.input_box.pack(padx=20, pady=20)

        self.root.bind("<Return>", self.show_message)

        self.root.mainloop()

    def show_message(self, event):
        print(self.input_box.get())