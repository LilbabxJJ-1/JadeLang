variables = {}


def p_expression_id(p):
    """expression : ID"""
    try:
        p[0] = variables[f"{p[1]}"]
    except KeyError:
        print(f"Variable '{p[1]}' Not Defined: {p[1]}\n"
              f"                            {'^' * len(p[1])}")
        exit()

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


def p_expression_fstring(p):
    """expression : FSTRING"""
    try:
     var_names = p[1].replace("'", "").replace('"', "").replace("$", "")
     for i in range(var_names.count("[")):
        inx = var_names.find("[")
        closest = var_names.find("]", inx)
        orig = var_names[inx:closest + 1]
        var = orig.removeprefix("[").removesuffix("]")
        var_names = var_names.replace(orig, str(variables[var]))
    except KeyError:
        print(f'Variable "{var}" Not Defined: {p[1]}\n'
              f"                              {'^' * len(p[1])}")
        exit()
    p[0] = var_names


def p_expression_equal(p):
    """expression : ID EQUAL expression
                  | ID EQUAL expression COMMENT"""
    variables[p[1]] = p[3]