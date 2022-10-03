import ply.lex as lex
import ply.yacc as yacc


diccionario_valores = {'p': 0, 'q': 0}

# Definir las variables proporcionales y los operadores logicos como alfabetos:
tokens = (
    'VAR',
    'NEG',
    'AND',
    'OOR',
    'IMP',
    'IMD',
    'LPR',
    'RPR'
)

# Le necesitamos defnir a lex que son los tokens y como es que se ven:
t_NEG = r'\~'
t_AND = r'\^'
t_OOR = r'\|'
t_IMP = r'\=>'
t_IMD = r'\<=>'
t_LPR = r'\('
t_RPR = r'\)'

# Definimos un ignore por si se ubican espacios en blanco:

t_ignore = r' '

# Para valores de variables etc tenemos que crear una funcion para que lex lo reconozca:


def t_VAR(t):
    r'[p-zP-Z]'
    t.type = 'VAR'
    return t

# Para errores de sintaxis:


def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Construimos el lexer:
lexer = lex.lex()


# Definimos la precedencia de los operadores logicos:
precedence = (
    ('left', 'OOR'),
    ('left', 'AND'),
    ('right', 'NEG'),
    ('left', 'IMP'),
    ('left', 'IMD')
)

# Definimos las posibles gramaticas de nuestras expresiones en una funcion:


def p_calc(p):
    """
    calc : expression
    """
    print("Resultado: " + str(run(p[1])))


def p_expression(p):
    '''expression : expression AND expression
                  | expression OOR expression
                  | expression IMP expression
                  | expression IMD expression
                  | NEG expression
                  | LPR expression RPR
                  | VAR'''

    # print("Llamandolo:")
    # for pos in p:
    #     if pos is not None:
    #         print(pos, end=' ')
    # print()

    # p[0] = (p[2], p[1], p[3]) if len(p) > 2 else p[1]

    # print(len(p))
    if len(p) > 3:
        # print("Entro con 2")
        p[0] = (p[2], p[1], p[3])
    elif len(p) > 2:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

# Definimos la funcion para errores de sintaxis:


def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Definimos un posible empty:


def p_empty(p):
    """
    empty :
    """
    p[0] = None


# Creamos un parseador:
parser = yacc.yacc()

# Creamos una funcion para correr el parseador:


def run(p):
    # print("Corriendo:")
    # for pos in p:
    #     if pos is not None:
    #         print(pos, end=' ')
    # print()

    if type(p) == tuple:
        if p[0] == '^':
            return run(p[1]) and run(p[2])
        elif p[0] == '|':
            return run(p[1]) or run(p[2])
        elif p[0] == '=>':
            return not run(p[1]) or run(p[2])
        elif p[0] == '<=>':
            return run(p[1]) == run(p[2])
        elif p[0] == '~':
            return not run(p[1])
    else:
        return diccionario_valores[str(p[0])]


# # Probamos el lexer:
# lexer.input("p^q")
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)


# Probamos el parser:
# parser.parse("p<=>q")
parser.parse("~q")
# parser.parse("((p=>q)^p)")
