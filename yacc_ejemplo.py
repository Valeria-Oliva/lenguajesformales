import ply.yacc as yacc
from lex_ejemplo import tokens  # Asegúrate de que esto coincida con tu archivo de tokens del lexer

def p_json(p):
    '''json : object
            | array'''
    p[0] = p[1]

def p_object(p):
    'object : LBRACE RBRACE'
    p[0] = {}

def p_object_nonempty(p):
    'object : LBRACE members RBRACE'
    p[0] = p[2]

def p_members(p):
    'members : pair'
    p[0] = dict([p[1]])

def p_members_multiple(p):
    'members : pair COMMA members'
    p[0] = dict([p[1]] + list(p[3].items()))

def p_pair(p):
    'pair : STRING COLON value'
    p[0] = (p[1], p[3])

def p_array(p):
    'array : LBRACKET RBRACKET'
    p[0] = []

def p_array_nonempty(p):
    'array : LBRACKET elements RBRACKET'
    p[0] = p[2]

def p_elements(p):
    'elements : value'
    p[0] = [p[1]]

def p_elements_multiple(p):
    'elements : value COMMA elements'
    p[0] = [p[1]] + p[3]

def p_value_string(p):
    'value : STRING'
    p[0] = p[1]

def p_value_number(p):
    'value : NUMBER'
    p[0] = p[1]

def p_value_object(p):
    'value : object'
    p[0] = p[1]

def p_value_array(p):
    'value : array'
    p[0] = p[1]

def p_value_true(p):
    'value : TRUE'
    p[0] = True

def p_value_false(p):
    'value : FALSE'
    p[0] = False

def p_value_null(p):
    'value : NULL'
    p[0] = None

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Para probar el parser, necesitarás tener un JSON como entrada.
# Por ejemplo, puedes probarlo directamente con una cadena:
test_json = '''
{
  "name": "John",
  "age": 30,
  "is_student": false,
  "courses": ["Math", "Science"],
  "profile": null
}
'''
result = parser.parse(test_json)
print(result)
