import tkinter as tk

window = tk.Tk()

window.title('卷积实现过程')
window.geometry('900x600')


def lianxugifOK():  # gif动画
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


def lisangifOK():  # gif动画
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

    
a = 0


def lianxu_aniu():
    global a
    if a == 2:
        exec(open("hello.py").read())
        a = a + 1
        
    if a == 1:
        exec(open("hello.py").read())
        a = a + 1
    if a == 0:
        exec(open("hello.py").read())
        a = a + 1
        lianxugifOK()


def lisan_aniu():
    global a
    if a == 5:
        exec(open("hello.py").read())
        a = a + 1

    if a == 4:
        exec(open("hello.py").read())
        a = a + 1

    if a == 3:
        exec(open("hello.py").read())
        a = 4


lianxu = tk.Button(window, text='连续信号', width=10,
                   height=3, command=lianxu_aniu)
lianxu.place(x=100, y=30)

lisan = tk.Button(window, text='离散信号', width=10, height=3, command=lisan_aniu)
lisan.place(x=300, y=30)


window.mainloop()
