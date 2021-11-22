import ply.yacc as yacc 
from analizadorLexico import tokens

def p_instrucciones(p):
    '''instrucciones : asignacion 
                     | expresion 
                     | condicion
                     | sentenciaIf
                     | sentenciaFor
                     | inicio
                     | array
                     | arrayAsig'''

# JAHIR VELIZ
def p_asignacion(p):
    '''asignacion : VAR VARIABLE BOOL IGUAL booleano
                  | VAR VARIABLE INT IGUAL expresion
                  | VAR VARIABLE FLOAT IGUAL expresion
                  | VAR VARIABLE STRING IGUAL CADENA
                  | VAR VARIABLE puntero IGUAL refer
                  | VAR VARIABLE puntero
                  | VARIABLE DECLARADOR valor
                  | VARIABLE IGUAL valor
                  | derefer IGUAL valor
       booleano   : condicion
                  | TRUE 
                  | FALSE
       valor      : booleano
                  | expresion
                  | CADENA
                  | VARIABLE
                  | mapa
                  | refer'''

#JAHIR VELIZ
def p_sentenciaIf(p):
    '''sentenciaIf : IF condicion LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT
                   | IF condicion LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT else
                   | IF condicion LLAVELEFT instrucciones LLAVERIGHT
                   | IF condicion LLAVELEFT instrucciones LLAVERIGHT else
                   | IF condicion LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | IF condicion LLAVELEFT RETURN VARIABLE LLAVERIGHT else
       else :        ELSE LLAVELEFT instrucciones LLAVERIGHT
                   | ELSE LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT
                   | ELSE LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | ELSE sentenciaIf'''

#JAHIR VELIZ
def p_mapa(p):
    ''' mapa : MAP CORCHLEFT tipo CORCHRIGHT tipo LLAVELEFT par LLAVERIGHT
             | MAP CORCHLEFT tipo CORCHRIGHT tipo LLAVELEFT LLAVERIGHT
        par  : dato DOSPUNTOS dato
             | dato DOSPUNTOS dato mas
        mas  : COMA par
             | COMA par mas
        tipo : BOOL
             | INT
             | FLOAT
             | STRING
        dato : VARIABLE
             | expresion
             | CADENA
             | TRUE
             | FALSE'''

#JAHIR VELIZ
# refer: "&" se utiliza para obtener la dirección de una variable
# derefer: "*" dereferir un puntero significa obtener el valor de la dirección almacenada en el puntero.
def p_puntero(p):
    '''puntero : PRODUCTO BOOL
               | PRODUCTO INT
               | PRODUCTO FLOAT
               | PRODUCTO STRING
       refer   : AMPERSAND VARIABLE
       derefer : PRODUCTO VARIABLE'''

def p_sentenciaFor(p):
    'sentenciaFor : FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHT'

def p_iniciofor(p):
    'inicio : VARIABLE DECLARADOR ENTERO'

def p_condicion(p):
    'condicion : termc comparador termc'

def p_incrementa(p):
    'incrementa : VARIABLE INCREMENTO'

def p_typeData(p):
    '''typeData : BOOL
            | INT
            | FLOAT
            | STRING'''

def p_array(p):
    'array : VARIABLE DECLARADOR CORCHLEFT ENTERO CORCHRIGHT typeData LLAVELEFT contArray LLAVERIGHT'

def p_arrayAsig(p):
    'arrayAsig : VAR VARIABLE CORCHLEFT ENTERO CORCHRIGHT typeData'

def p_contenidoArray(p):
    'contArray : contArray COMA numericos'

def p_comparador(p):
    '''comparador : MAYORQUE 
                    | MENORQUE
                    | ESIGUAL 
                    | MAYORIGUAL 
                    | MENORIGUAL'''

def p_suma_expresion(p):
    'expresion : expresion SUMA numericos'

def p_resta_expresion(p):
    'expresion : expresion RESTA numericos'

def p_producto_expresion(p):
    'expresion : expresion PRODUCTO numericos'

def p_div_expresion(p):
    'expresion : expresion DIVISION numericos'

def p_modulo_expresion(p):
    'expresion : expresion MODULO numericos'

def p_expression_term(p):
    'expresion : term'
    #p[0] = p[1]

def p_expression_term2(p):
    'contArray : term'
    #p[0] = p[1]

def p_term_factor(p):
    'term : numericos'
    #p[0] = p[1]

def p_term_condicion(p):
    'termc : VARIABLE' 

def p_term_condicionm(p):
    'termc : numericos'

def p_factor_var(p):
    'factor : VARIABLE'

def p_factor_num(p):
    'numericos : ENTERO'
def p_factor_float(p):
    'numericos : FLOTANTE'

def p_factor_bool(p):
    'factor : BOOL'

def p_comparacion(p):
    'comparacion : condiciones'

def p_comparaciones_negado(p):
    'comparacion : NEGACION PARLEFT condiciones PARRIGHT'

def p_comparaciones_paren(p):
    'comparacion : PARLEFT condiciones PARRIGHT'

# Operadores logicos
def p_mayorque_compare(p):
    'condiciones : factor MAYORQUE factor'

def p_menorque_compare(p):
    'condiciones : factor MENORQUE factor'

def p_distinto_compare(p):
    'condiciones : factor DIFERENTE factor'

def p_igualdad_compare(p):
    'condiciones : factor ESIGUAL factor'

def p_menoroigual_compare(p):
    'condiciones : factor MENORIGUAL factor'

def p_mayoroigual_compare(p):
    'condiciones : factor MAYORIGUAL factor'

def p_comparaciones(p):
    'comparaciones : comparacion'

def p_comparaciones_uno(p):
    'comparaciones : comparacion anado comparaciones'

def p_condicion_extra(p):
    'anado : condicion'

def p_condicion_and(p):
    'condicion : AND'

def p_condicion_or(p):
    'condicion : OR'
    
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