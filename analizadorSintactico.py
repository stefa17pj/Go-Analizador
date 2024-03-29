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
                  | VAR VARIABLE INT IGUAL expresionInt
                  | VAR VARIABLE FLOAT IGUAL expresionFloat
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
    '''sentenciaIf : IF comparaciones LLAVELEFT instrucciones masInstrucciones RETURN valor LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones RETURN valor LLAVERIGHT else
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                   | IF comparaciones LLAVELEFT instrucciones masInstrucciones LLAVERIGHT else
                   | IF comparaciones LLAVELEFT RETURN valor LLAVERIGHT
                   | IF comparaciones LLAVELEFT RETURN valor LLAVERIGHT else
        else :       ELSE LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                   | ELSE LLAVELEFT instrucciones masInstrucciones RETURN valor LLAVERIGHT
                   | ELSE LLAVELEFT RETURN valor LLAVERIGHT
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
    '''parEntero  : CADENA DOSPUNTOS datoEntero COMA masEntero
                  | CADENA DOSPUNTOS datoEntero COMA
       masEntero  : masEntero CADENA DOSPUNTOS datoEntero COMA
                  | CADENA DOSPUNTOS datoEntero COMA
       datoEntero : VARIABLE
                  | expresionInt'''

def p_mapaCadena(p):
    '''parCadena  : CADENA DOSPUNTOS CADENA COMA masCadena
                  | CADENA DOSPUNTOS datoCadena COMA
       masCadena  : masCadena CADENA DOSPUNTOS datoCadena COMA
                  | CADENA DOSPUNTOS datoCadena COMA
       datoCadena : VARIABLE
                  | CADENA'''

def p_mapaFlotante(p):
    '''parFlotante  : CADENA DOSPUNTOS datoFlotante COMA masFlotante
                    | CADENA DOSPUNTOS datoFlotante COMA
       masFlotante  : masFlotante CADENA DOSPUNTOS datoFlotante COMA
                    | CADENA DOSPUNTOS datoFlotante COMA
       datoFlotante : VARIABLE
                    | expresionFloat'''

def p_mapaBooleano(p):
    '''parBoolean  : CADENA DOSPUNTOS datoBoolean COMA masBoolean
                   | CADENA DOSPUNTOS datoBoolean COMA
       masBoolean  : masBoolean CADENA DOSPUNTOS datoBoolean COMA
                   | CADENA DOSPUNTOS datoBoolean COMA
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

# STEFANY LAVAYEN: Regla semantica - En Go, solo podemos usar operadores en los mismos tipos de datos. No podemos sumar/restar/multiplicar/dividirseun int y un float64 
def p_aritmetica_expresion(p):
    '''expresion : expresionInt
                 | expresionFloat
    expresionInt : expresionInt operadorArit ENTERO
                 | ENTERO operadorArit ENTERO
                 | ENTERO
    expresionFloat : expresionFloat operadorArit FLOTANTE
                   | FLOTANTE operadorArit FLOTANTE
                   | FLOTANTE
    '''
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
    '''slices : declaracion_slices_enteros LLAVELEFT contArrayEnteros LLAVERIGHT
              | declaracion_slices_strings LLAVELEFT contArrayCadenas LLAVERIGHT
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO PARRIGHT
              | VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO PARRIGHT
              | VAR VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO PARRIGHT
              | VAR VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO PARRIGHT
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO COMA ENTERO PARRIGHT
              | VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO COMA ENTERO PARRIGHT
              | VAR VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO COMA ENTERO PARRIGHT
              | VAR VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT INT COMA ENTERO COMA ENTERO PARRIGHT
              | declaracion_slices_enteros
              | declaracion_slices_strings
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO PARRIGHT
              | VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO PARRIGHT
              | VAR VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO PARRIGHT
              | VAR VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO PARRIGHT
              | VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO COMA ENTERO PARRIGHT
              | VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO COMA ENTERO PARRIGHT
              | VAR VARIABLE DECLARADOR metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO COMA ENTERO PARRIGHT
              | VAR VARIABLE IGUAL metodos_slices PARLEFT CORCHLEFT CORCHRIGHT STRING COMA ENTERO COMA ENTERO PARRIGHT
       metodos_slices : MAKE'''

def p_declaracion_slice_enteros(p):
    '''declaracion_slices_enteros : VAR VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT INT
                                  | VAR VARIABLE CORCHLEFT ENTERO CORCHRIGHT INT
                                  | VAR VARIABLE CORCHLEFT CORCHRIGHT INT
                                  | VAR VARIABLE IGUAL CORCHLEFT CORCHRIGHT INT
                                  | VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT INT
                                  | VARIABLE DECLARADOR CORCHLEFT CORCHRIGHT INT'''

def p_declaracion_slices_strings(p):
    '''declaracion_slices_strings : VAR VARIABLE IGUAL CORCHLEFT CORCHRIGHT STRING
                                  | VAR VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT STRING
                                  | VARIABLE IGUAL CORCHLEFT ENTERO CORCHRIGHT STRING
                                  | VARIABLE DECLARADOR CORCHLEFT CORCHRIGHT STRING'''
def p_comparacion(p):
    'comparacion : condiciones'

def p_comparaciones_negado(p):
    'comparacion : NEGACION PARLEFT condiciones PARRIGHT'

def p_comparaciones_paren(p):
    'comparacion : PARLEFT condiciones PARRIGHT'

# Estructura de functions
def p_funcion(p):
    '''funcion : funcion_sin_parametro
               | funcion_parametro'''

def p_funcion_sin_parameters(p):
    '''funcion_sin_parametro : FUNC VARIABLE PARLEFT PARRIGHT LLAVELEFT instrucciones masInstrucciones LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT typeData LLAVELEFT RETURN valor LLAVERIGHT
                             | FUNC VARIABLE PARLEFT PARRIGHT typeData LLAVELEFT instrucciones masInstrucciones RETURN valor LLAVERIGHT'''

def p_funcion_parameters(p):
    '''funcion_parametro : FUNC VARIABLE PARLEFT parametros PARRIGHT typeData LLAVELEFT RETURN valor LLAVERIGHT
                         | FUNC VARIABLE PARLEFT parametros PARRIGHT typeData LLAVELEFT instrucciones masInstrucciones RETURN valor LLAVERIGHT
                         | FUNC VARIABLE PARLEFT parametros PARRIGHT LLAVELEFT instrucciones masInstrucciones LLAVERIGHT'''

def p_parametros(p):
    '''parametros : VARIABLE typeData
                  | VARIABLE typeData COMA parametros'''

# Estructura de switch / case
def p_switch(p):
    'switch : SWITCH VARIABLE LLAVELEFT bloque_switch LLAVERIGHT'

def p_bloque_switch(p):
    '''bloque_switch : CASE caso_switch DOSPUNTOS instrucciones masInstrucciones BREAK
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones
                     | CASE caso_switch DOSPUNTOS instrucciones BREAK
                     | CASE caso_switch DOSPUNTOS instrucciones
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones CONTINUE
                     | CASE caso_switch DOSPUNTOS instrucciones CONTINUE
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones BREAK bloque_switch
                     | CASE caso_switch DOSPUNTOS instrucciones masInstrucciones bloque_switch
                     | CASE caso_switch DOSPUNTOS instrucciones bloque_switch
                     | CASE caso_switch DOSPUNTOS instrucciones switch_default
                     | switch_default'''

def p_caso_switch(p):
    '''caso_switch : VARIABLE
                   | CADENA
                   | ENTERO '''

def p_switch_default(p):
    '''switch_default : DEFAULT DOSPUNTOS instrucciones masInstrucciones BREAK
                      | DEFAULT DOSPUNTOS instrucciones masInstrucciones
                      | DEFAULT DOSPUNTOS instrucciones BREAK
                      | DEFAULT DOSPUNTOS instrucciones masInstrucciones CONTINUE
                      | DEFAULT DOSPUNTOS instrucciones CONTINUE
                      | DEFAULT DOSPUNTOS instrucciones'''

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
