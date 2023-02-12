def p_expression_int(p):
    'expression : INT'
    p[0] = int(p[1])


def p_expression_float(p):
    'expression : FLOAT'
    p[0] = float(p[1])


def p_expression_string(p):
    'expression : STRING'
    p[0] = str(p[1][1:-1])