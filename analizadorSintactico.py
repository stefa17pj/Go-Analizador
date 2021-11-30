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
                     | funcion
                     | PACKAGE VARIABLE IMPORT CADENA funcion''' # <- inicio valido de un programa en go

def p_masInstrucciones(p):
    '''masInstrucciones : masInstrucciones instrucciones
                        | masInstrucciones
                        | '''

# JAHIR VELIZ
def p_asignacion(p):
    '''asignacion : VAR VARIABLE BOOL IGUAL booleano
                  | VAR VARIABLE INT IGUAL expresion
                  | VAR VARIABLE FLOAT IGUAL expresion
                  | VAR VARIABLE STRING IGUAL CADENA
                  | VAR VARIABLE puntero IGUAL refer
                  | VAR VARIABLE puntero
                  | slices
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
    '''sentenciaIf : IF comparaciones LLAVELEFT instrucciones masInstrucciones RETURN VARIABLE LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones RETURN VARIABLE LLAVERIGHT else
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones LLAVERIGHT else
                   | IF comparaciones LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | IF comparaciones LLAVELEFT RETURN VARIABLE LLAVERIGHT else
        else :       ELSE LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                   | ELSE LLAVELEFT instrucciones masInstrucciones RETURN VARIABLE LLAVERIGHT
                   | ELSE LLAVELEFT RETURN VARIABLE LLAVERIGHT
                   | ELSE sentenciaIf'''

#JAHIR VELIZ
def p_mapa(p):
    ''' mapa : MAP CORCHLEFT STRING CORCHRIGHT typeData LLAVELEFT LLAVERIGHT
             | MAP CORCHLEFT STRING CORCHRIGHT contMapa'''

# la clave del mapa siempre será una cadena, pero su valor puede ser entero, float, cadena o booleano
def p_contenidoMapa(p):
    '''contMapa  : INT LLAVELEFT parEntero LLAVERIGHT
                 | STRING LLAVELEFT parCadena LLAVERIGHT 
                 | FLOAT LLAVELEFT parFlotante LLAVERIGHT
                 | BOOL LLAVELEFT parBoolean LLAVERIGHT'''

def p_mapaEntero(p):
    '''parEntero  : CADENA DOSPUNTOS datoEntero masEntero
                  | CADENA DOSPUNTOS datoEntero
       masEntero  : masEntero COMA CADENA DOSPUNTOS datoEntero
                  | COMA CADENA DOSPUNTOS datoEntero
       datoEntero : VARIABLE
                  | expresion'''

def p_mapaCadena(p):
    '''parCadena  : CADENA DOSPUNTOS datoCadena masCadena
                  | CADENA DOSPUNTOS datoCadena
       masCadena  : masCadena COMA CADENA DOSPUNTOS datoCadena
                  | COMA CADENA DOSPUNTOS datoCadena
       datoCadena : VARIABLE
                  | CADENA'''

def p_mapaFlotante(p):
    '''parFlotante  : CADENA DOSPUNTOS datoFlotante masFlotante
                    | CADENA DOSPUNTOS datoFlotante
       masFlotante  : masFlotante COMA CADENA DOSPUNTOS datoFlotante
                    | COMA CADENA DOSPUNTOS datoFlotante
       datoFlotante : VARIABLE
                    | expresion'''

def p_mapaBooleano(p):
    '''parBoolean  : CADENA DOSPUNTOS datoBoolean masBoolean
                   | CADENA DOSPUNTOS datoBoolean
       masBoolean  : masBoolean COMA CADENA DOSPUNTOS datoBoolean
                   | COMA CADENA DOSPUNTOS datoBoolean
       datoBoolean : condicion
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
    ''' sentenciaFor : FOR inicio PUNTOCOMA condiciones PUNTOCOMA incrementa LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
        inicio       : VARIABLE DECLARADOR ENTERO
        incrementa   : VARIABLE INCREMENTO'''

#STEFANY LAVAYEN: Tipos de Datos
def p_typeData(p):
    '''typeData : BOOL
                | INT
                | FLOAT
                | STRING'''

#STEFANY LAVAYEN: Regla semantica en ARRAYS: Validacion de los elementos del arreglo de acuerdo al tipo de dato definido
# colors := [4]string{"blue", "red", "pink", "yellow"} ---->  Elementos del arreglo solo debe ser de tipo String
# edad := [4]int{1,2,3,4} ---->  Elementos del arreglo solo debe ser de tipo int
# edad := [4]int{"blue", "red", "pink", "yellow"} ---->  X (error de semantica)
def p_array(p):
    'array : VARIABLE DECLARADOR CORCHLEFT ENTERO CORCHRIGHT contArray'

def p_contenidoArray(p):
    '''contArray : INT LLAVELEFT contArrayEnteros LLAVERIGHT
                 | STRING LLAVELEFT contArrayCadenas LLAVERIGHT 
                 | FLOAT LLAVELEFT contArrayFloat LLAVERIGHT'''

def p_ArrayEnteros(p):
    '''contArrayEnteros : ENTERO COMA ENTERO
                        | contArrayEnteros COMA ENTERO'''

def p_ArrayCadenas(p):
    '''contArrayCadenas : CADENA COMA CADENA
                        | contArrayCadenas COMA CADENA'''

def p_ArrayFlotante(p):
    '''contArrayFloat : FLOTANTE COMA FLOTANTE
                      | contArrayFloat COMA FLOTANTE'''


def p_methodGeneral(p):
    'method : methodArray'

#STEFANY LAVAYEN:  metodos de estructuras de datos ARRAY
def p_methodArray(p):
    ''' methodArray : namemetodoArr PARLEFT VARIABLE PARRIGHT
        namemetodoArr   :   LEN
                        |   CAP '''

#STEFANY LAVAYEN: Print -> Regla semantica: Solo pueden imprimir contenido tipo STRING, variables, o resultados de un metodos
def p_print(p):
    'print : IMPRIMIR PARLEFT contPrint PARRIGHT'

def p_contenidoPrint(p):
    '''contPrint : contenido masCont
                 | contenido
       masCont   : masCont COMA contenido
                 | COMA contenido
       contenido : CADENA
                 | VARIABLE
                 | method
                 | '''

#STEFANY LAVAYEN : lectura de datos Scan
def p_lectura(p):
    'lectura : SCAN PARLEFT contScan PARRIGHT'

def p_contenidoScan(p):
    'contScan : AMPERSAND VARIABLE'

# STEFANY LAVAYEN: Regla semantica - Los datos numericos (int, float) son los unicos que pueden sumar/restar/multiplicar/dividirse entre si 
def p_aritmetica_expresion(p):
    '''expresion : expresion operadorArit term'''

def p_operador_aritmetico(p):
    '''operadorArit : SUMA
                    | RESTA
                    | PRODUCTO
                    | DIVISION
                    | MODULO
    '''
def p_expression_term(p):
    'expresion : term'
    #p[0] = p[1]

def p_term_factor(p):
    'term : numericos'
    #p[0] = p[1]

def p_factor_num(p):
    'factor : numericos'

def p_factor_var(p):
    'factor : VARIABLE'

def p_numericos(p):
    '''numericos : ENTERO
                | FLOTANTE '''

def p_factor_exp(p):
    'numericos : PARLEFT expresion PARRIGHT'

#} END STEFANY LAVAYEN

# start - Bryan Puchaicela

def p_estructura_slice(p):
    '''slices : declaracion_slices
              | declaracion_slices LLAVELEFT contArrayEnteros LLAVERIGHT
              | declaracion_slices LLAVELEFT contArrayCadenas LLAVERIGHT
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT typeData COMA ENTERO PARRIGHT
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT typeData COMA ENTERO COMA ENTERO PARRIGHT
       metodos_slices : MAKE'''

def p_declaracion_slice(p):
    '''declaracion_slices : VAR VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT typeData
                          | VAR VARIABLE IGUAL CORCHLEFT CORCHRIGHT typeData
                          | VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT typeData
                          | VARIABLE IGUAL CORCHLEFT CORCHRIGHT typeData
                          | VARIABLE DECLARADOR CORCHLEFT CORCHRIGHT typeData'''

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
    '''funcion_sin_parametro : FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT RETURN LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones masInstrucciones RETURN LLAVERIGHT'''

def p_funcion_sin_parameters_return(p):
    'funcion_sin_parametro_return : FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones masInstrucciones RETURN VARIABLE LLAVERIGHT'

def p_funcion_parameters(p):
    '''funcion_parametro : FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                         | FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT instrucciones masInstrucciones RETURN LLAVERIGHT
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
    '''bloque_switch : CASE caso_switch DOSPUNTOS instrucciones masInstrucciones BREAK
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones CONTINUE
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones BREAK bloque_switch
                     | switch_default'''

def p_caso_switch(p):
    '''caso_switch : VARIABLE
                   | CADENA
                   | ENTERO '''

def p_switch_default(p):
    '''switch_default : DEFAULT DOSPUNTOS instrucciones masInstrucciones BREAK
                      | DEFAULT DOSPUNTOS instrucciones masInstrucciones CONTINUE'''

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
    textResult += str(result)+"\n"
    return textResult
