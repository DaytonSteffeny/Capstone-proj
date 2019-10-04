from tkinter import *

root = Tk()

N1 = ["Routers"]
N2 = ["Switches"]
N3 = ["Firewalls"]

ipEnter = Entry(root, width=50)
ipEnter.pack()

myLabel1 = Label(root, text="Black & Veatch Automation").grid(row=0, column=0)
myLabel2 = Label(root, text="Pick A Device: ").grid(row=1, column=1)
myLabel3 = Label(root, text="Pick A Model: ").grid(row=1, column=1)
myLabel4 = Label(root, text="Enter IP Address: ").grid(row=2)
root.geometry("1000x800")
root.title("Black & Veatch Automation")



var=tkinter.StringVar()

set1 = tkinter.OptionMenu(root,var,N1,N2,N3)
set1.configure(font=("Arial",15))
set1.grid(row=20)
set1.pack()



root.mainloop()
