import ply.lex as lex
import ply.yacc as yacc
from JadeFiles.vars import p_expression_fstring, p_expression_equal, p_expression_set, p_expression_id
from JadeFiles.minimum import p_expression_int, p_expression_float, p_expression_string

# List of token names. This is always required
tokens = [
    'COMMENT',
    'FUNCNAME',
    'LBRACKET',
    'RBRACKET',
    'INT',
    'FLOAT',
    'STRING',
    'SET',
    'EQUAL',
    'ID',
    'VALUE',
    'SAY',
    'FSTRING',
    'TASK',
    "ADD",
    "MINUS",
    "DIVIDE",
    "MULTIPLY"
]

# Dictionary of reserved words
reserved = {
    'Set': 'SET',
    'Say': "SAY",
    'Task': "TASK"
}

# Regular expression rules for simple tokens
t_ignore_newline = r'\n'
t_ignore = ' \t'
t_COMMENT = r"~~.*"
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*\"'
t_EQUAL = r'='
t_ADD = "\+"
t_MINUS = "\-"
t_DIVIDE = "/"
t_MULTIPLY = "\*"
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_FSTRING = r"\$\".*?\""
t_FUNCNAME = r'[a-zA-Z_][a-zA-Z0-9_]*\((.*)\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'


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


def t_TASK(t):
    r"""Task"""
    t.type = reserved.get(t.value, "Task")
    return t


lexer = lex.lex()


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += 1
    return

# def p_expression_task(p):
#    """expression : TASK FUNCNAME LBRACKET expression RBRACKET"""
#    name = p[2].replace(p[2][p[2].find("("):p[2].find(")") + 1], "")
#    args = p[2].replace(f"{name}(", "").replace(")", "").replace(" ", "").split(",")
#    code = p[4]
#    funcs[name] = code
#    print(name, args, code)
#    return


def p_expression_operation(p):
    """expression : expression ADD expression
                  | expression MULTIPLY expression
                  | expression MINUS expression
                  | expression DIVIDE expression"""
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]



def p_expression_comment(p):
    """expression : COMMENT"""
    return


def p_expression_say(p):
    """expression : SAY expression"""
    print(p[2])
    return


parser = yacc.yacc()

with open("jade.jd", "r") as Jade:
    for line in Jade:
        parser.parse(line)
