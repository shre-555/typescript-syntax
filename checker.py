import ply.lex as lex

# List of token names.   
tokens = (
    'NUMBER',
    'SELECTION_STATEMENTS_IF',
    'SELECTION_STATEMENTS_ELSE',
    'SELECTION_STATEMENTS_ELSEIF',
    'VARIABLE_DECLARATION_STATEMENT', # var, let
    'VARIABLE_DECLARATION_STATEMENT_CONST', #const
    'VARIABLE_TYPE',
    'EQUAL',
    'TYPE_DECLARATOR',
    'PUNCTUATOR',
    'COMMA',
    'LSQUARE',
    'RSQUARE',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'VARIABLE_NAME',
    'STRING',
    'RELATIONAL_OPERATOR'
)

# Regular expression rules for tokens
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"' #quotation marks should have starting and ending
    return t

#t_KEYWORDS = r'\b(await | break | case | catch | class | const | continue | debugger | default | delete | do | else | enum | export | extends | false | final | finally | for | function | if | implements | import | in | instanceof | interface | let | new | null | package | private | protected | public | return | super | switch | this | throw | true | try | typeof | var | void | while | with | yield)\b'
t_SELECTION_STATEMENTS_IF = r'\b(if)\b' #\b to avoid cases where it detectes if within another word like stiff
t_SELECTION_STATEMENTS_ELSE = r'\b(else)\b'
t_SELECTION_STATEMENTS_ELSEIF = r'\b(else\s+if)\b'
t_VARIABLE_TYPE = r'\b(number|string|boolean|object)\b'
t_VARIABLE_DECLARATION_STATEMENT = r'\b(let|var)\b'
t_VARIABLE_DECLARATION_STATEMENT_CONST = r'\b(const)\b'
t_VARIABLE_NAME = r'(?!(await | break | case | catch | class | const | continue | debugger | default | delete | do | else | enum | export | extends | false | final | finally | for | function | if | implements | import | in | instanceof | interface | let | new | null | package | private | protected | public | return | super | switch | this | throw | true | try | typeof | var | void | while | with | yield | number|string|boolean|object)\b)[a-zA-Z_$][a-zA-Z0-9_$]*'
t_RELATIONAL_OPERATOR = r'(===|==|>=|<=|!=|!|>|<|&&|\|\|)'
t_PUNCTUATOR = r';'
t_COMMA= r','
t_EQUAL = r'='
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_TYPE_DECLARATOR = r':'
t_ignore_COMMENT = r'//.*'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# #Test it out
# data = '''
# let abc : number = 5;
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
