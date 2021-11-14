import ply.lex as lex 

#Analizador Lexico GO

#------------------------------------------------------------
# List of token names.   This is always required
#------------------------------------------------------------

#Stefany Lavayen: palabras reservadas 
reserved = {
  'break'       : 'BREAK',
  'else'        : 'ELSE',
  'for'         : 'FOR',
  'if'          : 'IF',
  'case'        : 'CASE',
  'func'        : 'FUNC',
  'continue'    : 'CONTINUE',
  'fallthrough' : 'FALLTHROUGH',
  'goto'        : 'GOTO',
  'interface'   : 'INTERFACE',
  'map'         : 'MAP',
  'package'     : 'PACKAGE',
  'range'       : 'RANGE',
  'return'      : 'RETURN',
  'select'      : 'SELECT',
  'struct'      : 'STRUCT',
  'switch'      : 'SWITCH',
  'type'        : 'TYPE',
  'var'         : 'VAR',
  'chan'        : 'CHAN', 
  'go'          : 'GO',
  'default'     : 'DEFAULT',
  'defer'       : 'DEFER',
  'import'      : 'IMPORT',
  'const'       : 'CONST'
}

tokens = (
  'IDENTIFICADOR',
  'NUMBER',
  'CADENA',
  'PARLEFT',
  'PARRIGHT',
  'MAYORQUE',
  'MENORQUE',
  'IGUAL',
  'COMENTARIO',
  'COMA',
  'BOOLEAN'
 ) + tuple(reserved.values())

# ---------------------------------------------
# Regular expression rules for simple tokens
#-----------------------------------------------

t_PARLEFT  = r'\('
t_PARRIGHT = r'\)'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL    = r'='
t_COMA     = r','
t_BOOLEAN  = r'true|false'


#Stefany Lavayen: palabras reservadas
t_IF          = r'(if)'
t_BREAK       = r'(break)'
t_ELSE        = r'(else)'
t_FOR         = r'(for)'
t_CASE        = r'(case)'
t_FUNC        = r'func'       
t_CONTINUE    = r'continue'   
t_FALLTHROUGH = r'fallthrough'
t_GOTO        = r'goto'       
t_INTERFACE   = r'interface'  
t_MAP         = r'map'        
t_PACKAGE     = r'package'    
t_RANGE       = r'range'      
t_RETURN      = r'return'     
t_SELECT      = r'select'     
t_STRUCT      = r'struct'     
t_SWITCH      = r'switch'     
t_TYPE        = r'type'       
t_VAR         = r'var'        
t_CHAN        = r'chan'       
t_GO          = r'go'         
t_DEFAULT     = r'default'    
t_DEFER       = r'defer'      
t_IMPORT      = r'import'     
t_CONST       = r'const'      

# Numeros: Stefany Lavayen
def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

# Cadenas: Stefany Lavayen
def t_CADENA(t):
  r'\w+(_\dw)*'
  return t

# Comentario
def t_COMENTARIO(t):
  r'(\//.*|\/\*.*\*\/)'
  pass

# IDENTIFICADOR
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR') 
    return t


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