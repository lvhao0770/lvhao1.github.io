import tkinter as tk
import pyglet
window = tk.Tk()

window.title('卷积实现过程')
window.geometry('900x600')

txt = tk.StringVar()
txt.set('请选择连续信号或者是离散信号')
Bar = tk.Label(window, textvariable=txt, width=50, height=2)
Bar.place(x=300, y=10)

Barflag = True


def d_app():  # 离散信号
    global d_app1
    global d_app2
    global d_app3
    global d_app4
    global d_app5
    d_app1 = tk.Button(window, text='一', width=5, height=2, command=d_a1)
    d_app1.place(x=120, y=135)
    d_app2 = tk.Button(window, text='二', width=5, height=2, command=d_a2)
    d_app2.place(x=120, y=195)
    d_app3 = tk.Button(window, text='三', width=5, height=2, command=d_a3)
    d_app3.place(x=120, y=255)
    d_app4 = tk.Button(window, text='四', width=5, height=2, command=d_a4)
    d_app4.place(x=120, y=315)
    d_app5 = tk.Button(window, text='五', width=5, height=2, command=d_a5)
    d_app5.place(x=120, y=375)


def d_a1():  # gif动画
    ag_file = "abc.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()


def d_a2_1():
    global image_file
    Demonstration = tk.Canvas(window, height='550', width='750')
    image_file = tk.PhotoImage(file="abc.gif")
    Demonstration.create_image(0, 0, anchor="nw", image=image_file)
    Demonstration.place(x=200, y=50)


def d_a2():
    global Demonstration
    global image_file
    Demonstration.destroy()
    d_a2_1()


def d_a3():
    pass


def d_a4():
    pass


def d_a5():
    pass


def c_app():  # 连续信号
    d_app1.destroy()
    d_app2.destroy()
    d_app3.destroy()
    d_app4.destroy()
    d_app5.destroy()
    c_app1 = tk.Button(window, text='Ⅰ', width=5, height=2, command=c_a1)
    c_app1.place(x=120, y=135)
    c_app2 = tk.Button(window, text='Ⅱ', width=5, height=2, command=c_a2)
    c_app2.place(x=120, y=195)
    c_app3 = tk.Button(window, text='Ⅲ', width=5, height=2, command=c_a3)
    c_app3.place(x=120, y=255)
    c_app4 = tk.Button(window, text='Ⅳ', width=5, height=2, command=c_a4)
    c_app4.place(x=120, y=315)
    c_app5 = tk.Button(window, text='Ⅴ', width=5, height=2, command=c_a5)
    c_app5.place(x=120, y=375)


def c_a1():  # gif动画
    ag_file = "a.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()


def c_a2():
    pass


def c_a3():
    pass


def c_a4():
    pass


def c_a5():
    pass


def Discrete_app():  # 离散信号
    global image_file
    Demonstration = tk.Canvas(window, height='550', width='750')
    image_file = tk.PhotoImage(file="b.gif")
    Demonstration.create_image(0, 0, anchor="nw", image=image_file)
    Demonstration.place(x=200, y=50)
    d_app()
    exec(open("hello.py").read())


def Continuous_app():  # 连续信号
    global image_file
    Demonstration = tk.Canvas(window, height='550', width='750')
    image_file = tk.PhotoImage(file="a.gif")
    Demonstration.create_image(0, 0, anchor="nw", image=image_file)
    Demonstration.place(x=200, y=50)
    c_app()
    exec(open("hello.py").read())


def fc():
    global Barflag
    if Barflag == False:
        Barflag = True
        txt.set('连续信号')
        Demonstration.destroy()
        Continuous_app()


def fd():
    global Barflag
    global Demonstration
    if Barflag == True:
        Barflag = False
        txt.set('离散信号')
        Demonstration.destroy()
        Discrete_app()


Continuous = tk.Button(window, text='连续信号', width=10, height=3, command=fc)
Continuous.place(x=5, y=300)

Discrete = tk.Button(window, text='离散信号', width=10, height=3, command=fd)
Discrete.place(x=5, y=200)

Demonstration = tk.Canvas(window, height='550', width='750')
image_file = tk.PhotoImage(file="formulas.gif")
image = Demonstration.create_image(0, 0, anchor="nw", image=image_file)
Demonstration.place(x=200, y=50)


window.mainloop()
