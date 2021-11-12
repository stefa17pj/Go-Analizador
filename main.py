import ply.lex as lex 

#Analizador Lexico GO

# List of token names.   This is always required

#Stefany Lavayen: palabras reservadas 
keywords = {
  'break' : 'BREAK',
  'else' : 'ELSE',
  'for' : 'FOR',
  'if' : 'IF',
  'case' : 'CASE',
  'func' : 'FUNC',
  'continue' : 'CONTINUE',
  'fallthrough' : 'FALLTHROUGH',
  'goto' : 'GOTO',
  'interface' : 'INTERFACE',
  'map' : 'MAP',
  'package' : 'PACKAGE',
  'range' : 'RANGE',
  'return' : 'RETURN',
  'select' : 'SELECT',
  'struct' : 'STRUCT',
  'switch' : 'SWITCH',
  'type' : 'TYPE',
  'var' : 'VAR',
  'chan' : 'CHAN', 
  'go' : 'GO',
  'default': 'DEFAULT',
  'defer' : 'DEFER',
  'import' : 'IMPORT',
  'const' : 'CONST'
}

tokens = (
  'NUMBER',
  'PARLEFT',
  'PARRIGHT',
  'MAYORQUE',
  'MENORQUE',
  'IGUAL'
) + tuple(keywords.values())

# Regular expression rules for simple tokens
t_PARLEFT = r'\('
t_PARRIGHT = r'\)'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL = r'='

t_IF=r'(if)'


#Algorithm
def t_error(t):
  print("No se reconoce '%s'" % t.value[0])
  t.lexer.skip(1)

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