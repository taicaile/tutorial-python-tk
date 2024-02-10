# refactor code using classes

import tkinter as tk

func_active_page = None


class MainWindow(tk.Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.title = title
        self.geometry(f"{width}x{height}")
        # Option Frame
        self.options_frame = OptionsPage(self, bg="#c3c3c3")
        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(height=400, width=100)
        # Page Frame
        self.page_frame = PageFrame(self)
        self.page_frame.pack(side=tk.LEFT)
        self.page_frame.pack_propagate(False)
        self.page_frame.configure(height=400, width=400)


class PageFrame(tk.Frame):
    def __init__(self, master=None, text=None):
        super().__init__(
            master=master, highlightbackground="grey", highlightthickness=2
        )
        self.active_frame = None
        global func_active_page
        func_active_page = self.set_active_page

    def set_active_page(self, text):
        if self.active_frame is not None:
            self.active_frame.destroy()
        self.active_frame = tk.Frame(self)
        label = tk.Label(self.active_frame, text=text + "  Page", font=("bold", 30))
        label.pack()
        self.active_frame.pack(pady=20)


class OptionsPage(tk.Frame):
    def __init__(self, master=None, bg=None):
        super().__init__(master=master, bg=bg)
        self.indicators = {}
        # Home Button
        HomeName = "Home"
        self.homebtn = OptionButton(
            self, HomeName, command=lambda: self.switch_page(HomeName)
        )
        self.homebtn.place(x=10, y=50, width=80)
        self.homebtnindicator = OptionButtonIndicator()
        self.homebtnindicator.place(x=3, y=50, width=5, height=25)
        self.indicators[HomeName] = self.homebtnindicator

        # Menu Button
        MenuName = "Menu"
        self.menubtn = OptionButton(
            self, MenuName, command=lambda: self.switch_page(MenuName)
        )
        self.menubtn.place(x=10, y=100, width=80)
        self.menubtnindicator = OptionButtonIndicator()
        self.menubtnindicator.place(x=3, y=100, width=5, height=25)
        self.indicators[MenuName] = self.menubtnindicator

        # Contact Button
        ContactName = "Contact"
        self.contactbtn = OptionButton(
            self, ContactName, command=lambda: self.switch_page(ContactName)
        )
        self.contactbtn.place(x=10, y=150, width=80)
        self.contactbtnindicator = OptionButtonIndicator()
        self.contactbtnindicator.place(x=3, y=150, width=5, height=25)
        self.indicators[ContactName] = self.contactbtnindicator

        # About Button
        AboutName = "Name"
        self.aboutbtn = OptionButton(
            self, AboutName, command=lambda: self.switch_page(AboutName)
        )
        self.aboutbtn.place(x=10, y=200, width=80)
        self.aboutbtnindicator = OptionButtonIndicator()
        self.aboutbtnindicator.place(x=3, y=200, width=5, height=25)
        self.indicators[AboutName] = self.aboutbtnindicator

    def set_active_indicator(self, name):
        for key in self.indicators:
            self.indicators[key].configure(bg="#c3c3c3")
        self.indicators[name].configure(bg="#158aff")

    def switch_page(self, name):
        # clicked_btn_text = btn.cget("text")
        self.set_active_indicator(name)
        if callable(func_active_page):
            func_active_page(name)


class OptionButton(tk.Button):
    def __init__(self, master=None, text="", command=None):
        super().__init__(
            master=master,
            text=text,
            font=("bold", 15),
            fg="#158aff",
            bd=0,
            bg="#c3c3c3",
            command=command,
        )


class OptionButtonIndicator(tk.Label):
    def __init__(self, master=None, text=""):
        super().__init__(
            master=master,
            text=text,
            bg="#c3c3c3",
        )


mainwindow = MainWindow(width=500, height=400, title="Switch Pages")


mainwindow.mainloop()
