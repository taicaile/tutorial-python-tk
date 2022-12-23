# Tkinter - Pack and Grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("640x480")

style = ttk.Style()
style.configure("MainFrame.TFrame", background="blue")
style.configure("FrameLeft.TFrame", background="yellow")
style.configure("FrameRight.TFrame", background="orange")
style.configure("FrameTop.TFrame", background="red")
style.configure("FrameBottom.TFrame", background="purple")


frame_main = ttk.Frame(root, style="MainFrame.TFrame")
frame_left = ttk.Frame(frame_main, style="FrameLeft.TFrame", width=50)
frame_right = ttk.Frame(frame_main, style="FrameRight.TFrame", width=50)
frame_top = ttk.Frame(frame_main, style="FrameTop.TFrame", height=50)
frame_bottom = ttk.Frame(frame_main, style="FrameBottom.TFrame", height=50)

lbl_hello = ttk.Label(frame_main, text="Hello")

print(frame_main.winfo_class())
frame_main.pack(expand=True, fill=tk.BOTH)
frame_left.pack(side=tk.LEFT, fill=tk.Y)
frame_right.pack(side=tk.RIGHT, fill=tk.Y)
frame_top.pack(side=tk.TOP, fill=tk.X)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

lbl_hello.pack(expand=True)

root.mainloop()
