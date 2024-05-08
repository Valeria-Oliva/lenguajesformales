import ply.lex as lex

tokens = (
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'COLON', 'COMMA',
    'STRING', 'NUMBER',
    'TRUE', 'FALSE', 'NULL'
)

# Reglas de expresiones regulares para tokens simples.
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COLON     = r':'
t_COMMA     = r','
t_ignore = ' \t\n\r'


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')  # Eliminar las comillas dobles
    return t

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

# Regla para manejar errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
