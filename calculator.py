from tkinter import *
import math



root=Tk()
root.title("Calculator")


input1=Entry(root,width=40,borderwidth=5 , justify="right",bg="grey11",fg="white")
input1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
	string= input1.get()
	input1.delete(0,END)
	input1.insert(0,str(string)+str(number))
def button_plus():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="qo'shish"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)	
def button_mutply():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="ko'paytirish"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)
def button_deservion():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="bo'lish"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)	
def button_clear():
	input1.delete(0,END)
def button_minus():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="ayirish"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)
def button_procent():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="foiz"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)	
def button_degree():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="daraja"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)
def button_sqrt():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal="ildiz"
	saqlangan_raqam = float(raqamni_olish)
	input1.delete(0,END)
	y=math.sqrt(saqlangan_raqam)
	input1.insert(0,y)

def button_equal():
	summa = input1.get()
	input1.delete(0,END)
	if amal=="qo'shish":
		y=saqlangan_raqam + float(summa)
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))	
	if amal=="ayirish":
		y=saqlangan_raqam - float(summa)
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))
	if amal=="daraja":
		y=saqlangan_raqam ** float(summa)
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))
	if amal=="foiz":
		y=(saqlangan_raqam * float(summa))/100
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))					
	if amal=="ko'paytirish":
		y = saqlangan_raqam*float(summa)
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))
	if amal=="bo'lish":
		y = saqlangan_raqam / float(summa)
		if y%1==0:
			input1.insert(0,int(y))
		else:
			input1.insert(0,float(y))
		
	



button_1=Button(root, text="1", padx=40, pady=15,bg="orange",command=lambda: button_click(1))
button_2=Button(root, text="2", padx=48, pady=15,bg="orange",command=lambda: button_click(2))
button_3=Button(root, text="3", padx=42, pady=15,bg="orange",command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=15,bg="orange",command=lambda: button_click(4))
button_5=Button(root, text="5", padx=48, pady=15,bg="orange",command=lambda: button_click(5))
button_6=Button(root, text="6", padx=42, pady=15,bg="orange",command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=15,bg="orange",command=lambda: button_click(7))
button_8=Button(root, text="8", padx=48, pady=15,bg="orange",command=lambda: button_click(8))
button_9=Button(root, text="9", padx=42, pady=15,bg="orange",command=lambda: button_click(9))
button_0=Button(root, text="0", padx=48, pady=15,bg="orange",command=lambda: button_click(0))
button_equal=Button(root, text="=", padx=44, pady=15,bg="black",fg="white",command=button_equal)
button_plus=Button(root, text="+", padx=44, pady=15,fg="white",bg="red",command=button_plus)
button_minus=Button(root, text="-", padx=44, pady=15,fg="white",bg="red",command=button_minus)
button_mutply=Button(root, text="x", padx=44, pady=15,fg="white",bg="red",command=button_mutply)
button_deservion=Button(root, text="/", padx=44, pady=15,fg="white",bg="red",command=button_deservion)
button_clear=Button(root, text="C", padx=40, pady=15,fg="white",bg="red",command=button_clear)
button_degree=Button(root, text="x^y", padx=40, pady=15,fg="white",bg="red",command=button_degree)
button_procent=Button(root, text="%", padx=40, pady=15,fg="white",bg="red",command=button_procent)
button_sqrt=Button(root, text="√", padx=40, pady=15,fg="white",bg="red",command=button_sqrt)
button_dot=Button(root, text= '.' , padx=42, pady=15,fg="white",bg="red",command=lambda: button_click('.'))

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_plus.grid(row=6, column=3)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_minus.grid(row=5, column=3)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_clear.grid(row=3, column=0)
button_0.grid(row=7, column=1)
button_equal.grid(row=7, column=3)
button_deservion.grid(row=3, column=3)
button_degree.grid(row=3, column=1)
button_procent.grid(row=3, column=2)
button_sqrt.grid(row=7, column=0)
button_mutply.grid(row=4, column=3)
button_dot.grid(row=7, column=2)




root.mainloop()