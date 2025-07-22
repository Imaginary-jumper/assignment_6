from tkinter import *

window = Tk()
window.geometry("310x470")
window.title("Calculator")
window.config(bg="light grey")

entry_box = Entry(window , width=18 , borderwidth=5 , font=('Arial', 20) , relief=SUNKEN)
entry_box.place(x=14 , y=10 , height= 70)
temp=0
rem1=0
current_operator=""
def operator(name):
    def check():
        global temp
        temp = entry_box.get()
        if len(str(temp)) == 0:
            temp=0
        else:
            temp = float(entry_box.get())
    check()
    if name=="%":
        result = temp
        result = result/100
        entry_box.delete(0, END)
        entry_box.insert(0, result)
    elif name=="1/x":
        if temp==0:
            entry_box.delete(0, END)
            entry_box.insert(0, "")
        else:
            result = temp
            result = 1 / result
            result = format(result, ".5f")
            entry_box.delete(0, END)
            entry_box.insert(0, result)
    elif name=="sqr":
        result = temp
        result = result**2
        entry_box.delete(0, END)
        entry_box.insert(0, result)
    elif name=="sqrt":
        result = temp
        result = result**0.5
        result = format(result, ".5f")
        entry_box.delete(0, END)
        entry_box.insert(0, result)
    elif name=="Del":
        result = temp
        result = str(result)
        a=len(result)
        result = result[0:a-1]
        entry_box.delete(0, END)
        entry_box.insert(0, result)
    elif name=="/" or name=="*" or name=="+" or name=="-":
        global rem1
        if entry_box.get() == "":
            rem1 = 0
        else:
            rem1 = float(entry_box.get())
            entry_box.delete(0, END)
            global current_operator
            current_operator = name
    else:
        pass

button1 = Button(window , text="%" , font=('Arial', 15), borderwidth=5 , command=lambda:operator("%"), activebackground= "dark grey")
button1.place (x=20, y=100 , width=60 , height=50 )
def clear():
    entry_box.delete(0, END)
    global rem1
    rem1 = 0
button2 = Button(window , text="CE" , font=('Arial', 15), borderwidth=5,command=lambda :clear(), activebackground= "dark grey")
button2.place (x=90, y=100 , width=60 , height=50 )

button3 = Button(window , text="C" , font=('Arial', 15), borderwidth=5 ,command=lambda:entry_box.delete(0, END), activebackground= "dark grey" )
button3.place (x=160, y=100 , width=60 , height=50 )

button4 = Button(window , text="Del" , font=('Arial', 15), borderwidth=5,command=lambda:operator("Del") , activebackground= "dark grey")
button4.place (x=230, y=100 , width=60 , height=50 )

button5 = Button(window , text="1/x" , font=('Arial', 15), borderwidth=5,command=lambda:operator("1/x") , activebackground= "dark grey")
button5.place (x=20, y=160 , width=60 , height=50 )

button6 = Button(window , text="sqr" , font=('Arial', 15), borderwidth=5,command=lambda:operator("sqr"), activebackground= "dark grey")
button6.place (x=90, y=160 , width=60 , height=50 )

button7 = Button(window , text="sqrt" , font=('Arial', 15), borderwidth=5,command=lambda:operator("sqrt"), activebackground= "dark grey")
button7.place (x=160, y=160 , width=60 , height=50 )

button8 = Button(window , text="/" , font=('Arial', 15), borderwidth=5, command=lambda:operator("/"), activebackground= "dark grey")
button8.place (x=230, y=160 , width=60 , height=50 )

def num(number):
    result=entry_box.get()
    a= len(str(result))
    entry_box.insert(a,str(number))

button9 = Button(window , text="7" , font=('Arial', 15), borderwidth=5, command=lambda:num(7), activebackground= "dark grey")
button9.place (x=20, y=220 , width=60 , height=50 )

button10 = Button(window , text="8" , font=('Arial', 15), borderwidth=5, command=lambda:num(8), activebackground= "dark grey")
button10.place (x=90, y=220 , width=60 , height=50 )

button11= Button(window , text="9" , font=('Arial', 15), borderwidth=5, command=lambda:num(9), activebackground= "dark grey")
button11.place (x=160, y=220 , width=60 , height=50 )

button12= Button(window , text="*" , font=('Arial', 15), borderwidth=5, command=lambda:operator("*"), activebackground= "dark grey")
button12.place (x=230, y=220 , width=60 , height=50 )

button13 = Button(window , text="4" , font=('Arial', 15), borderwidth=5, command=lambda:num(4), activebackground= "dark grey")
button13.place (x=90, y=280 , width=60 , height=50 )

button14 = Button(window , text="5" , font=('Arial', 15), borderwidth=5, command=lambda:num(5), activebackground= "dark grey")
button14.place (x=160, y=280 , width=60 , height=50 )

button15 = Button(window , text="6" , font=('Arial', 15), borderwidth=5, command=lambda:num(6), activebackground= "dark grey")
button15.place (x=230, y=280 , width=60 , height=50 )

button16 = Button(window , text="-" , font=('Arial', 15), borderwidth=5, command=lambda:operator("-"), activebackground= "dark grey")
button16.place (x=20, y=280 , width=60 , height=50 )

button17 = Button(window , text="1" , font=('Arial', 15), borderwidth=5, command=lambda:num(1), activebackground= "dark grey")
button17.place (x=90, y=340 , width=60 , height=50 )

button18 = Button(window , text="2" , font=('Arial', 15), borderwidth=5, command=lambda:num(2), activebackground= "dark grey")
button18.place (x=160, y=340 , width=60 , height=50 )

button19 = Button(window , text="3" , font=('Arial', 15), borderwidth=5, command=lambda:num(3), activebackground= "dark grey")
button19.place (x=230, y=340 , width=60 , height=50 )

button20 = Button(window , text="+" , font=('Arial', 15), borderwidth=5, command=lambda:operator("+"), activebackground= "dark grey")
button20.place (x=20, y=340 , width=60 , height=50 )

def sign():
    if entry_box.get() == "":
        pass
    else:
        result=str(entry_box.get())
        a = result.find(".")
        if a == -1:
            result = int(result)
            b = result - (2 * result)
            entry_box.delete(0, END)
            entry_box.insert(0, str(b))
        else:
            result = float(result)
            b = result - (2 * result)
            entry_box.delete(0, END)
            entry_box.insert(0, str(b))


button21 = Button(window , text="+/-" , font=('Arial', 15), borderwidth=5, command=lambda:sign(), activebackground= "dark grey")
button21.place (x=90, y=400 , width=60 , height=50 )

button22 = Button(window , text="0" , font=('Arial', 15), borderwidth=5, command=lambda:num(0), activebackground= "dark grey")
button22.place (x=160, y=400 , width=60 , height=50 )

def dec():
    result=str(entry_box.get())
    a=result.find(".")
    if a==-1:
        result=result+"."
        entry_box.delete(0,END)
        entry_box.insert(0,result)
    else:
        pass

button23 = Button(window , text="." , font=('Arial', 15), borderwidth=5, command=lambda:dec(), activebackground= "dark grey")
button23.place (x=230, y=400 , width=60 , height=50 )

def equal():
    if current_operator == "/":
        rem2 = float(entry_box.get())
        entry_box.delete(0, END)
        final_result = rem1/rem2
        entry_box.insert(0, str(final_result))
    elif current_operator == "+":
        rem2 = float(entry_box.get())
        entry_box.delete(0, END)
        final_result = rem1+rem2
        entry_box.insert(0, str(final_result))
    elif current_operator == "-":
        rem2 = float(entry_box.get())
        entry_box.delete(0, END)
        final_result = rem1-rem2
        entry_box.insert(0, str(final_result))
    elif current_operator == "*":
        rem2 = float(entry_box.get())
        entry_box.delete(0, END)
        final_result = rem1*rem2
        entry_box.insert(0, str(final_result))
    else:
        pass
button24 = Button(window , text="=" , font=('Arial', 15), borderwidth=5, command=lambda:equal(), activebackground= "dark grey")
button24.place (x=20, y=400 , width=60 , height=50 )

window.mainloop()