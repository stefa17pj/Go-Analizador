from tkinter import *
from tkinter import ttk
from tkcode import CodeEditor
from analizadorLexico import analysisLex
from analizadorSintactico import analysisSyntax

root = Tk()
root.title("Editor de Codigo GO")
root.option_add("*tearOff", 0)
root.geometry("400x500")

menubar = Menu(root)
# menu desplegable archivo
menu_archivo = Menu(menubar)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir...")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como...")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir")
# menu desplegable ayuda
menu_ayuda = Menu(menubar)
menu_ayuda.add_command(label="Ayuda")
menu_ayuda.add_command(label="Acerca de")
# menus desplegables 
menubar.add_cascade(menu=menu_archivo, label="Archivo")
menubar.add_cascade(menu=menu_ayuda, label="Ayuda")
root.config(menu=menubar)
# editor de codigo
notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="main.go")
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=40,
    height=10,
    language="go",
    highlighter="monokai",
    autofocus=True,
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,
)

code_editor.pack(fill="both", expand=True)

code_editor.content = """package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}
"""

def getTextInputLex():
    text= code_editor.get(1.0, END)
    LabelResultado["text"] = analysisLex(text)

def getTextInputSin():
    text = code_editor.get(1.0, END)
    LabelResultado["text"] = analysisSyntax(text)

def clear():
    code_editor.delete(1.0, END)

# BOTONES
buttonFrame = Frame(root)
buttonFrame.pack(fill=X, pady=10)
botonLimpiar = Button(buttonFrame, text="Limpiar", command=clear)
botonLimpiar.grid(row=0, column=0, padx=20)
botonLexico = Button(buttonFrame, text="Lexico", command=getTextInputLex)
botonLexico.grid(row=0, column=1, padx=20)
botonSintactico = Button(buttonFrame, text="Sintactico / Semantico", command=getTextInputSin)
botonSintactico.grid(row=0, column=2, padx=20)

LabelResultado = Label(root, text =' ')
LabelResultado.pack(pady=20)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()