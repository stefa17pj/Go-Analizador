import ply.yacc as yacc 
from analizadorLexico import tokens

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