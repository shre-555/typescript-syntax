import ply.yacc as yacc
from checker import tokens

# Start symbol
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Basic statements
def p_statement(p):
    '''statement : selection_statement
                 | variable_declaration_statement
                 | expression_statement'''
    pass

# Variable declaration (e.g., const x: string = "hello";
def p_variable_declaration_statement(p):
    '''variable_declaration_statement : VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE EQUAL expression PUNCTUATOR'''
    pass

# Selection statement (if, if-else)
def p_selection_statement(p):
    '''selection_statement : SELECTION_STATEMENTS LPAREN expression RPAREN LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS LCURLY statement_list RCURLY'''
    pass

# Expressions
def p_expression_statement(p):
    '''expression_statement : expression PUNCTUATOR'''
    pass

# Expressions with numbers, variable names, relational operators
def p_expression(p):
    '''expression : NUMBER
                  | VARIABLE_NAME
                  | STRING
                  | expression RELATIONAL_OPERATOR expression
                  | expression EQUAL expression
                  | LPAREN expression RPAREN'''
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' (value: '{p.value}') on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test input
data = '''
let a = 3;
if (5 != "5" || 4)
'''

# Parse the input
result = parser.parse(data)
print("sucecc")
