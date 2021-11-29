import tkinter as tk
from tkinter import ttk
from tkcode import CodeEditor

root = tk.Tk()
root.title("Editor de Codigo GO")
root.option_add("*tearOff", 0)

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Abrir...")
file_menu.add_command(label="Guardar")
file_menu.add_command(label="Guardar como...")
file_menu.add_separator()
file_menu.add_command(label="Salir")

help_menu = tk.Menu(menubar)
help_menu.add_command(label="Ayuda")
help_menu.add_command(label="Acerca de")

menubar.add_cascade(menu=file_menu, label="Archivo")
menubar.add_cascade(menu=help_menu, label="Ayuda")

root.config(menu=menubar)

notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="main.go")
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=70,
    height=30,
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
	fmt.Println("Hello, World")
}
"""


root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()