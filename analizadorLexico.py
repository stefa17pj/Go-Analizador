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
    'byte'      : 'BYTES',
}

tokens = (
    'IDENTIFICADOR',
    'VARIABLE',
    'DECLARADOR',
    'TIPODEDATO',
    #Tipo de Datos
    'NUMERO',
    'FLOTANTE',
    'CADENA',
    'BOOLEAN',
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
    'COMENTARIO',
    'COMA',
    'DOSPUNTOS',
    'PUNTOCOMA',
    'LLAVELEFT',
    'LLAVERIGHT',
    'CORCHRIGHT',
    'CORCHLEFT',
    # Caracteres
    'BARRAINVERSA',
    'ESPACIO',
    #Estructuras de datos: Jahir
    'ARRAY',
    'SLICE',
    'MAPA',
    'METODO',
    'IMPRIMIR',
    'PUNTERO'
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

# Imprimir: Stefany
def t_IMPRIMIR(t):
    r'fmt\.Print(ln|f)*'
    return t

# Caracteres
t_BARRAINVERSA = r'\\'
t_ESPACIO = r'\s'

# Tipo de datos : Bryan
t_BOOLEAN = r'true|false'  


t_DECLARADOR = r':='

# Palabras reservadas: Stefany
t_BREAK = r'break'
t_ELSE = r'else' 
t_FOR = r'for'  
t_IF = r'if'   
t_CASE = r'case' 
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

# tipo de dato
t_BOOLEANO = r'bool'
t_ENTERO = r'int'
t_STRING = r'string'
t_BYTES = r'byte'

# ESTRUCTURAS DE DATOS: Jahir
## Array
def t_ARRAY(t):
    r'\[\d*\](bool|int|float|complex|string)({.*})?'
    return t

## Slices
def t_SLICE(t):
    r'[a-zA-Z_]([\w])*\[\d+\:\d+\]'
    return t

## Mapa
def t_MAPA(t):
    r'map\[(bool|int|float|complex|string)\](bool|int|float|complex|string){.*}'
    return t

# METODOS: Jahir
def t_METODO(t):
    r'[a-zA-Z]([\w])*\.?[a-zA-Z]([\w])*\([a-zA-Z_]([\w])*\)'
    return t


#TIPO DE DATO: Jahir
def t_TIPODEDATO(t):
    r'bool|int|float|complex|string'
    t.type = reserved.get(t.value, 'TIPODEDATO')
    return t


# PUNTEROS: Jahir
def t_PUNTERO(t):
    r'\*(bool|int|float|complex|string)'
    return t


# Variables: Stefany
def t_VARIABLE(t):
    r'[a-zA-Z_]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]
        return t
    else:
        return t


# IDENTIFICADOR, Flotante : Bryan
def t_FLOTANTE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t


# Numeros: Stefany
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Cadenas: Stefany
def t_CADENA(t):
    r'("[^"]*"|\'[^\']*\')'
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
