import os
from tkinter import*
root=Tk()
root.geometry('900x200')
root.title("Graphing Calculator")
l=Label(root, text="Choose one of the given options!", font=("Arial Bold", 25))
l.grid(row=0,column=0)
def ODE_NIC():
    os.system('ODE.py')
def ODE1_NIC():
    os.system('ODE1.py')  

b1=Button(root,text="Pendulum Differential Equation",bg="yellow", fg="blue",font=("Arial Bold", 15),command=ODE_NIC)
b1.grid(row=2,column=0)
b2=Button(root,text="Any ODE",bg="cyan", fg="blue",font=("Arial Bold", 15),command=ODE1_NIC)
b2.grid(row=2,column=1)
