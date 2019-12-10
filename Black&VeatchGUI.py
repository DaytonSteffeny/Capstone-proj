import tkinter as tk
from tkinter import *
import os
from PIL import Image

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'

def Login():
  global root
  global entryUser
  global entryPass


  HEIGHT = 600
  WIDTH = 800

  root = tk.Tk() #makes a new window
  canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#8c8c8c")
  canvas.pack()

  frame = tk.Frame(root, bg="#8c8c8c")
  frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


  buttonDeploy = tk.Button(root, text="Deploy", bg="#8c8c8c", command=CheckLogin)
  buttonDeploy.place(relx=.9, rely=.05, relwidth=.08, relheight=.034)

  label = tk.Label(frame, text="Black & Veatch Automation", font=('Arial Black', 20), bg="#8c8c8c")
  label.place(relx=-0.2, rely=-.03, relwidth=1.5, relheight=.1)

  labelIP = tk.Label(frame, text="IP Address:")
  labelIP.place(relx=0, rely=.2, relwidth=.14, relheight=.04)
  entryIP = tk.Entry(frame, bg="white")
  entryIP.place(relx=0.15, rely=.2, relwidth=.2, relheight=.04)

  labelUser = tk.Label(frame, text="Username:")
  labelUser.place(relx=.6, rely=.2, relwidth=.14, relheight=.04)
  entryUser = tk.Entry(frame, bg="white")
  entryUser.place(relx=0.76, rely=.2, relwidth=.2, relheight=.04)

  labelPass = tk.Label(frame, text="Password:")
  labelPass.place(relx=.6, rely=.3, relwidth=.14, relheight=.04)
  entryPass = tk.Entry(frame, bg="white", show="*")
  entryPass.place(relx=0.76, rely=.3, relwidth=.2, relheight=.04)

  labelDevice = tk.Label(frame, text="Pick Device:")
  labelDevice.place(relx=0, rely=.6, relwidth=.14, relheight=.04)
  var = StringVar(root)
  var.set("Firewall")
  optDevice = OptionMenu(root, var, "Firewall", "Router", "Switch")
  optDevice.place(relx=0.22, rely=.579, relwidth=.13, relheight=.035)


  labelModel = tk.Label(frame, text="Model:")
  labelModel.place(relx=.6, rely=.6, relwidth=.14, relheight=.04)
  var = StringVar(root)
  var.set("Cisco 1841")
  optModel = OptionMenu(root, var, "Cisco 1841", "Model2", "Model3")
  optModel.place(relx=0.70, rely=.579, relwidth=.20, relheight=.035)


  root.mainloop()


def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if entryUser.get() == uname and entryPass.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title('Success')
        r.geometry('400x200') # Makes the window a certain size
        rlbl = Label(r, text='\nPinging 10.180.128.171 with 32 bytes of data: \n yes') # "logged in" label
       
        rlbl.pack() # Pack is like .grid(), just different]

        r.mainloop()
        
    else:
        r = Tk()
        r.title('Failed')
        r.geometry('150x50')
        rlbl = Label(r, text='\nInvalid Credentials')
        rlbl.pack()
        r.mainloop()


if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
