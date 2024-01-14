import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Tkinter Hub")


options_frame = tk.Frame(root, bg="#c3c3c3")
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)


def home_page():
    home_frame = tk.Frame(page_frame)
    label = tk.Label(home_frame, text="Home Page\n\n page 1", font=("bold", 30))
    label.pack()
    home_frame.pack(pady=20)



def menu_page():
    home_frame = tk.Frame(page_frame)
    label = tk.Label(home_frame, text="Menu Page\n\n page 2", font=("bold", 30))
    label.pack()
    home_frame.pack(pady=20)

def contact_page():
    home_frame = tk.Frame(page_frame)
    label = tk.Label(home_frame, text="Contact Page\n\n page 3", font=("bold", 30))
    label.pack()
    home_frame.pack(pady=20)

def about_page():
    home_frame = tk.Frame(page_frame)
    label = tk.Label(home_frame, text="About Page\n\n page 4", font=("bold", 30))
    label.pack()
    home_frame.pack(pady=20)

home_btn = tk.Button(
    options_frame,
    text="Home",
    font=("bold", 15),
    fg="#158aff",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(home_indicator, home_page),
)
home_btn.place(x=10, y=50, width=80)
home_indicator = tk.Label(options_frame, text="", bg="#c3c3c3")
home_indicator.place(x=3, y=50, width=5, height=30)


menu_btn = tk.Button(
    options_frame,
    text="Menu",
    font=("bold", 15),
    fg="#158aff",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(menu_indicator, menu_page),
)
menu_btn.place(x=10, y=100, width=80)
menu_indicator = tk.Label(options_frame, text="", bg="#c3c3c3")
menu_indicator.place(x=3, y=100, width=5, height=30)


contact_btn = tk.Button(
    options_frame,
    text="Contact",
    font=("bold", 15),
    fg="#158aff",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(contact_indicator, contact_page),
)
contact_btn.place(x=10, y=150, width=80)
contact_indicator = tk.Label(options_frame, text="", bg="#c3c3c3")
contact_indicator.place(x=3, y=150, width=5, height=30)

about_btn = tk.Button(
    options_frame,
    text="About",
    font=("bold", 15),
    fg="#158aff",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(about_indicator, about_page),
)
about_btn.place(x=10, y=200, width=80)
about_indicator = tk.Label(options_frame, text="", bg="#c3c3c3")
about_indicator.place(x=3, y=200, width=5, height=30)

page_frame = tk.Frame(root, highlightbackground="grey", highlightthickness=2)
page_frame.pack(side=tk.LEFT)
page_frame.propagate(False)
page_frame.configure(height=400, width=400)


def delete_pages():
    for page in page_frame.winfo_children():
        page.destroy()


def hide_indicators():
    home_indicator.config(bg="#c3c3c3")
    menu_indicator.config(bg="#c3c3c3")
    contact_indicator.config(bg="#c3c3c3")
    about_indicator.config(bg="#c3c3c3")


def indicator(lb, page):
    hide_indicators()
    lb.configure(bg="#158aff")
    delete_pages()
    page()


root.mainloop()
