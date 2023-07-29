from tkinter import *

root = Tk()
root.geometry("400x650")
root.title("Calculator")
root.resizable(False, False)
root.configure(bg='black')

eq=''

def show(val):
    global eq
    eq+=val
    label_result.config(text=eq)

def clear():
    global eq
    eq=''
    label_result.config(text=eq)

def calaculate():
    global eq
    result=''
    if eq!='':
        try:
             result = eval(eq)
        except:
            result='Error'
            eq=''
        label_result.config(text=result)

label_result = Label(root, width=25, height=3, font=('arial', 30), text='')
label_result.pack()

C = Button(root, height=2, width=5, bg="blue", text="C",
           fg="white", font=('arial', 20), bd=1,command=lambda:clear()).place(x=7, y=150)
divide = Button(root, height=2, width=5, bg="#2a2d36",
                text="/", fg="white", font=('arial', 20), bd=1,command=lambda:show("/")).place(x=107, y=150)
Percent = Button(root, height=2, width=5, bg="#2a2d36",
                text="%", fg="white", font=('arial', 20), bd=1,command=lambda:show("%")).place(x=207, y=150)
star = Button(root, height=2, width=5, bg="#2a2d36",
                text="*", fg="white", font=('arial', 20), bd=1,command=lambda:show("*")).place(x=307, y=150)


seven = Button(root, height=2, width=5, bg="#2a2d36",
                text="7", fg="white", font=('arial', 20), bd=1,command=lambda:show("7")).place(x=7, y=250)
eight = Button(root, height=2, width=5, bg="#2a2d36",
                text="8", fg="white", font=('arial', 20), bd=1,command=lambda:show("8")).place(x=107, y=250)
nine = Button(root, height=2, width=5, bg="#2a2d36",
                text="9", fg="white", font=('arial', 20), bd=1,command=lambda:show("9")).place(x=207, y=250)
minus = Button(root, height=2, width=5, bg="#2a2d36",
                text="-", fg="white", font=('arial', 20), bd=1,command=lambda:show("-")).place(x=307, y=250)

four= Button(root, height=2, width=5, bg="#2a2d36",
                text="4", fg="white", font=('arial', 20), bd=1,command=lambda:show("4")).place(x=7, y=350)
five = Button(root, height=2, width=5, bg="#2a2d36",
                text="5", fg="white", font=('arial', 20), bd=1,command=lambda:show("5")).place(x=107, y=350)
six = Button(root, height=2, width=5, bg="#2a2d36",
                text="6", fg="white", font=('arial', 20), bd=1,command=lambda:show("6")).place(x=207, y=350)
plus = Button(root, height=2, width=5, bg="#2a2d36",
                text="+", fg="white", font=('arial', 20), bd=1,command=lambda:show("+")).place(x=307, y=350)

one = Button(root, height=2, width=5, bg="#2a2d36",
                text="1", fg="white", font=('arial', 20), bd=1,command=lambda:show("1")).place(x=7, y=450)
two = Button(root, height=2, width=5, bg="#2a2d36",
                text="2", fg="white", font=('arial', 20), bd=1,command=lambda:show("2")).place(x=107, y=450)
three = Button(root, height=2, width=5, bg="#2a2d36",
                text="3", fg="white", font=('arial', 20), bd=1,command=lambda:show("3")).place(x=207, y=450)

Zero = Button(root, height=2, width=11, bg="#2a2d36",
                text="0", fg="white", font=('arial', 20), bd=1,command=lambda:show("0")).place(x=7, y=550)
decimal = Button(root, height=2, width=5, bg="#2a2d36",
                text=".", fg="white", font=('arial', 20), bd=1,command=lambda:show(".")).place(x=207, y=550)

equal = Button(root, height=5, width=5, bg="orange",
                text="=", fg="white", font=('arial', 20), bd=1,command=calaculate).place(x=307, y=450)


root.mainloop()
