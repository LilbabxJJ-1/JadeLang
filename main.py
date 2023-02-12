import ply.lex as lex
import ply.yacc as yacc

# List of token names. This is always required
tokens = [
    'INT',
    'FLOAT',
    'STRING',
    'SET',
    'EQUAL',
    'ID',
    'VALUE',
    'SAY'

]

# Dictionary of reserved words
reserved = {
    'Set': 'SET',
    'Say': "SAY"
}

variables = {}

# Regular expression rules for simple tokens
t_ignore = ' \t\n'
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*\"'
t_EQUAL = r'='
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Check if the token is a reserved word
def t_SET(t):
    r'\bSet\b'
    t.type = reserved.get(t.value, 'Set')
    return t

def t_SAY(t):
    r'\bSay\b'
    t.type = reserved.get(t.value, 'Say')
    return t


# Build the lexer
lexer = lex.lex()


# Parsing rules
def p_expression_equal(p):
    """expression : ID EQUAL expression"""
    variables[p[1]] = p[3]

def p_expression_id(p):
    """expression : ID"""
    p[0] = variables[f"{p[1]}"]


def p_expression_int(p):
    'expression : INT'
    p[0] = int(p[1])


def p_expression_float(p):
    'expression : FLOAT'
    p[0] = float(p[1])


def p_expression_string(p):
    'expression : STRING'
    p[0] = str(p[1][1:-1])


def p_expression_say(p):
    '''expression : SAY expression'''
    print(p[2])
    return

def p_expression_set(p):
    'expression : SET ID EQUAL expression'
    var_name = p[2]
    var_value = p[4]
    try:
        var_value = int(var_value)
    except ValueError:
        try:
            var_value = float(var_value)
        except ValueError:
            pass
    variables[var_name] = var_value
    p[0] = (var_name, var_value)

def p_error(p):
    print(f"Syntax error in input at: {p.value}\n"
          f"                          {'^'*len(p.value)}")
    print(p)


parser = yacc.yacc()



with open("Main.JD", "r") as Jade:
    s = Jade.readlines()
    for i in s:
        result = parser.parse(i)