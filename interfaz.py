from tkinter import *
from analizadorLexico import analysisLex
from analizadorSintactico import analysisSyntax


def getTextInputLex():
     text= textCode.get(1.0,END)
     LabelResultado["text"]= analysisLex(text)

def getTextInputSin():
     text = textCode.get(1.0, END)
     LabelResultado["text"] = analysisSyntax(text)

#Interfaz Base
raiz =Tk()
raiz.title("Analizador GO")
raiz.resizable(0,0)
miFrame = Frame(raiz, width="650", height="700", bg="lightblue")
miFrame.pack()

Label(miFrame, text="Ingrese el texto para el analisis", fg="black", bg="lightblue").place(x=325, y=50, anchor="center")


# TEXTAREA
textCode = Text(miFrame, width=70, height=15, padx=10, pady=10)
textCode.place(x=325, y=200, anchor="center")
LabelResultado=Label(miFrame, text="Resultado: ", fg="black", bg="lightblue",font=("Arial Novas", 12))
LabelResultado.place(x=325, y=500, anchor="center")


# BOTONES
botonLexico = Button(miFrame, text="Analizador Lexico",command=getTextInputLex).place(x=150, y=600)
botonSintactico = Button(miFrame, text="Analizador Sintactico",command=getTextInputSin).place(x=400, y=600)


raiz.mainloop()