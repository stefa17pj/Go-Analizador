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

    #tipo de dato;

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

# Tipo de datos
t_BOOLEAN = r'true|false'  


t_DECLARADOR = r':='

#Palabras reservadas: Stefany
t_IF = r'(if)'
t_BREAK = r'(break)'
t_ELSE = r'(else)'
t_FOR = r'(for)'
t_CASE = r'(case)'
t_FUNC = r'func'
t_CONTINUE = r'continue'
t_FALLTHROUGH = r'fallthrough'
t_GOTO = r'goto'
t_INTERFACE = r'interface'
t_MAP = r'map'
t_PACKAGE = r'package'
t_RANGE = r'range'
t_RETURN = r'return'
t_SELECT = r'select'
t_STRUCT = r'struct'
t_SWITCH = r'switch'
t_TYPE = r'type'
t_VAR = r'var'
t_CHAN = r'chan'
t_GO = r'go'
t_DEFAULT = r'default'
t_DEFER = r'defer'
t_IMPORT = r'import'
t_CONST = r'const'


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
