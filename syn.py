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
    '''variable_declaration_statement : VARIABLE_DECLARATION_STATEMENT variable_declaration PUNCTUATOR
                                        | VARIABLE_DECLARATION_STATEMENT_CONST variable_initialization PUNCTUATOR
                                        '''
    pass

def p_variable_declaration(p):
    '''variable_declaration : VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE
                                | VARIABLE_NAME
                                | variable_declaration COMMA variable_declaration 
                                | variable_initialization
                                '''
    pass

def p_variable_initialization(p):
    '''variable_initialization : VARIABLE_NAME EQUAL expression 
                                | VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE EQUAL expression
                                | variable_initialization COMMA variable_initialization '''
    pass



# Selection statement (if, if-else)
def p_selection_statement(p):
    '''selection_statement : SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY
                            |  SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY SELECTION_STATEMENTS_ELSE LCURLY RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY SELECTION_STATEMENTS_ELSE LCURLY RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY elseif_statement
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY elseif_statement
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY elseif_statement SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY elseif_statement SELECTION_STATEMENTS_ELSE LCURLY RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY statement_list RCURLY elseif_statement SELECTION_STATEMENTS_ELSE LCURLY RCURLY
                           | SELECTION_STATEMENTS_IF LPAREN expression RPAREN LCURLY RCURLY elseif_statement SELECTION_STATEMENTS_ELSE LCURLY statement_list RCURLY
                           '''
    pass

def p_elseif_statement(p):
    '''elseif_statement : SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY statement_list RCURLY
                        | SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY RCURLY
                        | SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY statement_list RCURLY elseif_statement
                        | SELECTION_STATEMENTS_ELSEIF LPAREN expression RPAREN LCURLY RCURLY elseif_statement
    '''

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
    '''array_declaration_statement : VARIABLE_DECLARATION_STATEMENT array_declaration PUNCTUATOR
                                    | VARIABLE_DECLARATION_STATEMENT_CONST array_initialization PUNCTUATOR
                            '''
    pass

def p_array_declaration(p):
    '''array_declaration : VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE PUNCTUATOR
                            | array_declaration COMMA array_declaration
                            | array_initialization
    '''
    pass

def p_array_initialization(p):
    '''array_initialization : VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
                            | VARIABLE_NAME EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
                            | array_initialization COMMA array_initialization 
    '''
    pass


def p_array_elements(p):
    '''array_elements : NUMBER COMMA array_elements
                    | STRING COMMA array_elements
                    | NUMBER
                    | STRING
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    global no_of_syntax_errors
    if p:
        print(f"Syntax error at token '{p.type}' (value: '{p.value}') on line {p.lineno}")
        no_of_syntax_errors += 1
    else:
        pass

# Build the parser
parser = yacc.yacc()

data = input()  

# Parse the input
result = parser.parse(data)


if no_of_syntax_errors:
    print(no_of_syntax_errors, "syntax errors found")
else:
    print("No syntax errors found")
