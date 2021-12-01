from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcode import CodeEditor
from analizadorLexico import analysisLex
from analizadorSintactico import analysisSyntax

root = Tk()
root.title("Editor de Codigo GO")
root.option_add("*tearOff", 0)
root.geometry("500x550")

global archivo_abierto
archivo_abierto = False

# analizador lexico
def getTextInputLex():
    text = code_editor.get(1.0, END)
    LabelResultado["text"] = analysisLex(text)

# analizador sintactico
def getTextInputSin():
    text = code_editor.get(1.0, END)
    LabelResultado["text"] = analysisSyntax(text)

def nuevo_archivo():
    code_editor.delete(1.0, END)
    global archivo_abierto
    archivo_abierto = False
    notebook.tab(tab_1, text="main.go") # reseteamos

# abrir un archivo
def abrir_archivo():
    code_editor.delete(1.0, END) # borrar texto anterior
    archivo = filedialog.askopenfilename(initialdir="./" ,title="Abrir...", filetypes=(("Archivos GO", "*.go"), ("All", "*.*")))
    # comprobamos que hay un archivo abierto
    if archivo:
        # de esta forma podremos acceder al archivo abierto para guardar informacion 
        global archivo_abierto
        archivo_abierto = archivo
    nombre = archivo.split("/")[-1]
    notebook.tab(tab_1, text=nombre) # poner el nombre del archivo en la pestaña 
    # añadimos el texto del archivo al cuadro de texto
    archivo = open(archivo)
    codigo = archivo.read()
    code_editor.content = codigo
    archivo.close()

# guardar archivo como...
def guardar_como():
    archivo = filedialog.asksaveasfilename(defaultextension=".go", initialdir="./", title="Guardar Archivo", filetypes=(("Archivos GO", "*.go"), ("All", "*.*")))
    if archivo:
        nombre = archivo.split("/")[-1]
        notebook.tab(tab_1, text=nombre) # poner el nombre del archivo en la pestaña 
        # guardamos el archivo
        archivo = open(archivo, "w")
        archivo.write(code_editor.get(1.0, END))
        archivo.close()

def guardar():
    global archivo_abierto
    if archivo_abierto: #si existe un archivo abierto
        # guardamos el archivo
        archivo = open(archivo_abierto, "w")
        archivo.write(code_editor.get(1.0, END))
        archivo.close()
    else: #sino, lo guardamos como...
        guardar_como()

menubar = Menu(root)
# menu desplegable archivo
menu_archivo = Menu(menubar)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo) # limpiar cuadro de texto
menu_archivo.add_command(label="Abrir...", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_command(label="Guardar como...", command=guardar_como)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
# menu editar
menu_editar = Menu(menubar)
menu_editar.add_command(label="Deshacer", command=lambda: code_editor.edit_undo, accelerator="(Ctrl+z)")
menu_editar.add_command(label="Rehacer", command=lambda: code_editor.edit_redo, accelerator="(Ctrl+y)")
# Cambiar tema del editor de codigo
menu_tema = Menu(menubar)
menu_tema.add_command(label="Azure", command=lambda: code_editor.update_highlighter("azure"))
menu_tema.add_command(label="Dracula", command=lambda: code_editor.update_highlighter("dracula"))
menu_tema.add_command(label="Mariana", command=lambda: code_editor.update_highlighter("mariana"))
menu_tema.add_command(label="Monokai", command=lambda: code_editor.update_highlighter("monokai"))
menu_tema.add_command(label="Monokai-plus-plus", command=lambda: code_editor.update_highlighter("monokai-plus-plus"))
# menu desplegable ayuda
menu_ayuda = Menu(menubar)
menu_ayuda.add_command(label="Ayuda")
menu_ayuda.add_command(label="Acerca de")
# menus desplegables 
menubar.add_cascade(menu=menu_archivo, label="Archivo")
menubar.add_cascade(menu=menu_editar, label="Editar")
menubar.add_cascade(menu=menu_tema, label="Temas")
menubar.add_cascade(menu=menu_ayuda, label="Ayuda")
root.config(menu=menubar)
# BOTONES
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM, fill=X, pady=10)
botonLimpiar = Button(buttonFrame, text="Limpiar", command=lambda: code_editor.delete(1.0, END))
botonLimpiar.grid(row=0, column=0, padx=20)
botonLexico = Button(buttonFrame, text="Lexico", command=getTextInputLex)
botonLexico.grid(row=0, column=1, padx=20)
botonSintactico = Button(buttonFrame, text="Sintactico / Semantico", command=getTextInputSin)
botonSintactico.grid(row=0, column=2, padx=20)
LabelResultado = Label(root, text =' ')
LabelResultado.pack(pady=20, side=BOTTOM)
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

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()