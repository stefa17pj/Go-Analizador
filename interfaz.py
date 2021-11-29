from tkinter import *
from analizadorLexico import analysisLex
from analizadorSintactico import analysisSyntax


def getTextInputLex():
     text= textCode.get(1.0,END)
     LabelResultado["text"] = analysisLex(text)

def getTextInputSin():
     text = textCode.get(1.0, END)
     LabelResultado["text"] = analysisSyntax(text)

#Interfaz Base
raiz =Tk()
raiz.title("Analizador GO")
raiz.resizable(0,0)
miFrame = Frame()
miFrame.config(width="700", height="400", bg="gray")
miFrame.pack()
frameResult =  Frame()
frameResult.config(width='700', height='400')
frameResult.pack()
Label(miFrame, text="Ingrese el texto para el analisis", fg="black", bg="gray").place(x=325, y=50, anchor="center")


# TEXTAREA
textCode = Text(miFrame, width=70, height=15, padx=10, pady=10)
textCode.place(x=325, y=200, anchor="center")
LabelResultado= Label(frameResult, fg="black", bg = "white",font=("Arial Novas", 12))
LabelResultado.place(x=325, y=200, anchor="center")

# BOTONES
botonLexico = Button(frameResult, text="Analizador Lexico",command=getTextInputLex).place(x=100, y=50)
botonSintactico = Button(frameResult, text="Analizador Sintactico",command=getTextInputSin).place(x=400, y=50)


raiz.mainloop()