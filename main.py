from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=250, height=200)
window.config(padx=20, pady=20)
window.resizable(0,0)

def click(item):
   entry.insert(INSERT, item)

def button_disabled():
   buttonSum.configure(state=DISABLED)
   buttonTP.configure(state=DISABLED)
   buttonSub.configure(state=DISABLED)
   buttonXy.configure(state=DISABLED)
   buttonMult.configure(state=DISABLED)
   buttonPr.configure(state=DISABLED)
   buttonDiv.configure(state=DISABLED)

def button_enable():
   buttonSum.configure(state=NORMAL)
   buttonTP.configure(state=NORMAL)
   buttonSub.configure(state=NORMAL)
   buttonXy.configure(state=NORMAL)
   buttonMult.configure(state=NORMAL)
   buttonPr.configure(state=NORMAL)
   buttonDiv.configure(state=NORMAL)

def click2(item2):
   entry.insert(INSERT, item2)
   button_disabled()

def clear():
   entry.delete(0, END)
   button_enable()

def get():
   button_enable()
   a = entry.get()
   entry.delete(0, END)
   try:
      for x in a:
         if x in "+":
            a = a.split("+")
            a = list(a)
            b = (float(a[0]) + float(a[1]))
            entry.insert(0, round(b,3))
         elif x in "-":
            a = a.split("-")
            a = list(a)
            b = (float(a[0]) - float(a[1]))
            entry.insert(0, round(b,3))
         elif x in "*":
            a = a.split("*")
            a = list(a)
            b = (float(a[0]) * float(a[1]))
            entry.insert(0, round(b,3))
         elif x in "/":
            a = a.split("/")
            a = list(a)
            b = (float(a[0]) / float(a[1]))
            entry.insert(0, round(b,3))
         elif x in "√¯":
            a = a.replace("√¯","")
            a = float(a)
            b = a ** 0.5
            entry.insert(0, round(b,3))
         elif x in "xʸ":
            a = a.split("xʸ")
            a = list(a)
            b = (float(a[0]) ** float(a[1]))
            entry.insert(0, round(b, 3))
         elif x in "%":
            a = a.split("%")
            a = list(a)
            b = (float(a[0]) * (float(a[1])/100))
            entry.insert(0, round(b, 3))
      if a != a.find("+") or "":
         entry.delete(0, END)
         entry.insert(0, "Please trade using only two numbers!")
   except:
      print("")

def enter(event):
   get()



entry = Entry(width=35, justify=RIGHT)
entry.focus_set()
entry.pack()

button1 = Button(text="1" , font=("Ariel", 10, "bold"), command=lambda: click(1))
button1.place(x=20, y=30, width=30, height=30)

button2 = Button(text="2" , font=("Ariel", 10, "bold"), command=lambda: click(2))
button2.place(x=50, y=30, width=30, height=30)

button3 = Button(text="3" , font=("Ariel", 10, "bold"), command=lambda: click(3))
button3.place(x=80, y=30, width=30, height=30)

button4 = Button(text="4" , font=("Ariel", 10, "bold"), command=lambda: click(4))
button4.place(x=20, y=60, width=30, height=30)

button5 = Button(text="5" , font=("Ariel", 10, "bold"), command=lambda: click(5))
button5.place(x=50, y=60, width=30, height=30)

button6 = Button(text="6" , font=("Ariel", 10, "bold"), command=lambda: click(6))
button6.place(x=80, y=60, width=30, height=30)

button7 = Button(text="7" , font=("Ariel", 10, "bold"), command=lambda: click(7))
button7.place(x=20, y=90, width=30, height=30)

button8 = Button(text="8" , font=("Ariel", 10, "bold"), command=lambda: click(8))
button8.place(x=50, y=90, width=30, height=30)

button9 = Button(text="9" , font=("Ariel", 10, "bold"), command=lambda: click(9))
button9.place(x=80, y=90, width=30, height=30)

button0 = Button(text="0" , font=("Ariel", 10, "bold"), command=lambda: click(0))
button0.place(x=20, y=120, width=30, height=30)

buttonDot = Button(text="." , font=("Ariel", 10, "bold"), command=lambda: click("."))
buttonDot.place(x=50, y=120, width=30, height=30)

buttonEqual = Button(text="=" , font=("Ariel", 10, "bold"), command=get)
buttonEqual.place(x=80, y=120, width=30, height=30)

buttonAc = Button(text="AC" , font=("Ariel", 10, "bold"), command=clear, fg="red")
buttonAc.place(x=120, y=30, width=30, height=30)

buttonSum = Button(text="+" , font=("Ariel", 10, "bold"), command=lambda: click2("+"))
buttonSum.place(x=150, y=30, width=30, height=30)

buttonTP = Button(text="√¯" , font=("Ariel", 10, "bold"), command=lambda: click2("√¯"))
buttonTP.place(x=120, y=60, width=30, height=30)

buttonSub = Button(text="-" , font=("Ariel", 10, "bold"), command=lambda: click2("-"))
buttonSub.place(x=150, y=60, width=30, height=30)

buttonXy = Button(text="xʸ" , font=("Ariel", 10, "bold"), command=lambda: click2("xʸ"))
buttonXy.place(x=120, y=90, width=30, height=30)

buttonMult = Button(text="*" , font=("Ariel", 10, "bold"), command=lambda: click2("*"))
buttonMult.place(x=150, y=90, width=30, height=30)

buttonPr = Button(text="%" , font=("Ariel", 10, "bold"), command=lambda: click2("%"))
buttonPr.place(x=120, y=120, width=30, height=30)

buttonDiv = Button(text="/" , font=("Ariel", 10, "bold"), command=lambda: click2("/"))
buttonDiv.place(x=150, y=120, width=30, height=30)

window.bind("<Return>", enter)
window.mainloop()

