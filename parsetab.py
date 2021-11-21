
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BARRAINVERSA BOOL BREAK CADENA CASE CHAN COMA COMENTARIO CONST CONTINUE CORCHLEFT CORCHRIGHT DECLARADOR DEFAULT DEFER DIFERENTE DIVISION DOSPUNTOS ELSE ENTERO ESIGUAL ESPACIO FALLTHROUGH FALSE FLOAT FLOTANTE FOR FUNC GO GOTO IF IGUAL IMPORT IMPRIMIR INCREMENTO INT INTERFACE LLAVELEFT LLAVERIGHT MAP MASIGUAL MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOSIGUAL MODULO NEGACION OR PACKAGE PARLEFT PARRIGHT PRODUCTO PUNTOCOMA RANGE RESTA RETURN SELECT STRING STRUCT SUMA SWITCH TRUE TYPE VAR VARIABLEinstrucciones : expresion \n                    | condicion\n                    | sentenciaFor\n                    | iniciosentenciaFor : FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHTinicio : VARIABLE DECLARADOR ENTEROcondicion : termc comparador termcincrementa : VARIABLE INCREMENTOcomparador : MAYORQUE \n                    | MENORQUE\n                    | ESIGUAL \n                    | MAYORIGUAL \n                    | MENORIGUALexpresion : expresion SUMA numericosexpresion : expresion RESTA numericosexpresion : expresion PRODUCTO numericosexpresion : expresion DIVISION numericosexpresion : expresion MODULO numericosexpresion : termterm : numericostermc : VARIABLEtermc : numericosfactor : VARIABLEnumericos : ENTEROnumericos : FLOTANTE'
    
_lr_action_items = {'FOR':([0,41,],[9,9,]),'VARIABLE':([0,9,18,19,20,21,22,23,35,38,41,],[10,25,33,-9,-10,-11,-12,-13,33,40,10,]),'ENTERO':([0,13,14,15,16,17,18,19,20,21,22,23,26,35,41,],[11,11,11,11,11,11,11,-9,-10,-11,-12,-13,36,11,11,]),'FLOTANTE':([0,13,14,15,16,17,18,19,20,21,22,23,35,41,],[12,12,12,12,12,12,12,-9,-10,-11,-12,-13,12,12,]),'$end':([1,2,3,4,5,6,7,11,12,27,28,29,30,31,32,33,34,36,44,],[0,-1,-2,-3,-4,-20,-19,-24,-25,-14,-15,-16,-17,-18,-7,-21,-22,-6,-5,]),'LLAVERIGHT':([2,3,4,5,6,7,11,12,27,28,29,30,31,32,33,34,36,43,44,],[-1,-2,-3,-4,-20,-19,-24,-25,-14,-15,-16,-17,-18,-7,-21,-22,-6,44,-5,]),'SUMA':([2,6,7,11,12,27,28,29,30,31,],[13,-20,-19,-24,-25,-14,-15,-16,-17,-18,]),'RESTA':([2,6,7,11,12,27,28,29,30,31,],[14,-20,-19,-24,-25,-14,-15,-16,-17,-18,]),'PRODUCTO':([2,6,7,11,12,27,28,29,30,31,],[15,-20,-19,-24,-25,-14,-15,-16,-17,-18,]),'DIVISION':([2,6,7,11,12,27,28,29,30,31,],[16,-20,-19,-24,-25,-14,-15,-16,-17,-18,]),'MODULO':([2,6,7,11,12,27,28,29,30,31,],[17,-20,-19,-24,-25,-14,-15,-16,-17,-18,]),'MAYORQUE':([6,8,10,11,12,33,34,],[-22,19,-21,-24,-25,-21,-22,]),'MENORQUE':([6,8,10,11,12,33,34,],[-22,20,-21,-24,-25,-21,-22,]),'ESIGUAL':([6,8,10,11,12,33,34,],[-22,21,-21,-24,-25,-21,-22,]),'MAYORIGUAL':([6,8,10,11,12,33,34,],[-22,22,-21,-24,-25,-21,-22,]),'MENORIGUAL':([6,8,10,11,12,33,34,],[-22,23,-21,-24,-25,-21,-22,]),'DECLARADOR':([10,25,],[26,26,]),'PUNTOCOMA':([11,12,24,32,33,34,36,37,],[-24,-25,35,-7,-21,-22,-6,38,]),'LLAVELEFT':([39,42,],[41,-8,]),'INCREMENTO':([40,],[42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,41,],[1,43,]),'expresion':([0,41,],[2,2,]),'condicion':([0,35,41,],[3,37,3,]),'sentenciaFor':([0,41,],[4,4,]),'inicio':([0,9,41,],[5,24,5,]),'numericos':([0,13,14,15,16,17,18,35,41,],[6,27,28,29,30,31,34,34,6,]),'term':([0,41,],[7,7,]),'termc':([0,18,35,41,],[8,32,8,8,]),'comparador':([8,],[18,]),'incrementa':([38,],[39,]),}

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
  ('sentenciaFor -> FOR inicio PUNTOCOMA condicion PUNTOCOMA incrementa LLAVELEFT instrucciones LLAVERIGHT','sentenciaFor',9,'p_sentenciaFor','analizadorSintactico.py',11),
  ('inicio -> VARIABLE DECLARADOR ENTERO','inicio',3,'p_iniciofor','analizadorSintactico.py',14),
  ('condicion -> termc comparador termc','condicion',3,'p_condicion','analizadorSintactico.py',17),
  ('incrementa -> VARIABLE INCREMENTO','incrementa',2,'p_incrementa','analizadorSintactico.py',20),
  ('comparador -> MAYORQUE','comparador',1,'p_comparador','analizadorSintactico.py',23),
  ('comparador -> MENORQUE','comparador',1,'p_comparador','analizadorSintactico.py',24),
  ('comparador -> ESIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',25),
  ('comparador -> MAYORIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',26),
  ('comparador -> MENORIGUAL','comparador',1,'p_comparador','analizadorSintactico.py',27),
  ('expresion -> expresion SUMA numericos','expresion',3,'p_suma_expresion','analizadorSintactico.py',30),
  ('expresion -> expresion RESTA numericos','expresion',3,'p_resta_expresion','analizadorSintactico.py',33),
  ('expresion -> expresion PRODUCTO numericos','expresion',3,'p_producto_expresion','analizadorSintactico.py',36),
  ('expresion -> expresion DIVISION numericos','expresion',3,'p_div_expresion','analizadorSintactico.py',39),
  ('expresion -> expresion MODULO numericos','expresion',3,'p_modulo_expresion','analizadorSintactico.py',42),
  ('expresion -> term','expresion',1,'p_expression_term','analizadorSintactico.py',45),
  ('term -> numericos','term',1,'p_term_factor','analizadorSintactico.py',49),
  ('termc -> VARIABLE','termc',1,'p_term_condicion','analizadorSintactico.py',53),
  ('termc -> numericos','termc',1,'p_term_condicionm','analizadorSintactico.py',56),
  ('factor -> VARIABLE','factor',1,'p_factor_var','analizadorSintactico.py',59),
  ('numericos -> ENTERO','numericos',1,'p_factor_num','analizadorSintactico.py',62),
  ('numericos -> FLOTANTE','numericos',1,'p_factor_float','analizadorSintactico.py',64),
]
