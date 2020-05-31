from tkinter import*

def bntClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def cleardisplay():
    global operator
    operator = ""
    text_Input.set('')

def Equal():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    operator= operator + sumup

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

textDisplay = Entry(cal,font=('arial',20,'bold'),textvariable = text_Input,bd=30, insertwidth=5,bg="powder blue",justify='left').grid(columnspan=5)

############################################
btn7 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:bntClick(7),bg="powder blue").grid(row=1,column=0)

btn8 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:bntClick(8),bg="powder blue").grid(row=1,column=1)

btn9 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:bntClick(9),bg="powder blue").grid(row=1,column=2)

btnplus = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:bntClick('+'),bg="powder blue").grid(row=1,column=3)
################################################
btn4 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:bntClick(4),bg="powder blue").grid(row=2,column=0)

btn5 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:bntClick(5),bg="powder blue").grid(row=2,column=1)

btn6 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:bntClick(6),bg="powder blue").grid(row=2,column=2)

btnsub = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:bntClick('-'),bg="powder blue").grid(row=2,column=3)
##############################################
btn1 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:bntClick(1),bg="powder blue").grid(row=3,column=0)

btn2 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:bntClick(2),bg="powder blue").grid(row=3,column=1)

btn3 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:bntClick(3),bg="powder blue").grid(row=3,column=2)

btnmul = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:bntClick('*'),bg="powder blue").grid(row=3,column=3)
##############################################
btn0 = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:bntClick(0),bg="powder blue").grid(row=4,column=0)

btnC = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=cleardisplay,bg="powder blue").grid(row=4,column=1)

btniq = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=Equal,bg="powder blue").grid(row=4,column=2)

btndiv = Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:bntClick('/'),bg="powder blue").grid(row=4,column=3)
##############################################



cal.mainloop()

