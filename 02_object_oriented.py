import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    """ """

    def __init__(self):
        super().__init__()
        self.username = "CoolUsername"
        frame_main = ttk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)
        btn_show_username = ttk.Button(
            frame_main, text="show username", command=self.show_username_window
        )
        btn_show_username.pack(padx=10, pady=10)

    def show_username_window(self):
        username_window = UsernameWindow(self, self.username)


class UsernameWindow(tk.Toplevel):
    def __init__(self, master, username):
        super().__init__(master)
        self.username = username
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)
        lbl_username = ttk.Label(
            self.frame_main, text=f"My username is {self.username}"
        )
        lbl_username.pack(padx=50, pady=50)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
