import ply.lex as lex
import ply.yacc as yacc
from Nodo import Nodo
import sys
import networkx as nx
import matplotlib.pyplot as plt
sys.setrecursionlimit(1500)


diccionario_valores = {'p': 0, 'q': 0, 's': 0, 'r': 0, '0': 0, '1': 1}

lista_prev_arbol = []

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
    r'[p-zP-Z0-9]'
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
                  | VAR'''

    # print("Llamandolo:")
    lista_prev_arbol.clear()
    for pos in p:
        if pos is not None:
            lista_prev_arbol.append(pos)
            # print(pos, end=' ')
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


def p_parens(p):
    '''expression : LPR expression RPR'''
    p[0] = p[2]

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
# parser.parse("~q")
# parser.parse("((p=>q)^p)")
# parser.parse("(~(p^(q|r))|s)")
parser.parse("0=>(r|s)")

iteraciones = 0

numeroNodos = 1

listanodos = []


def crearNodo(lista):

    global iteraciones
    global numeroNodos
    nodo = None
    # print(lista)
    # izquierda, derecha, abajo, valor
    # ('~', ('^', 'p', ('|', 'q', 'r'))), '|', 's'
    # print(len(lista))
    if len(lista) == 3:
        if iteraciones > 0:
            nodo = Nodo(lista[1], lista[2], None, lista[0], numeroNodos)
            numeroNodos += 1
        else:
            nodo = Nodo(lista[0], lista[2], None, lista[1], numeroNodos)
            numeroNodos += 1
        # print("Nodo de tres: " + str(nodo))
        iteraciones += 1
        if type(nodo.derecha) == tuple:
            nodo.derecha = crearNodo(nodo.derecha)
        else:
            nodo.derecha = Nodo(None, None, None, nodo.derecha, numeroNodos)
            numeroNodos += 1
        if type(nodo.izquierda) == tuple:
            nodo.izquierda = crearNodo(nodo.izquierda)
        else:
            nodo.izquierda = Nodo(
                None, None, None, nodo.izquierda, numeroNodos)
            numeroNodos += 1

    elif len(lista) == 2:
        nodo = Nodo(None, None, lista[1], lista[0], numeroNodos)
        numeroNodos += 1
        if type(nodo.abajo) == tuple:
            nodo.abajo = crearNodo(nodo.abajo)
        else:
            nodo.abajo = Nodo(None, None, None, nodo.abajo, numeroNodos)
            numeroNodos += 1
    # print(nodo)
    return nodo

    # print()


nodoFinal = crearNodo(lista_prev_arbol)
# print(listanodos)

# print("Nodo Final: \n" + str(nodoFinal))

g = nx.DiGraph()
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(1, 4)
# g.add_edge(1, 5)
# g.add_edge(5, 6)
# g.add_edge(5, 7)
# g.add_edge(4, 8)
# g.add_edge(3, 8)

# Creando los nodos del grafo:


def crearGrafo(nodo_temp):
    global numeros
    if nodo_temp.izquierda != None:
        g.add_edge(nodo_temp.valor + " " + str(nodo_temp.numero),
                   crearGrafo(nodo_temp.izquierda))
    if nodo_temp.derecha != None:
        g.add_edge(nodo_temp.valor + " " + str(nodo_temp.numero),
                   crearGrafo(nodo_temp.derecha))

    if nodo_temp.abajo != None:
        g.add_edge(nodo_temp.valor + " " + str(nodo_temp.numero),
                   crearGrafo(nodo_temp.abajo))

    return nodo_temp.valor + " " + str(nodo_temp.numero)


crearGrafo(nodoFinal)


# drawing in circular layout
nx.draw_circular(g,  with_labels=True, node_size=2000)
plt.savefig("grafoPrueba.png")

# clearing the current plot
plt.clf()


# Esperado: 0
# parser.parse("(p<=>q)")
