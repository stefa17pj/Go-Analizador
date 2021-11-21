
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BARRAINVERSA BOOL BREAK CADENA CASE CHAN COMA COMENTARIO CONST CONTINUE CORCHLEFT CORCHRIGHT DECLARADOR DEFAULT DEFER DIFERENTE DIVISION DOSPUNTOS ELSE ENTERO ESIGUAL ESPACIO FALLTHROUGH FALSE FLOAT FLOTANTE FOR FUNC GO GOTO IF IGUAL IMPORT IMPRIMIR INCREMENTO INT INTERFACE LLAVELEFT LLAVERIGHT MAP MASIGUAL MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOSIGUAL MODULO NEGACION OR PACKAGE PARLEFT PARRIGHT PRODUCTO PUNTOCOMA RANGE RESTA RETURN SELECT STRING STRUCT SUMA SWITCH TRUE TYPE VAR VARIABLEinstrucciones : expresion \n                    | condicion\n                    | sentenciaFor\n                    | inicio\n                    | array\n                    | arrayAsigsentenciaFor : FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHTinicio : VARIABLE DECLARADOR ENTEROcondicion : termc comparador termcincrementa : VARIABLE INCREMENTOtypeData : BOOL \n                | INT\n                | FLOAT\n                | STRING array : VARIABLE DECLARADOR CORCHLEFT ENTERO CORCHRIGHT typeData LLAVELEFT contArray LLAVERIGHTarrayAsig : VAR VARIABLE CORCHLEFT ENTERO CORCHRIGHT typeDatacontArray : contArray COMA numericoscomparador : MAYORQUE \n                    | MENORQUE\n                    | ESIGUAL \n                    | MAYORIGUAL \n                    | MENORIGUALexpresion : expresion SUMA numericosexpresion : expresion RESTA numericosexpresion : expresion PRODUCTO numericosexpresion : expresion DIVISION numericosexpresion : expresion MODULO numericosexpresion : termcontArray : termterm : numericostermc : VARIABLEtermc : numericosfactor : VARIABLEnumericos : ENTEROnumericos : FLOTANTE'
    
_lr_action_items = {'FOR':([0,58,],[11,11,]),'VARIABLE':([0,11,14,21,22,23,24,25,26,39,47,58,],[12,28,30,37,-18,-19,-20,-21,-22,37,51,12,]),'VAR':([0,58,],[14,14,]),'ENTERO':([0,16,17,18,19,20,21,22,23,24,25,26,29,39,40,42,43,58,60,67,],[13,13,13,13,13,13,13,-18,-19,-20,-21,-22,41,13,41,45,46,13,13,13,]),'FLOTANTE':([0,16,17,18,19,20,21,22,23,24,25,26,39,58,60,67,],[15,15,15,15,15,15,15,-18,-19,-20,-21,-22,15,15,15,15,]),'$end':([1,2,3,4,5,6,7,8,9,13,15,31,32,33,34,35,36,37,38,41,53,54,55,56,57,65,66,],[0,-1,-2,-3,-4,-5,-6,-30,-28,-34,-35,-23,-24,-25,-26,-27,-9,-31,-32,-8,-11,-12,-13,-14,-16,-7,-15,]),'LLAVERIGHT':([2,3,4,5,6,7,8,9,13,15,31,32,33,34,35,36,37,38,41,53,54,55,56,57,61,62,63,64,65,66,68,],[-1,-2,-3,-4,-5,-6,-30,-28,-34,-35,-23,-24,-25,-26,-27,-9,-31,-32,-8,-11,-12,-13,-14,-16,65,66,-30,-29,-7,-15,-17,]),'SUMA':([2,8,9,13,15,31,32,33,34,35,],[16,-30,-28,-34,-35,-23,-24,-25,-26,-27,]),'RESTA':([2,8,9,13,15,31,32,33,34,35,],[17,-30,-28,-34,-35,-23,-24,-25,-26,-27,]),'PRODUCTO':([2,8,9,13,15,31,32,33,34,35,],[18,-30,-28,-34,-35,-23,-24,-25,-26,-27,]),'DIVISION':([2,8,9,13,15,31,32,33,34,35,],[19,-30,-28,-34,-35,-23,-24,-25,-26,-27,]),'MODULO':([2,8,9,13,15,31,32,33,34,35,],[20,-30,-28,-34,-35,-23,-24,-25,-26,-27,]),'MAYORQUE':([8,10,12,13,15,37,38,],[-32,22,-31,-34,-35,-31,-32,]),'MENORQUE':([8,10,12,13,15,37,38,],[-32,23,-31,-34,-35,-31,-32,]),'ESIGUAL':([8,10,12,13,15,37,38,],[-32,24,-31,-34,-35,-31,-32,]),'MAYORIGUAL':([8,10,12,13,15,37,38,],[-32,25,-31,-34,-35,-31,-32,]),'MENORIGUAL':([8,10,12,13,15,37,38,],[-32,26,-31,-34,-35,-31,-32,]),'DECLARADOR':([12,28,],[29,40,]),'PUNTOCOMA':([13,15,27,36,37,38,41,44,],[-34,-35,39,-9,-31,-32,-8,47,]),'COMA':([13,15,62,63,64,68,],[-34,-35,67,-30,-29,-17,]),'CORCHLEFT':([29,30,],[42,43,]),'CORCHRIGHT':([45,46,],[48,49,]),'BOOL':([48,49,],[53,53,]),'INT':([48,49,],[54,54,]),'FLOAT':([48,49,],[55,55,]),'STRING':([48,49,],[56,56,]),'LLAVELEFT':([50,52,53,54,55,56,59,],[58,60,-11,-12,-13,-14,-10,]),'INCREMENTO':([51,],[59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,58,],[1,61,]),'expresion':([0,58,],[2,2,]),'condicion':([0,39,58,],[3,44,3,]),'sentenciaFor':([0,58,],[4,4,]),'inicio':([0,11,58,],[5,27,5,]),'array':([0,58,],[6,6,]),'arrayAsig':([0,58,],[7,7,]),'numericos':([0,16,17,18,19,20,21,39,58,60,67,],[8,31,32,33,34,35,38,38,8,63,68,]),'term':([0,58,60,],[9,9,64,]),'termc':([0,21,39,58,],[10,36,10,10,]),'comparador':([10,],[21,]),'incrementa':([47,],[50,]),'typeData':([48,49,],[52,57,]),'contArray':([60,],[62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> expresion','instrucciones',1,'p_instrucciones','analizadorSintactico.py',5),
  ('instrucciones -> condicion','instrucciones',1,'p_instrucciones','analizadorSintactico.py',6),
  ('instrucciones -> sentenciaFor','instrucciones',1,'p_instrucciones','analizadorSintactico.py',7),
  ('instrucciones -> inicio','instrucciones',1,'p_instrucciones','analizadorSintactico.py',8),
  ('instrucciones -> array','instrucciones',1,'p_instrucciones','analizadorSintactico.py',9),
  ('instrucciones -> arrayAsig','instrucciones',1,'p_instrucciones','analizadorSintactico.py',10),
  ('sentenciaFor -> FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHT','sentenciaFor',9,'p_sentenciaFor','analizadorSintactico.py',13),
  ('inicio -> VARIABLE DECLARADOR ENTERO','inicio',3,'p_iniciofor','analizadorSintactico.py',16),
  ('condicion -> termc comparador termc','condicion',3,'p_condicion','analizadorSintactico.py',19),
  ('incrementa -> VARIABLE INCREMENTO','incrementa',2,'p_incrementa','analizadorSintactico.py',22),
  ('typeData -> BOOL','typeData',1,'p_tipodato','analizadorSintactico.py',25),
  ('typeData -> INT','typeData',1,'p_tipodato','analizadorSintactico.py',26),
  ('typeData -> FLOAT','typeData',1,'p_tipodato','analizadorSintactico.py',27),
  ('typeData -> STRING','typeData',1,'p_tipodato','analizadorSintactico.py',28),
  ('array -> VARIABLE DECLARADOR CORCHLEFT ENTERO CORCHRIGHT typeData LLAVELEFT contArray LLAVERIGHT','array',9,'p_array','analizadorSintactico.py',31),
  ('arrayAsig -> VAR VARIABLE CORCHLEFT ENTERO CORCHRIGHT typeData','arrayAsig',6,'p_arrayAsig','analizadorSintactico.py',34),
  ('contArray -> contArray COMA numericos','contArray',3,'p_contenidoArray','analizadorSintactico.py',37),
  ('comparador -> MAYORQUE','comparador',1,'p_comparador','analizadorSintactico.py',40),
  ('comparador -> MENORQUE','comparador',1,'p_comparador','analizadorSintactico.py',41),
  ('comparador -> ESIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',42),
  ('comparador -> MAYORIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',43),
  ('comparador -> MENORIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',44),
  ('expresion -> expresion SUMA numericos','expresion',3,'p_suma_expresion','analizadorSintactico.py',47),
  ('expresion -> expresion RESTA numericos','expresion',3,'p_resta_expresion','analizadorSintactico.py',50),
  ('expresion -> expresion PRODUCTO numericos','expresion',3,'p_producto_expresion','analizadorSintactico.py',53),
  ('expresion -> expresion DIVISION numericos','expresion',3,'p_div_expresion','analizadorSintactico.py',56),
  ('expresion -> expresion MODULO numericos','expresion',3,'p_modulo_expresion','analizadorSintactico.py',59),
  ('expresion -> term','expresion',1,'p_expression_term','analizadorSintactico.py',62),
  ('contArray -> term','contArray',1,'p_expression_term2','analizadorSintactico.py',66),
  ('term -> numericos','term',1,'p_term_factor','analizadorSintactico.py',70),
  ('termc -> VARIABLE','termc',1,'p_term_condicion','analizadorSintactico.py',74),
  ('termc -> numericos','termc',1,'p_term_condicionm','analizadorSintactico.py',77),
  ('factor -> VARIABLE','factor',1,'p_factor_var','analizadorSintactico.py',80),
  ('numericos -> ENTERO','numericos',1,'p_factor_num','analizadorSintactico.py',83),
  ('numericos -> FLOTANTE','numericos',1,'p_factor_float','analizadorSintactico.py',85),
]
