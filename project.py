from tkinter import *
from random import *

w1=Tk()
w1.geometry("600x600")

def change():
    adj=choice(["Good","Bad","Awesome","Dark","Handsome","Big","Red","Huge"])
    num=randrange(1,101)
    name=e1_value.get()
    password=adj+name+str(num)
    e2.delete(0,END)
    e2.insert(END,password)
    return password

def go():
    if e3_value.get()==e2_value.get() and e1_value.get()!="" and e3_value.get()!="":
        m1=Label(w1,text="YOU HAVE GENERATED A PASSWORD", bg="green")
        m1.place(x=20,y=470,width=500,height=50)
    else:
        m1=Label(w1,text="THIS PASSWORD IS ALREADY TAKEN", bg="red")
        m1.place(x=20,y=470,width=500,height=50)

l1=Label(w1,text="ENTER A PASSWORD:", font=('arial',15) )
l1.place(x=20,y=50,width=300,height=40)

e1_value=StringVar()
e1=Entry(w1,textvariable=e1_value)
e1.place(x=300,y=50,width=150,height=40)
e1.focus()


b1.place(x=180,y=160,width=190,height=40)

e2_value=StringVar()
e2=Entry(w1,textvariable=e2_value)
e2.place(x=180,y=230,width=190,height=40)

l2=Label(w1,text="ENTER CONFIRM PASSWORD:", font=('arial',10))
l2.place(x=20,y=330,width=300,height=40)

e3_value=StringVar()
e3=Entry(w1,textvariable=e3_value)
e3.place(x=270,y=330,width=190,height=40)

b1=Button(w1,text="CREATE",command=go, font=('arial',15))
b1.place(x=180,y=410,width=190,height=40)

w1.configure(bg='#333333')
w1.mainloop()
x='Athrva'
