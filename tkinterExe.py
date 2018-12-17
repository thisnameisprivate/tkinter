from tkinter import *


# 用数组定义一个棋盘，棋盘大小为 15×15
# 数组索引代表位置，
# 元素值代表该位置的状态：-1代表没有棋子，0代表有黑棋，1代表有白棋。

def callback(event):
    global tag, tagx, tagy, a
    color = ["black", "white"]
    x = round(event.x / mesh) - 1
    y = round(event.y / mesh) - 1
    errorX = mesh * (x + 1) - event.x
    errorY = mesh * (y + 1) - event.y
    dis = (errorX ** 2 + errorY ** 2) ** 0.5
    if QP[x][y] == -1 and dis < K / 2 * mesh and stop == 0:
        a.config(text=key[(tag + 1) % 2], fg=color[(tag + 1) % 2])
        QP[x][y] = tag
        canvas.create_oval(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                           fill=color[tag])
        v = [[0, 1], [1, 0], [1, 1], [1, -1]]
        for i in v:
            x1, y1 = x, y
            while x1 < num - 1 and x1 > 0 and y1 > 0 and y1 < num - 1:
                x1 += i[0]
                y1 += i[1]
            count = 0
            while x1 <= num - 1 and x1 >= 0 and y1 >= 0 and y1 <= num - 1:
                if QP[x1][y1] == tag:
                    count += 1
                    if count == 5:
                        win()
                else:
                    count = 0
                x1 -= i[0]
                y1 -= i[1]
        tag = (tag + 1) % 2
        tagx, tagy = x, y


def restart():
    global QP, tag, a, b, stop
    QP = []
    for i in range(num):
        QP.append([-1] * num)
    canvas.create_rectangle(mesh - 20, mesh - 20, mesh * num + 20, mesh * num + 20, fill="yellow")
    for i in range(num):
        canvas.create_line(mesh, mesh * (i + 1), mesh * num, mesh * (i + 1))
        canvas.create_line(mesh * (i + 1), mesh, mesh * (i + 1), mesh * num)
    tag = 0
    stop = 0
    a.config(text=key[tag], fg=color[tag])
    b.config(text="走棋", fg=color[tag])


def regret():
    if stop != 1:
        QP[tagx][tagy] = -1
        x, y = tagx, tagy
        # 这里写的这么麻烦主要是因为 tkinter 蛋疼的画图功能不够强大。
        # 没有办法设置棋子边界颜色，悔棋后会留下印记。

        # 在棋子处，用黄色先覆盖
        canvas.create_rectangle(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                                fill="yellow")
        # 在黑色的边界处用画了黄颜色的线条
        canvas.create_line(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) - Qr, mesh * (y + 1) + Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) - Qr, mesh * (y + 1) + Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) + Qr, mesh * (y + 1) + Qr, mesh * (x + 1) + Qr, mesh * (y + 1) - Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) + Qr, mesh * (y + 1) - Qr, mesh * (x + 1) - Qr, mesh * (y + 1) - Qr,
                           fill="yellow")
        # 最后再画上棋线
        canvas.create_line(mesh * (x + 1), mesh * (y + 1) - mesh / 2, mesh * (x + 1), mesh * (y + 1) + mesh / 2)
        canvas.create_line(mesh * (x + 1) - mesh / 2, mesh * (y + 1), mesh * (x + 1) + mesh / 2, mesh * (y + 1))


def lose():
    global stop
    a.config(text=key[tag], fg=color[tag])
    b.config(text="认输", fg='black')
    stop = 1  # stop = 1时不能再放棋子了


def win():
    global stop
    a.config(text=key[tag], fg=color[tag])
    b.config(text="获胜", fg='red')
    stop = 1


if __name__ == '__main__':

    tag = 0  # tag标记该轮哪家走，0代表黑方，1代表白方
    stop = 0
    num = 18  # 棋盘网格数量
    K = 0.9  # 点击的灵敏度 0~1 之间
    Qr = 0.45 * 20  # 棋子的大小，前面的系数在0~0.5之间选取

    px = 5
    py = 50
    wide = 60
    high = 30
    mesh = round(400 / num)
    key = ["黑方", "白方"]
    color = ["black", "white"]

    # 初始化棋盘
    QP = []
    for i in range(num):
        QP.append([-1] * num)

    tk = Tk()
    tk.geometry(str((num + 1) * mesh + 2 * px) + 'x' + str((num + 1) * mesh + py + px))
    tk.title('五子棋')
    # 构造棋盘界面
    asdf = Canvas(tk, width=(num + 1) * mesh + 2 * px, height=(num + 1) * mesh + py + px)
    asdf.place(x=0, y=0)
    asdf.create_rectangle(0, 0, (num + 1) * mesh + 2 * px, (num + 1) * mesh + py + px, fill="green")
    canvas = Canvas(tk, width=str((num + 1) * mesh), height=str((num + 1) * mesh))
    canvas.place(x=px, y=py)
    canvas.create_rectangle(mesh - 20, mesh - 20, mesh * num + 20, mesh * num + 20, fill="yellow")
    for i in range(num):
        canvas.create_line(mesh, mesh * (i + 1), mesh * num, mesh * (i + 1))
        canvas.create_line(mesh * (i + 1), mesh, mesh * (i + 1), mesh * num)
    canvas.bind("<Button-1>", callback)

    # 几个按钮
    Button(tk, text='开始', command=restart).place(x=2 * px, y=(py - high) / 2, width=wide, heigh=high)
    Button(tk, text='重来', command=restart).place(x=2 * px + 60 + 10, y=(py - high) / 2, width=wide, heigh=high)
    Button(tk, text='悔棋', command=regret).place(x=(num + 1) * mesh + px - wide - px - 60 - 10, y=(py - high) / 2,
                                                width=wide, heigh=high)
    Button(tk, text='认输', command=lose).place(x=(num + 1) * mesh + px - wide - px, y=(py - high) / 2, width=wide,
                                              heigh=high)

    # 中间的文字
    a = Label(tk, text=key[tag], fg=color[tag], bg='green', font=("Times", "14", "bold"))
    b = Label(tk, text="走棋", fg=color[tag], bg='green', font=("Times", "14", "bold"))
    a.place(x=2 * px + 60 + 10 + 90, y=(py - high) / 2 + 4)
    b.place(x=(num + 1) * mesh + px - wide - px - 10 - 42 - 90, y=(py - high) / 2 + 4)

    tk.mainloop()
