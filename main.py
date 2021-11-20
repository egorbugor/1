from tkinter import *
import time
import sys
import os
import xlsxwriter
import tkinter.messagebox as mb

nomer = 0
pos1 = 0
pos2 = 0
x = 0
tim1 = 0
iter = 0
timer = 0
txt = ""
people = 0
name2 = 0
path = "file" + str(nomer) + ".xlsx"

while True:
    if os.path.exists(path):
        nomer = nomer + 1
        path = "file" + str(nomer) + ".xlsx"
    if os.path.exists(path) == False:
        break
workbook = xlsxwriter.Workbook(path)
worksheet = workbook.add_worksheet()


window = Tk()
window.geometry('1600x900')
window.title("Добро пожаловать!")

text1 = "испытуемых : " + str(0)

def clicked():
    global iter
    global time0
    global timer
    global pos1
    global pos2
    global people
    if iter % 2 == 0:
        time0 = time.time()
        btn3.configure(fg = "green")
    if iter % 2 == 1:
        timer = round(time.time() - time0, 2)
        name = txt.get()
        lbl7.configure(text = str(timer) + " " + name)
        if name2 == 1:
            timer = round(name1 - timer, 2)
        worksheet.write(pos1, pos2, name)
        worksheet.write(pos1, pos2 + 1, timer)
        pos1 = pos1 + 1
        txt.delete(0, END)
        txt.insert(0, "")
        btn3.configure(state = DISABLED)
        people = people + 1
        lbl.configure(text="испытуемых : " + str(people))
        btn3.configure(fg="black")
    iter = iter + 1



def obnulenie():
    answer = mb.askyesno(
        title="Вопрос",
        message="Вы уверены?")
    if answer:
        if pos1 > 0:
            worksheet.write(pos1 - 1, pos2, " ")
            worksheet.write(pos1 - 1, pos2+1, " ")
            lbl.configure(text="испытуемых : " + str(people - 1))
        if pos1 == 0:
            pass


def close():
    sys.exit()

def absolut():
    global name1
    global name2
    if txt1.get() == "":
        lbl6.configure(bg="red")
    if txt1.get() != "":
        try:
            name1 = int(txt1.get())
            name2 = 1
            lbl6.configure(bg="green")
        except ValueError:
            lbl6.configure(bg="red")
def start():
    if txt.get() == "":
        lbl5.configure(bg="red")
    if txt.get() != "":
        btn3.configure(state = NORMAL)
        lbl5.configure(bg="green")

try:
    txt = Entry(window)
    txt.place(x=243, y=22)
    txt1 = Entry(window)
    txt1.place(x = 300, y = 82)

    lbl = Label(window, text=text1,  font=("Arial Bold", 20))
    lbl.place(x=1200, y=7)
    lbl1 = Label(window, text="последний результат:",  font=("Arial Bold", 20))
    lbl1.place(x=640, y=70)
    lbl5 = Label(window, text="имя испытуемого:",  font=("Arial Bold", 20))
    lbl5.place(x=0, y=10)
    lbl6 = Label(window, text="абсолютное значение:",  font=("Arial Bold", 20))
    lbl6.place(x=0, y=70)
    lbl7 = Label(window, text="0", font=("Arial Bold", 20))
    lbl7.place(x=930, y=70)

    btn = Button(window, text="начать", font =("Arial Bold", 20), command = start)
    btn.place(x=385, y=0)
    btn2 = Button(window, text="cохранить и выйти", font =("Arial Bold", 20), command = close)
    btn2.place(x=520, y=0)
    btn3 = Button(window, text="старт", font =("Arial Bold", 58),width = 35, height=8, command = clicked, state = DISABLED)
    btn3.place(x =0,y = 120)
    btn4 = Button(window, text="потдвердить", font =("Arial Bold", 20), command = absolut)
    btn4.place(x = 440, y = 60)
    btn5 = Button(window, text="удалить прошлый результат", font=("Arial Bold", 20), command=obnulenie)
    btn5.place(x=800, y=0)

    window.mainloop()
finally:
    workbook.close()