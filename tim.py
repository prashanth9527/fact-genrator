from tkinter import *
import  randfacts
top = Tk()
top.config(bg = "#66ee99")
# Code to add widgets will go here...
top.title("Random facts generator")
top.geometry("600x500")

frm1 = Frame(top,height = 20,bg = "#66ee99")
frm1.pack()

frm2 = Frame(top,height = 30,bg = "#66ee99")
frm2.pack()

frm3 = Frame(top,height = 20,bg = "#66ee99")
frm3.pack()

frm4 = Frame(top,height = 10,bg = "#66ee99")
frm4.pack()

frm5 = Frame(top,height = 20,bg = "#66ee99")
frm5.pack()

frm6 = Frame(top,height = 20,bg = "#66ee99")
frm6.pack()

frm7 = Frame(top,height = 20,bg = "#66ee99")
frm7.pack()

frm8 = Frame(top,height = 50,bg = "#66ee99")
frm8.pack()

frm9 = Frame(top,height = 20,bg = "#66ee99")
frm9.pack()

frm10 = Frame(top,height = 40,bg = "#66ee99")
frm10.pack()

frm11 = Frame(top,height = 20,bg = "#66ee99")
frm11.pack()

frm12 = Frame(top,height = 30,bg = "#66ee99")
frm12.pack()

frm13 = Frame(top,height = 20,bg = "#66ee99")
frm13.pack()

frm14 = Frame(top,height = 30,bg = "#66ee99")
frm14.pack()

frm15 = Frame(top,height = 20,bg = "#66ee99")
frm15.pack()

def f():
	fact = randfacts.get_fact(True)
	t = "*)"
	global fac
	fac = Label(frm8,text = t+fact,bg = "#66ee99",fg = "#6e0460",font = ("Macondo",10,"bold"))
	fac.pack()
	q["state"] = "active"

def r():
	top.destroy()


tit = Label(frm1,text = "Facts Generator",font = ("Helvetica",25,"bold"),fg = "#7e1975",bg = "#66ee99",borderwidth = '4',relief = "flat")
tit.pack()

fa = Button(frm3,text = "Generate fact",command = f,fg = "#cab363",bg = "#985adf",borderwidth = '10',font = ("Helvetica",15,"bold"))
fa.pack()

q = Button(frm5,text = "QUIT",command = r,fg = "#ff35ed",bg = "#1d93ed",borderwidth = '10',font = ("Helvetica",15),state = "disable")
q.pack(side = "left")

top.mainloop()