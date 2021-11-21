import ply.yacc as yacc 
from analizadorLexico import tokens

def p_instrucciones(p):
    '''instrucciones :  condicion
                       | sentenciaFor
                       | inicio'''

def p_sentenciaFor(p):
    'sentenciaFor : FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHT'

def p_iniciofor(p):
    'inicio : VARIABLE DECLARADOR ENTERO'

def p_condicion(p):
    'condicion : factor comparador factor'

def p_incrementa(p):
    'incrementa : VARIABLE INCREMENTO'

def p_comparador(p):
    '''comparador : MAYORQUE 
                    | MENORQUE
                    | ESIGUAL 
                    | MAYORIGUAL 
                    | MENORIGUAL'''

def p_factor_var(p):
    'factor : VARIABLE'

def p_facto_num(p):
    'factor : ENTERO'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('Python > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)