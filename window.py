from tkinter import *
import tkinter.scrolledtext as scroll

WIDTH = 38


def authorization():
    pass


def enter():
    

root = Tk()
root.geometry("+10+10")
root.title('git Hub')
root.attributes("-topmost", True)

canvas = Canvas(root, bg='white')
canvas.pack()

lf = LabelFrame(canvas, text='Авторизация', bd=4, fg='red')
lf.pack()
log = Entry(lf, width=WIDTH, font='Arial 14', fg='grey')
log.pack()
mail = Entry(lf, width=WIDTH, font='Arial 14', fg='grey')
mail.pack()
pas = Entry(lf, width=WIDTH, font='Arial 14', fg='grey')
pas.pack()
rep = Entry(lf, width=WIDTH, font='Arial 14', fg='grey')
rep.pack()
log.insert(0, 'login')
mail.insert(0, 'mail')
pas.insert(0, 'password')
rep.insert(0, 'repository')
log.get
btn = Button(lf, text='Enter', fg='black', command=authorization, bg='green', font='Arial 14')
btn.pack()
btn2 = Button(lf, text='Back', fg='black', command=root.destroy, bg='red', font='Arial 14')
btn2.pack()
lf2 = LabelFrame(canvas, text=' cmd ', height=250, bd=4, fg='blue')
lf2.pack_propagate(False)
lf2.pack(fill='both')
text = scroll.ScrolledText(lf2, font='Arial 12')
text.pack()
root.bind('1', enter)

root.mainloop()
