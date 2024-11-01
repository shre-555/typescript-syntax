import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'SELECTION_STATEMENTS',
    'VARIABLE_DECLARATION_STATEMENT', # var, let, const
    'VARIABLE_TYPE',
    'EQUAL',
    'TYPE_DECLARATOR',
    'PUNCTUATOR',
    'LSQUARE',
    'RSQUARE',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'KEYWORDS',
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

t_SELECTION_STATEMENTS = r'\b(if|else)\b'
t_VARIABLE_TYPE = r'\b(number|string|boolean|object)\b'
t_VARIABLE_DECLARATION_STATEMENT = r'\b(let|const)\b'
t_VARIABLE_NAME = r'(?!(if|else|let|const)\b)[a-zA-Z_][a-zA-Z0-9_]*'
t_RELATIONAL_OPERATOR = r'(===|==|>=|<=|!=|!|>|<|&&|\|\|)'
t_PUNCTUATOR = r';'
t_EQUAL = r'='
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_TYPE_DECLARATOR = r':'
t_KEYWORDS = r'\b(return|function|for|while|do|break|continue)\b'

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

# Test it out
data = '''
if (5!='5' || 4)
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
