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
    'case': 'CASE',
    'func': 'FUNC',
    'continue': 'CONTINUE',
    'fallthrough': 'FALLTHROUGH',
    'goto': 'GOTO',
    'interface': 'INTERFACE',
    'map': 'MAP',
    'package': 'PACKAGE',
    'range': 'RANGE',
    'return': 'RETURN',
    'select': 'SELECT',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'type': 'TYPE',
    'var': 'VAR',
    'chan': 'CHAN',
    'go': 'GO',
    'default': 'DEFAULT',
    'defer': 'DEFER',
    'import': 'IMPORT',
    'const': 'CONST',

    #tipo de dato: Bryan P
    'bool'      : 'BOOLEANO',
    'int'       : 'ENTERO',
    'string'    : 'STRING',
    'float64'   : 'FLOAT_64',
    'float'     : 'FLOAT_32',
    'byte'      : 'BYTES',
    'complex64' : 'NUMBER_COMPLEX'
}

tokens = (
    'IDENTIFICADOR',
    'VARIABLE',
    'DECLARADOR',
    #Tipo de Datos
    'NUMBER',
    'FLOAT',
    'CADENA',
    'BOOLEAN',
    #Operadores Matematicos
    'SUMA',
    'RESTA',
    'PRODUCT',
    'DIV',
    'MOD',
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
    'COMENTARIO',
    'COMA',
    'PUNTOCOMA',
    # Caracteres
    'BARRAINVERSA',
    'ESPACIO'
) + tuple(reserved.values())

#-----------------------------------------------
# Regular expression rules for simple tokens
#-----------------------------------------------

# Operadores Aritmetico: Stefany
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_PRODUCT = r'\*'
t_DIV     = r'\/'
t_MOD     = r'\%'

# Operadores Asignacion: Stefany
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_IGUAL = r'='

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
t_INCREMENTO = r'\+\+'

# Caracteres
t_BARRAINVERSA = r'\\'
t_ESPACIO = r'\s'

# Tipo de datos : Bryan
t_BOOLEAN = r'true|false'  


t_DECLARADOR = r':='


# Variables: Stefany
def t_VARIABLE(t):
    r'[a-z]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]
        return t
    else:
        return t


# IDENTIFICADOR : Bryan
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t


# Numeros: Stefany
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Cadenas: Stefany
def t_CADENA(t):
    r'"\w+(_\dw)*"'
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


def analysis(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


analysis(data)
