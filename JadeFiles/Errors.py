def p_error(p):
    print(f"Syntax Error at line {p.lineno}: {p.value}\n"
          f"                        {'^' * len(p.value)}")