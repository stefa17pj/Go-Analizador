import ply.yacc as yacc 
from analizadorLexico import tokens
from analizadorLexico import reserved 

textResult = ""

#STEFANY LAVAYEN
def p_instrucciones(p):
    '''instrucciones : asignacion
                     | expresion 
                     | condiciones
                     | sentenciaIf
                     | sentenciaFor
                     | print
                     | mapa
                     | puntero
                     | lectura
                     | array
                     | switch
                     | arrayAsig
                     | funcion'''

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
                  | VARIABLE MASIGUAL acumular
                  | VARIABLE MENOSIGUAL expresion
                  | derefer IGUAL valor
       booleano   : condicion
                  | TRUE 
                  | FALSE
       valor      : booleano
                  | expresion
                  | CADENA
                  | VARIABLE
                  | mapa
                  | refer
        acumular  : expresion
                  | CADENA
                  | VARIABLE'''

#JAHIR VELIZ
def p_sentenciaIf(p):
    '''sentenciaIf : IF comparaciones LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT else
                   | IF comparaciones LLAVELEFT instrucciones LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones LLAVERIGHT else
                   | IF comparaciones LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | IF comparaciones LLAVELEFT RETURN VARIABLE LLAVERIGHT else
       else :        ELSE LLAVELEFT instrucciones LLAVERIGHT
                   | ELSE LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT
                   | ELSE LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | ELSE sentenciaIf'''

#JAHIR VELIZ
def p_mapa(p):
    ''' mapa : MAP CORCHLEFT typeData CORCHRIGHT typeData LLAVELEFT par LLAVERIGHT
             | MAP CORCHLEFT typeData CORCHRIGHT typeData LLAVELEFT LLAVERIGHT
        par  : dato DOSPUNTOS dato mas
             | dato DOSPUNTOS dato
        mas  : mas COMA dato DOSPUNTOS dato
             | COMA dato DOSPUNTOS dato
        dato : VARIABLE
             | expresion
             | CADENA
             | TRUE
             | FALSE'''

#JAHIR VELIZ
# refer: "&" se utiliza para obtener la dirección de una variable
# derefer: "*" dereferir un puntero significa obtener el valor de la dirección almacenada en el puntero.
def p_puntero(p):
    '''puntero : PRODUCTO typeData
       refer   : AMPERSAND VARIABLE
       derefer : PRODUCTO VARIABLE'''

#STEFANY LAVAYEN: Sentencia For: ' for inicio; condicion; incremento { codigo } ' como esta en el avance 0
def p_sentenciaFor(p):
    'sentenciaFor : FOR inicio PUNTOCOMA condiciones PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHT'

#STEFANY LAVAYEN: inicio del For
def p_iniciofor(p):
    'inicio : VARIABLE DECLARADOR ENTERO'

#STEFANY LAVAYEN: incremento del For
def p_incrementa(p):
    'incrementa : VARIABLE INCREMENTO'

#STEFANY LAVAYEN: Tipos de Datos
def p_typeData(p):
    '''typeData : BOOL
                | INT
                | FLOAT
                | STRING'''

#STEFANY LAVAYEN: Declaracion de Arrays
def p_array(p):
    'array : VARIABLE DECLARADOR CORCHLEFT ENTERO CORCHRIGHT typeData LLAVELEFT contArray LLAVERIGHT'

#STEFANY LAAVYEN: Asignacion de Arrays
def p_arrayAsig(p):
    'arrayAsig : VAR VARIABLE CORCHLEFT ENTERO CORCHRIGHT typeData'

#STEFANY: Print
def p_print(p):
    'print : IMPRIMIR PARLEFT contPrint PARRIGHT'

def p_contenidoPrint(p):
    '''contPrint : contenido masCont
                 | contenido
       masCont   : masCont COMA contenido
                 | COMA contenido
       contenido : expresion
                 | CADENA
                 | VARIABLE
                 | '''

#STEFANY LAVAYEN : lectura de datos Scan
def p_lectura(p):
    'lectura : SCAN PARLEFT contScan PARRIGHT'

def p_contenidoScan(p):
    'contScan : AMPERSAND VARIABLE'

# STEFANY LAVAYEN START{
def p_contenidoArray(p):
    'contArray : contArray COMA numericos'

def p_suma_expresion(p):
    '''expresion : expresion SUMA term'''

def p_resta_expresion(p):
    'expresion : expresion RESTA term'

def p_producto_expresion(p):
    'expresion : expresion PRODUCTO term'

def p_div_expresion(p):
    'expresion : expresion DIVISION term'

def p_modulo_expresion(p):
    'expresion : expresion MODULO term'

def p_expression_term(p):
    'expresion : term'
    #p[0] = p[1]

def p_expression_term2(p):
    'contArray : term'
    #p[0] = p[1]

def p_term_factor(p):
    'term : numericos'
    #p[0] = p[1]

def p_factor_num(p):
    'factor : numericos'

def p_factor_var(p):
    'factor : VARIABLE'

def p_numericos(p):
    'numericos : ENTERO'

def p_numericos_float(p):
    'numericos : FLOTANTE'

def p_factor_exp(p):
    'numericos : PARLEFT expresion PARRIGHT'

#} END STEFANY LAVAYEN

# start - Bryan Puchaicela

def p_comparacion(p):
    'comparacion : condiciones'

def p_comparaciones_negado(p):
    'comparacion : NEGACION PARLEFT condiciones PARRIGHT'

def p_comparaciones_paren(p):
    'comparacion : PARLEFT condiciones PARRIGHT'

# Estructura de functions
def p_funcion(p):
    '''funcion : funcion_sin_parametro
               | funcion_parametro
               | funcion_sin_parametro_return'''

def p_funcion_sin_parameters(p):
    '''funcion_sin_parametro : FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT RETURN LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones RETURN LLAVERIGHT'''

def p_funcion_sin_parameters_return(p):
    'funcion_sin_parametro_return : FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones RETURN VARIABLE LLAVERIGHT'

def p_funcion_parameters(p):
    '''funcion_parametro : FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT instrucciones LLAVERIGHT
                         | FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT instrucciones RETURN LLAVERIGHT
                         | FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT RETURN LLAVERIGHT'''

def p_parametros(p):
    '''parametros : VARIABLE
                  | VARIABLE COMA parametros
                  | typeData VARIABLE
                  | typeData VARIABLE COMA parametros'''

# Estructura de switch / case
def p_switch(p):
    'switch : SWITCH VARIABLE LLAVELEFT bloque_switch LLAVERIGHT'

def p_bloque_switch(p):
    '''bloque_switch : CASE caso DOSPUNTOS instrucciones BREAK
                     | CASE caso DOSPUNTOS instrucciones CONTINUE
                     | CASE caso DOSPUNTOS instrucciones BREAK bloque_switch
                     | switch_default
       caso          : VARIABLE
                     | CADENA
                     | ENTERO'''

def p_switch_default(p):
    'switch_default : DEFAULT DOSPUNTOS instrucciones '

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

def p_factor_bool(p):
    'factor : BOOL'
# end - Bryan Puchaicela 

# Error rule for syntax errors
def p_error(p):
    global textResult
    print(p)
    textResult += "Syntax error in input!\n" + str(p)

# Build the parser
parser = yacc.yacc()

def analysisSyntax(data):
    global textResult
    textResult = ""
    result = parser.parse(data)
    textResult += str (result)+"\n"
    return textResult
