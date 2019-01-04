import tkinter as tk

window = tk.Tk()

window.title('卷积实现过程')
window.geometry('900x600')

a=0

def lianxu_aniu():
    global a
    if a==2:
        exec(open("hello.py").read())
        a = a+1
    if a==1:
        exec(open("hello.py").read())
        a = a+1
    if a==0:
        exec(open("hello.py").read())
        a = a+1


def lisan_aniu():
    global a
    if a==5:
        exec(open("hello.py").read())
        a = a+1

    if a==4:
        exec(open("hello.py").read())
        a = a+1

    if a==3:
        exec(open("hello.py").read())
        a = 4

lianxu = tk.Button(window, text='连续信号', width=10, height=3, command=lianxu_aniu)
lianxu.place(x=100, y=30)

lisan = tk.Button(window, text='离散信号', width=10, height=3, command=lisan_aniu)
lisan.place(x=300, y=30)



window.mainloop()
