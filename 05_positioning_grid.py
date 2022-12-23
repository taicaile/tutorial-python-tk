# Tkinter - Pack and Grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("640x480")

# TODO no idea what this purpose

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.configure("MainFrame.TFrame", background="blue")
style.configure("FrameLeft.TFrame", background="yellow")
style.configure("FrameRight.TFrame", background="orange")
style.configure("FrameTop.TFrame", background="red")
style.configure("FrameBottom.TFrame", background="purple")

frame_main = ttk.Frame(root, style="MainFrame.TFrame")
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

frame_left = ttk.Frame(frame_main, style="FrameLeft.TFrame", width=50)
frame_right = ttk.Frame(frame_main, style="FrameRight.TFrame", width=50)
frame_top = ttk.Frame(frame_main, style="FrameTop.TFrame", height=50)
frame_bottom = ttk.Frame(frame_main, style="FrameBottom.TFrame", height=50)

lbl_hello = ttk.Label(frame_main, text="Hello")

print(frame_main.winfo_class())
frame_main.grid(row=0, column=0, sticky="ewns", padx=5, pady=5)

# frame_left.pack(side=tk.LEFT, fill=tk.Y)
frame_left.grid(row=0, column=0, sticky="wns")
# frame_right.pack(side=tk.RIGHT, fill=tk.Y)
frame_right.grid(row=0, column=2, sticky="ens")
# frame_top.pack(side=tk.TOP, fill=tk.X)
frame_top.grid(row=0, column=1, sticky="ewn")
# frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)
frame_bottom.grid(row=0, column=1, sticky="ews")
# lbl_hello.pack(expand=True)
lbl_hello.grid(row=0, column=1)
root.mainloop()
