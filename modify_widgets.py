import tkinter as tk
from tkinter import ttk


class Response:
    def __init__(self, answer: str, update_func):
        self.answer = answer
        self.update_func = update_func

    def get_response(self):
        if self.answer == "Python":
            self.update_func("Python is really cool!")
        else:
            self.update_func("I don't know that language.")


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_frame_main().pack(fill=tk.BOTH, expand=True)

    def create_frame_main(self) -> ttk.Frame:
        self.frame_main = ttk.Frame(self)
        self.lbl_title = ttk.Label(
            self.frame_main, text="What is your favouriate programming language?"
        )

        self.entry_answer = ttk.Entry(self.frame_main)
        self.btn_submit = ttk.Button(
            self.frame_main, text="Submit", command=self.on_submit_button_clicked
        )

        self.lbl_response = ttk.Label(self.frame_main, text="Hi, I am a Label.")

        self.lbl_title.pack()
        self.entry_answer.pack()
        self.btn_submit.pack()
        self.lbl_response.pack(pady=15)

        return self.frame_main

    def on_submit_button_clicked(self):
        # Get the user's answer
        user_answer = self.entry_answer.get()
        response = Response(answer=user_answer, update_func=self.change_label_text)
        response.get_response()

    def change_label_text(self, new_text: str):
        self.lbl_response.configure(text=new_text)


if __name__ == "__main__":

    main_window = MainWindow()
    main_window.mainloop()
