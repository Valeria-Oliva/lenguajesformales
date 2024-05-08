import ply.lex as lex
import json

tokens = (
    'brace_inicio',
    'brace_final',
    'bracket_inicio',
    'bracket_final',
    'dos_puntos',
    'coma',
    'texto',
    'numero' 
)

t_brace_inicio = r'\{'
t_brace_final = r'\}'
t_bracket_inicio = r'\['
t_bracket_final = r'\]'
t_dos_puntos = r':'
t_coma = r','
t_texto = r'"[^"]*"'
t_numero = r'[0-9]+'

t_ignore = ' \t\n\r'

def t_error(t):
    print('Carácter ilegal', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


'''
with open('unlibro.json', 'r', encoding='utf-8') as file:
    data = file.read()
    lexer.input(data)
    for tok in lexer:
        print(tok)
'''
