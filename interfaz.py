from tkinter import *
from analizadorLexico import analysisLex
from analizadorSintactico import analysisSyntax


def getTextInputLex():
    text= textCode.get(1.0,END)
    LabelResultado["text"] = analysisLex(text)

def getTextInputSin():
    text = textCode.get(1.0, END)
    LabelResultado["text"] = analysisSyntax(text)

def clear():
    textCode.delete(1.0, END)

#Interfaz Base
root =Tk()
root.title("Analizador GO")
root.resizable(0,0)
root.geometry("600x600")

# TEXTAREA
Label1 = Label(root, text="Analizador Sintactico de GO")
Label1.pack(pady=20)
textCode = Text(root, width=40, height=10)
textCode.pack(pady=20)

# BOTONES
buttonFrame = Frame(root)
buttonFrame.pack()
botonLimpiar = Button(buttonFrame, text="Limpiar", command=clear)
botonLimpiar.grid(row=0, column=0)
botonLexico = Button(buttonFrame, text="Lexico",command=getTextInputLex)
botonLexico.grid(row=0, column=1, padx=20)
botonSintactico = Button(buttonFrame, text="Sintactico",command=getTextInputSin)
botonSintactico.grid(row=0, column=2, padx=10)

LabelResultado = Label(root, text ='')
LabelResultado.pack(pady=20)

root.mainloop()