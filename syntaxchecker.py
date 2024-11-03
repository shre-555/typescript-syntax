import ply.yacc as yacc
from checker import tokens

no_of_syntax_errors=0

# Start symbol
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Basic statements
def p_statement(p):
    '''statement : selection_statement
                 | variable_declaration_statement
                 | expression_statement
                 | array_declaration_statement
                 '''
    pass

# Variable declaration (e.g., const x: string = "hello";
def p_variable_declaration_statement(p):
    '''variable_declaration_statement : VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE PUNCTUATOR'''
    pass

# Selection statement (if, if-else)
def p_selection_statement(p):
    '''selection_statement : SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           '''
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
                  | LPAREN expression RPAREN'''
    pass

# Array declaration
def p_array_declaration_statement(p):
    '''array_declaration_statement : VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE PUNCTUATOR
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' (value: '{p.value}') on line {p.lineno}")
        global no_of_syntax_errors
        no_of_syntax_errors+=1
    else:
        pass
        # "Syntax error at EOF"

# Build the parser
parser = yacc.yacc()

# Test input
data = '''
a:number;
'''

# Parse the input
result = parser.parse(data)


if no_of_syntax_errors:
    print(no_of_syntax_errors, "syntax errors found")
else:
    print("No syntax errors found")
