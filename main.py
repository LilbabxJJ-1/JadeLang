import ply.lex as lex
import ply.yacc as yacc
from JadeFiles.vars import p_expression_fstring, p_expression_equal, p_expression_set, p_expression_id
from JadeFiles.minimum import p_expression_int, p_expression_float, p_expression_string

# List of token names. This is always required
tokens = [
    'COMMENT',
    'INT',
    'FLOAT',
    'STRING',
    'SET',
    'EQUAL',
    'ID',
    'VALUE',
    'SAY',
    'FSTRING'
]

# Dictionary of reserved words
reserved = {
    'Set': 'SET',
    'Say': "SAY"
}

# Regular expression rules for simple tokens
t_ignore_newline = r'\n'
t_ignore = ' \t'
t_COMMENT = r"~~.*"
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*\"'
t_EQUAL = r'='
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_FSTRING = r"\$\".*?\""


# Error handling rule
def t_error(t):
    print(f"Error at: {t.value}\n"
          f"          {'^' * len(t.value)}")
    exit()
    t.lexer.skip(1)


# Check if the token is a reserved word
def t_SET(t):
    r"""\bSet\b"""
    t.type = reserved.get(t.value, 'Set')
    return t


def t_SAY(t):
    r"""\bSay\b"""
    t.type = reserved.get(t.value, 'Say')
    return t


lexer = lex.lex()


def t_newline(t):
    r"""\n"""
    t.lexer.lineno += 1


def p_expression_comment(p):
    """expression : COMMENT"""
    return


def p_expression_say(p):
    """expression : SAY expression"""
    print(p[2])
    return


parser = yacc.yacc()

with open("Jade.JD", "r") as Jade:
    for s in Jade:
        if s == "\n":
            continue
        result = parser.parse(s)
