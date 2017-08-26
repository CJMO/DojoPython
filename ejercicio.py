from tkinter import*

root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo Python")

input_1 = StringVar()
operador=""

Tops = Frame (root, width=1600, height=80, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

frame = Frame (root, width=300, height=700, bg="powder blue", relief=SUNKEN)
frame.pack(side=TOP)

info = Label(Tops, font=("SHOWCARD GOTHIC", 50, "bold"), text="Dojo Python")
info.grid(row=0, column=0)

def botonClick(numero):
    global operator
    operator = operator + str(numero)
    input_1.set(operator)

def botonEvaluar(numero):
    global operator
    resultado = str(eval(operator))
    input_1.set(resultado)
    operator=""

txtDisplay = Entry(frame, font=("SHOWCARD GOTHIC", 50, "bold"), textvariable=input_1, bg="black" )
txtDisplay.grid(columnspan=4)

boton_1 = Button(frame, font=("SHOWCARD GOTHIC", 20, "bold"), command=lambda:botonClick(1)).grid(row=2, column=0)
boton_2 = Button(frame, font=("SHOWCARD GOTHIC", 20, "bold"), command=lambda:botonClick(2)).grid(row=2, column=1)

boton_suma = Button(frame, font=("SHOWCARD GOTHIC", 20, "bold"), command=lambda:botonClick("+")).grid(row=2, column=2)
boton_igual = Button(frame, font=("SHOWCARD GOTHIC", 20, "bold"), command=botonEvaluar().grid(row=2, column=3)



root.mainloop()
