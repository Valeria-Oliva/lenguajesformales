import ply.yacc as yacc
from lexCopy import tokens


def p_JSON(p):
    'JSON : brace_inicio BOOKS brace_final'
    p[0] = p[1]

def p_books(p):
    'BOOKS : texto dos_puntos bracket_inicio BOOK_LIST bracket_final'
    p[0] = {p[2]: p[5]}  

def p_book_lis(p):
    'BOOK_LIST : brace_inicio BOOK_ENTRIES brace_final'
    p[0] = p[2]

def p_book_entries(p):
    '''BOOK_ENTRIES : BOOK_ENTRY
                    | BOOK_ENTRY coma BOOK_ENTRIES'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {**p[1], **p[3]}

def p_book_entry(p):
    '''BOOK_ENTRY : TITLE
                  | AUTHOR
                  | GENRE
                  | PUBLICATION
                  | ISBN
                  | CHARACTERS
                  | REVIEWS'''
    p[0] = p[1]

def p_title(p):
    'TITLE : texto dos_puntos texto coma'
    p[0] = {p[1]: p[3]}

def p_author(p):
    'AUTHOR : texto dos_puntos brace_inicio AUTHOR_DETAILS brace_final coma'
    p[0] = {p[1]: p[4]}
    
def p_txt(p):
    'STRING : texto dos_puntos texto'
    p[0] = p[1] + p[2] + p[3]
    
def p_int(p):
    'INT : texto dos_puntos numero'
    p[0] = p[1] + p[2] + p[3]

def p_author_details(p):
    'AUTHOR_DETAILS : STRING coma INT coma STRING'
    p[0] = p[1] + p[3] + p[5]
    
def p_genre(p):
    'GENRE : texto dos_puntos bracket_inicio texto coma texto bracket_final coma'
    p[0] = {p[1]: [p[4], p[6]]}

def p_publication(p):
    'PUBLICATION : texto dos_puntos brace_inicio STRING coma INT coma STRING brace_final coma'
    p[0] = {p[1]: p[4] + p[6] + p[8]}

def p_isbn(p):
    'ISBN : texto dos_puntos brace_inicio STRING coma STRING brace_final coma'
    p[0] = {p[1]: p[4] + p[6]}

def p_characters(p):
    'CHARACTERS : texto dos_puntos bracket_inicio CHARACTER_ENTRIES bracket_final coma'
    p[0] = {p[1]: p[4]}

def p_character_entries(p):
    'CHARACTER_ENTRIES : CHARACTER_ENTRY coma CHARACTER_ENTRY'
    p[0] = [p[1], p[3]]

def p_character_entry(p):
    'CHARACTER_ENTRY : brace_inicio STRING coma STRING brace_final'
    p[0] = p[2] + p[4]

def p_reviews(p):
    'REVIEWS : texto dos_puntos bracket_inicio REVIEW_ENTRIES bracket_final'
    p[0] = {p[1]: p[4]}

def p_review_entries(p):
    'REVIEW_ENTRIES : REVIEW_ENTRY coma REVIEW_ENTRY'
    p[0] = [p[1], p[3]]

def p_review_entry(p):
    'REVIEW_ENTRY : brace_inicio INT coma STRING brace_final'
    p[0] = p[2] + p[4]

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Example usage for debugging
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
    },
    {
      "title": "The Lord of the Rings",
      "author": {
        "name": "J.R.R. Tolkien",
        "birth_year": 1892,
        "nationality": "English"
      },
      "genre": ["Fantasy", "Adventure"],
      "publication": {
        "publisher": "George Allen & Unwin",
        "year": 1954,
        "language": "English"
      },
      "isbn": {
        "10": "0-395-19395-8",
        "13": "978-0-395-19395-7"
      },
      "characters": [
        {
          "name": "Frodo Baggins",
          "description": "The main protagonist. A hobbit tasked with destroying the One Ring."
        },
        {
          "name": "Gandalf",
          "description": "A wizard who guides the fellowship on their quest."
        }
      ],
      "reviews": [
        {
          "rating": 50,
          "comment": "A masterpiece of fantasy literature, with rich world-building and memorable characters."
        },
        {
          "rating": 40,
          "comment": "Enjoyed the epic journey, but found some parts slow-paced."
        }
      ]
    }
  ]
}
  
'''
result = parser.parse(test_json)
print(result)
