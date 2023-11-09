from tkinter import *
from tkinter import scrolledtext
from technical.strToFunc import strToFunc
from chord_method.chord_method import chord_method
from bisection_method.bisection_method import bisection_method
from technical.find_interval import find_intrerval
from technical.def_pypplot import def_pyplot

"""номер корня"""
root1 = 0
root1_mass = []
root2 = 0
root2_mass = []


def clean1():  # функция отвечающая за очистку первой пенели ввода
    global root1
    txt1.delete(0, END)
    txt3.delete(0, END)
    txt5.delete(0, END)
    root1 = 0



def clean2():  # аналогичная фун. для второй панели
    global root2
    txt2.delete(0, END)
    txt4.delete(0, END)
    txt6.delete(0, END)
    root2 = 0
    


def clicked1():  # функция 1ой кнопки(вызов сорт. сорт слиянием )
    res = format(txt1.get())
    a, b = float(format(txt3.get())), float(format(txt5.get()))  # получение отрезка
    res = strToFunc(res)
    def_pyplot(res, a, b)
    res = chord_method(res, a, b)
    txt.insert(INSERT, f"\nметод хорд => {res}")


def clicked2():  # функция 2ой кнопки(вызов бисекции)
    res = format(txt2.get())  # получение данных из панели ввода
    a, b = float(format(txt4.get())), float(format(txt6.get()))  # получение отрезка
    res = strToFunc(res)
    res = bisection_method(res, a, b)
    txt.insert(INSERT, f"\nбисекция => {res}")


def clicked3():
    global root1
    global root1_mass
    if root1 == 0:
        res = format(txt1.get())
        root1_mass = find_intrerval(strToFunc(res))

    if len(root1_mass)>=root1+1:
        txt3.delete(0, END)
        txt5.delete(0, END)
        txt3.insert(
        0,f"{root1_mass[root1]["a"]}"
        )
        txt5.insert(
        0,f"{root1_mass[root1]["b"]}"
        )
        root1=root1+1

def clicked4():
    global root2
    global root2_mass
    if root2 == 0:
        res = format(txt2.get())
        root2_mass = find_intrerval(strToFunc(res))

    if len(root2_mass)>=root2+1:
        txt4.delete(0, END)
        txt6.delete(0, END)
        txt4.insert(
        0,f"{root2_mass[root2]["a"]}"
        )
        txt6.insert(
        0,f"{root2_mass[root2]["b"]}"
        )
        root2=root2+1

"""Создание класса ткинтера"""
window = Tk()
window.title("ТГУ")
window.geometry("900x400")

"""текстовые маркеры"""
lbl1 = Label(window, text="метод хорд")
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="метод пол. деления")
lbl2.grid(column=0, row=2)
lbl3 = Label(window, text="функция")
lbl3.grid(column=1, row=0)
lbl4 = Label(window, text="функция")
lbl4.grid(column=1, row=2)
lbl5 = Label(window, text="a")
lbl5.grid(column=3, row=0)
lbl6 = Label(window, text="a")
lbl6.grid(column=3, row=2)
lbl7 = Label(window, text="b")
lbl7.grid(column=5, row=0)
lbl8 = Label(window, text="b")
lbl8.grid(column=5, row=2)
"""панели ввода"""
txt1 = Entry(window, width=15)
txt1.insert(0, "2.2 - 2**x")
txt1.grid(column=2, row=0)
txt2 = Entry(window, width=15)
txt2.insert(0, "2.2 - 2**x")
txt2.grid(column=2, row=2)
txt3 = Entry(window, width=10)
txt3.grid(column=4, row=0)
txt4 = Entry(window, width=10)
txt4.grid(column=4, row=2)
txt5 = Entry(window, width=10)
txt5.grid(column=6, row=0)
txt6 = Entry(window, width=10)
txt6.grid(column=6, row=2)

"""кнопки"""
btn1 = Button(window, text="найти", command=clicked1)
btn1.grid(column=7, row=0)
btn2 = Button(window, text="найти", command=clicked2)
btn2.grid(column=7, row=2)
btn3 = Button(window, text="Очистить", command=clean1)
btn3.grid(column=8, row=0)
btn4 = Button(window, text="Очистить", command=clean2)
btn4.grid(column=8, row=2)
btn5 = Button(window, text="Промежутки", command=clicked3)
btn5.grid(column=9, row=0)
btn6 = Button(window, text="Промежутки", command=clicked4)
btn6.grid(column=9, row=2)

"""панель вывода"""
txt = scrolledtext.ScrolledText(window, width=40, height=20)
txt.grid(column=0, row=10)


window.mainloop()
