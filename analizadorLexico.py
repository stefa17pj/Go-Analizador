import ply.lex as lex

#Analizador Lexico GO

#Integrantes
# Lavayen Santana Stefany Marisela
# Puchaicela Buri Bryan Alexander
# Veliz Chavez Jahir David

#------------------------------------------------------------
# List of token names.   This is always required
#------------------------------------------------------------

#Palabras reservadas: Stefany
reserved = {
    'break': 'BREAK',
    'else': 'ELSE',
    'for': 'FOR',
    'if': 'IF',
    'var': 'VAR',
    'case': 'CASE',
    'func': 'FUNC',
    'continue': 'CONTINUE',
    #'fallthrough': 'FALLTHROUGH',
    #'goto': 'GOTO',
    #'interface': 'INTERFACE',
    'map': 'MAP',
    #'package': 'PACKAGE',
    #'range': 'RANGE',
    'return': 'RETURN',
    #'select': 'SELECT',
    #'struct': 'STRUCT',
    'switch': 'SWITCH',
    #'type': 'TYPE',
    'var': 'VAR',
    #'chan': 'CHAN',
    #'go': 'GO',
    'default': 'DEFAULT',
    #'defer': 'DEFER',
    #'import': 'IMPORT',
    #'const': 'CONST',
    'true': 'TRUE',
    'false': 'FALSE',
    #id de tipos de datos
    'bool': 'BOOL',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING'
}

tokens = (
    'VARIABLE',
    'DECLARADOR',
    #Tipo de Datos
    'ENTERO',
    'FLOTANTE',
    'CADENA',
    #Operadores Matematicos
    'SUMA',
    'RESTA',
    'PRODUCTO',
    'DIVISION',
    'MODULO',
    #Operadores Logicos
    'MAYORQUE',
    'MENORQUE',
    'DIFERENTE',
    'ESIGUAL',
    'MENORIGUAL',
    'MAYORIGUAL',
    'AND',
    'OR',
    'NEGACION',
    #Operadores Asignacion
    'MASIGUAL',
    'MENOSIGUAL',
    'IGUAL',
    #Delimitadores
    'INCREMENTO',
    'PARLEFT',
    'PARRIGHT',
    #'COMENTARIO',
    'COMA',
    'DOSPUNTOS',
    'PUNTOCOMA',
    'LLAVELEFT',
    'LLAVERIGHT',
    'CORCHRIGHT',
    'CORCHLEFT',
    #Caracteres
    #'BARRAINVERSA',
    #'ESPACIO',
    #Imprimir
    'IMPRIMIR',
    'AMPERSAND',
    #'COMILLA',
    #Lectura de datos
    'SCAN'

) + tuple(reserved.values())

#-----------------------------------------------
# Regular expression rules for simple tokens
#-----------------------------------------------

# Operadores Aritmetico: Stefany
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_PRODUCTO = r'\*'
t_DIVISION = r'\/'
t_MODULO = r'\%'

# Operadores Asignacion: Stefany
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_IGUAL = r'='
t_DECLARADOR = r':='

# Operadores logicos: Stefany
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_DIFERENTE = r'!='
t_ESIGUAL = r'=='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NEGACION = r'!'

# Delimitadores: Stefany
t_PARLEFT = r'\('
t_PARRIGHT = r'\)'
t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_INCREMENTO = r'\+\+'
t_LLAVELEFT = r'\{'
t_LLAVERIGHT = r'\}'
t_CORCHRIGHT = r'\]'
t_CORCHLEFT = r'\['

# Caracteres
#t_BARRAINVERSA = r'\\'
#t_ESPACIO = r'\s'
t_AMPERSAND = r'&'

# Imprimir: Stefany
def t_IMPRIMIR(t):
    r'fmt\.Print(ln|f)?'
    return t

# Lectura: Stefany
def t_SCAN(t):
    r'fmt\.Scan(ln|f)?'
    return t

#comillas :Stefany 
def t_COMILLA (t):
    r'(\'|\")'

# Flotante : Bryan
def t_FLOTANTE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

# Numeros Enteros: Stefany
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Cadenas: Stefany
def t_CADENA(t):
    r'("[^"]*"|\'[^\']*\')'
    return t

# Variable: Bryan
def t_VARIABLE(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# Comentario: Bryan
def t_COMENTARIO(t):
    r'(\//.*|\/\*.*\*\/)'
    pass

#IGNORE
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("No se reconoce '%s'" % t.value[0])
    t.lexer.skip(1)

#Algorithm

lexer = lex.lex()
text = open("textALexico.txt")
data = text.read()
'''
def analysis(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

analysis(data)
'''