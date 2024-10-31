import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'SELECTION_STATEMENTS',
   'VARIABLE_DECLARATION_STATEMENT', #var,let,const
   'VARIABLE_NAME',
   'VARIABLE_TYPE',
   'EQUAL',
   'TYPE_DECLARATOR',
   'PUNCTUATOR',
   'LSQUARE',
   'RSQUARE',
   'KEYWORDS'
)

# Regular expression rules for simple tokens
t_EQUAL   = r'='
t_LSQUARE  = r'\['
t_RSQUARE  = r'\]'
t_TYPE_DECLARATOR= r':'
t_PUNCTUATOR= r'(;|")'
t_SELECTION_STATEMENTS = r'(else if | if | else)'
t_VARIABLE_DECLARATION_STATEMENT=r'(let | const)'
t_VARIABLE_NAME= r'(([A-Za-z_]+[0-9]*)+)'
t_VARIABLE_TYPE=r'(number|string|boolean|object)'
# t_KEYWORDS= 

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
if let 5
const b: string = "abc";
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
