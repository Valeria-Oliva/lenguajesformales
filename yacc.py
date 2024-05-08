import ply.yacc as yacc
from lex import tokens

def p_start(p):
    'JSON : OBJETOS'
    p[0] = p[1]

def p_objeto_libro(p):
    'OBJETOS : brace_inicio BOOKS brace_final'
    p[0] = p[1] + p[2] + p[3]
    
def p_books(p):
    'BOOKS : texto dos_puntos bracket_inicial brace_inicio INFO brace_final bracket_final '
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
    
def p_info(p):
    '''INFO : LIBRO
            | LIBRO coma INFO'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def p_libro(p):
    'LIBRO : TITLE AUTHOR GENRE PUBLICATION ISBN CHARACTERS REVIEWS'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_renglontxt(p):
    'RENGLON : texto dos_puntos texto'
    p[0] = p[1] + p[2] + p[3]
    
def p_renglonint(p):
    'INT: texto dos_puntos numero'
    p[0] = p[1] + p[2] + p[3]
    
def p_objetotipo2(p):
    'OBJ02 : brace_inicio RENGLON coma RENGLON brace_final'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] 

def p_objetotipo3(p):
    'OBJ03 : brace_inicio INT coma RENGLON brace_final'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    
def p_title(p):
    'TITLE : RENGLON coma'
    p[0] = p[1] + p[2]
    
def p_author(p):
    'AUTHOR : texto dos_puntos brace_inicio RENGLON coma INT coma RENGLON brace_final coma'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10]
    
def p_genre(p):
    'GENRE : texto dos_puntos bracket_inicio texto coma texto bracket_final coma'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]

def p_publication(p):
    'PUBLICATION : texto dos_puntos brace_inicio RENGLON coma INT coma RENGLON brace_final coma'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10]

def p_isbn(p):
    'ISBN : texto dos_puntos OBJ02 coma'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_characters(p):
    'CHARACTERS : texto dos_puntos bracket_inicio OBJ02 coma OBJ02 bracket_final coma'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]

def p_reviews(p):
    'REVIEWS : texto dos_puntos bracket_inicio OBJ03 coma OBJ03 bracket_final'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]  

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


'''
with open('html_prueba1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    result = parser.parse(html_content)
    print("RESULTADO: ", result)
'''

test_json = '''
{
  "books": [     
      {
      "title": "The Catcher in the Rye",
      "author": {
            "name": "J.D. Salinger",
            "birth_year": 1919,
            "nationality": "American"
      },
      "genre": ["Fiction", "Coming-of-age"],
      "publication": {
            "publisher": "Little, Brown and Company",
            "year": 1951,
            "language": "English"
      },
      "isbn": {
            "10": "0-316-76948-7",
            "13": "978-0-316-76948-0"
      },
      "characters": [
        {
          "name": "Holden Caulfield",
          "description": "The protagonist and narrator. A sixteen-year-old boy."
        },
        {
          "name": "Phoebe Caulfield",
          "description": "Holden's ten-year-old sister. Intelligent and understanding."
        }
      ],
      "reviews": [
        {
          "rating": 45,
          "comment": "A classic coming-of-age story with a memorable protagonist."
        },
        {
          "rating": 30,
          "comment": "Didn't connect with the protagonist's voice, but appreciated the themes."
        }
      ]
    }
  ]
}
  
'''
result = parser.parse(test_json)
print(result)