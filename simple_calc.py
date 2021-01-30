
from tkinter import *
root =Tk()
root.geometry('350x370')



root.title("SimpCalc")
root.configure(background='#d1ff00')
e =Entry(root, width=38, borderwidth=3, bg='white', fg='black')
a =Entry(root, width=20, borderwidth=2, bg='black', fg='white')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
a.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


def click(n):
    cu = e.get()
    e.delete(0, END)
    e.insert(0,str(cu)+str(n))
def delete():
    e.delete(0, END)
    a.delete(0, END)
def add():
    cu = str(e.get())
    global num1
    global act
    act='add'
    num1=int(cu)
    e.delete(0, END)
    e.insert(0, str(cu)+str('+'))
def multi():
    cu = str(e.get())
    global num1
    global act
    act='multi'
    num1=int(cu)
    e.delete(0, END)
    e.insert(0, str(cu)+str('x'))
def substr():
    cu = str(e.get())
    global num1
    global act
    act='sub'
    num1=int(cu)
    e.delete(0, END)
    e.insert(0, str(cu)+str('-'))
def div():
    cu = str(e.get())
    global num1
    global act
    act='div'
    num1=int(cu)
    e.delete(0, END)
    e.insert(0, str(cu)+str('/'))

def equal():
    now=str(e.get())
    e.delete(0, END)
    a.delete(0, END)
    if act=='add':
        a1,a2=now.split('+')
        con=int(int(a1)+int(a2))
        now=str(e.get())
    if act=='multi':
        a1,a2=now.split('x')
        con=int(int(a1)*int(a2))
    if act=='sub':
        a1,a2=now.split('-')
        con=int(int(a1)-int(a2))
    if act=='div':
        a1,a2=now.split('/')
        con=int(int(a1)/int(a2))
        
    a.insert(0, con)



b_1 =Button(root, text="1", padx=25, pady=11, command=lambda: click(1), bg='#94ffff', font='chilanka')
b_2 =Button(root, text="2", padx=20, pady=11, command=lambda: click(2), bg='#94ffff', font='chilanka')
b_3 =Button(root, text="3", padx=20, pady=11, command=lambda: click(3), bg='#94ffff', font='chilanka')
b_4 =Button(root, text="4", padx=20, pady=11, command=lambda: click(4), bg='#94ffff', font='chilanka')
b_4 =Button(root, text="4", padx=20, pady=11, command=lambda: click(4), bg='#94ffff', font='chilanka')
b_5 =Button(root, text="5", padx=20, pady=11, command=lambda: click(5), bg='#94ffff', font='chilanka')
b_5 =Button(root, text="5", padx=20, pady=11, command=lambda: click(5), bg='#94ffff', font='chilanka')
b_6 =Button(root, text="6", padx=20, pady=11, command=lambda: click(6), bg='#94ffff', font='chilanka')
b_7 =Button(root, text="7", padx=20, pady=11, command=lambda: click(7), bg='#94ffff', font='chilanka')
b_8 =Button(root, text="8", padx=20, pady=11, command=lambda: click(8), bg='#94ffff', font='chilanka')
b_9 =Button(root, text="9", padx=20, pady=11, command=lambda: click(9), bg='#94ffff', font='chilanka')
b_0 =Button(root, text="0", padx=20, pady=11, command=lambda: click(0), bg='#94ffff', font='chilanka')


b_add =Button(root, text="+", padx=39, pady=11, command=add, bg='#72b808', font='chilanka')
b_equal =Button(root, text="=", padx=55, pady=11, command=equal, bg='#72b808', font='chilanka')
b_clear =Button(root, text="Clear", padx=30, pady=11, bg='#72b808', font='chilanka',command=delete)
b_multi =Button(root, text='x', padx=39, pady=11, bg='#72b808', font='chilanka', command=multi)
b_substr =Button(root, text='-', padx=39, pady=11, bg='#72b808', font='chilanka', command=substr)
b_div =Button(root, text='/', padx=39, pady=11, bg='#72b808', font='chilanka', command=div)
b_quit=Button(root, text='Quit', padx=10, pady=8, bg='#72b808', font='chilanka', command=root.quit)

b_1.grid(row=4, column=0)
b_2.grid(row=4, column=1)
b_3.grid(row=4, column=2)
b_4.grid(row=3, column=0)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_7.grid(row=2, column=0)
b_8.grid(row=2, column=1)
b_9.grid(row=2, column=2)
b_0.grid(row=5, column=1)
b_add.grid(row=5, column=0)
b_equal.grid(row=7, column=1)
b_clear.grid(row=5, column=2)
b_substr.grid(row=6, column=0)
b_div.grid(row=6, column=1)
b_multi.grid(row=6, column=2)
b_quit.grid(row=1, column=2)


root.mainloop()

