import Tkinter as tk
from Tkinter import *
import ttk


HEIGHT = 600
WIDTH = 800


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#8c8c8c")
canvas.pack()

frame = tk.Frame(root, bg="#8c8c8c")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


button = tk.Button(root, text="Deploy", bg="#8c8c8c")
button.place(relx=.9, rely=.05, relwidth=.08, relheight=.034)

label = tk.Label(frame, text="Black & Veatch Network Automation", font=('Arial Black', 25), bg="#8c8c8c")
label.place(relx=-0.2, rely=-.03, relwidth=1.5, relheight=.1)

label = tk.Label(frame, text="IP Address:")
label.place(relx=0, rely=.2, relwidth=.14, relheight=.04)
entry = tk.Entry(frame, bg="white")
entry.place(relx=0.15, rely=.2, relwidth=.2, relheight=.04)

label = tk.Label(frame, text="Username:")
label.place(relx=.6, rely=.2, relwidth=.14, relheight=.04)
entry = tk.Entry(frame, bg="white")
entry.place(relx=0.76, rely=.2, relwidth=.2, relheight=.04)

label = tk.Label(frame, text="Password:")
label.place(relx=.6, rely=.3, relwidth=.14, relheight=.04)
entry = tk.Entry(frame, bg="white")
entry.place(relx=0.76, rely=.3, relwidth=.2, relheight=.04)


label = tk.Label(frame, text="Pick Device:")
label.place(relx=0, rely=.6, relwidth=.14, relheight=.04)
var = StringVar(root)
var.set("Firewall")
opt = OptionMenu(root, var, "Firewall", "Router", "Switch")
opt.place(relx=0.22, rely=.579, relwidth=.13, relheight=.035)


label = tk.Label(frame, text="Model:")
label.place(relx=.6, rely=.6, relwidth=.14, relheight=.04)
var = StringVar(root)
var.set("Cisco 1841")
opt = OptionMenu(root, var, "Cisco 1841", "Model2", "Model3")
opt.place(relx=0.70, rely=.579, relwidth=.20, relheight=.035)


root.mainloop()