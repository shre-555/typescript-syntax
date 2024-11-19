import ply.yacc as yacc
from checker import tokens
import sys

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
                                | variable_initialization 
                                | variable_declaration COMMA variable_declaration
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
    '''array_declaration_statement : VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE PUNCTUATOR
                                    | VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
                                    | VARIABLE_DECLARATION_STATEMENT VARIABLE_NAME EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
                                    | VARIABLE_DECLARATION_STATEMENT_CONST VARIABLE_NAME TYPE_DECLARATOR VARIABLE_TYPE LSQUARE RSQUARE EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
                                    | VARIABLE_DECLARATION_STATEMENT_CONST VARIABLE_NAME EQUAL LSQUARE array_elements RSQUARE PUNCTUATOR
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
var name:string = "mary";
var name:string;
var name = "mary";
var name;
let a,b:number;
let a:string="HI",b:number=9,c=10,d:string="bye",e:number,f:string="abc";
let a:number, b:string="hi";
let a="hi",b:number=10;
let a="hi",b=10;
const a: number = 6, b = 2;
let a="hi",b:number;
'''

# data = sys.stdin.read()  # Read until EOF (Ctrl+Z and then enter)

# Parse the input
result = parser.parse(data)


if no_of_syntax_errors:
    print(no_of_syntax_errors, "syntax errors found")
else:
    print("No syntax errors found")
