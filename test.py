from datetime import datetime
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x640")

style = ttk.Style()
style.configure("MainFrame.TFrame", background="blue")
style.configure("FrameLeft.TFrame", background="yellow")
style.configure("FrameRight.TFrame", background="orange")
style.configure("FrameTop.TFrame", background="red")
style.configure("FrameBottom.TFrame", background="purple")

main_frame = ttk.Frame(root, style="MainLeft.TFrame")
main_frame.pack(expand=True, fill=tk.BOTH)

left_frame = ttk.Frame(master=main_frame, width=50, style="FrameLeft.TFrame")
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = ttk.Frame(master=main_frame, width=50, style="FrameRight.TFrame")
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

top_frame = ttk.Frame(master=main_frame, height=50, style="FrameTop.TFrame")
top_frame.pack(side=tk.TOP, fill=tk.X)

# ttk.Frame(master=main_frame, height=10, style="FrameRight.TFrame").pack(side=tk.BOTTOM, fill=tk.X)

bottom_frame = ttk.Frame(master=main_frame, height=50, style="FrameBottom.TFrame", relief="sunken")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# lbl_label = ttk.Label(master=bottom_frame, text="This is a label.")
# lbl_label.grid(row=0, column=0)

logoutput = tk.Text(bottom_frame, height = 5,
              width = 25,
              bg = "light cyan")
logoutput.pack(expand=True, fill=tk.BOTH)

for i in range(100):
    logoutput.insert(tk.END, str(datetime.now()) + f": init {i}\n")
root.mainloop()
