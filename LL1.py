import pandas as pd
from lexer import tokens


counter = 0
dot = ''
# print(syntax_table)

def print_list(node_list):
    for nod in node_list:
        print(nod.symbol.symbol, nod.symbol.id, end=" - " )
        print()

def print_stack(stack):
    print("STACK -> ", end='')
    for element in stack:
        #print(element.symbol + ':' + str(element.is_terminal), end=' ')
        print(element.symbol, end=' ')
    print()

def print_input(input):
    print("INPUT -> ", end='')
    for element in input:        
        print(element[0], end=' ')
    print()

def find_in_tree(node_list, id):
    for nod in node_list:
        if nod.symbol.id == id:
            return nod

def print_tree(node, node_list, info = False):
    global dot
    dot = "digraph G { \n"    

    for nod in node_list:
        if nod.symbol.is_terminal: 
            if nod.symbol.symbol == 'e':
                dot += str(nod.symbol.id) + ' [ style=filled fillcolor=yellow  label=< <b>' + nod.symbol.symbol + '</b> > ]; \n'            
            else:             
                lexeme = nod.lexeme
                lexeme = "&#38;" if lexeme == '&' else nod.lexeme # el & genera errores en dot, por eso lo pasamos en codigo HTML
                dot += str(nod.symbol.id) + ' [ style=filled fillcolor=yellow  label=< <b>' + nod.symbol.symbol + '</b> <br/>' + str(lexeme) + ' <br/> line '+str(nod.line) + ' > ]; \n'            
        else:
            # esta info es para el analizador semantico
            #########################################################
            if info and ( nod.symbol.symbol == 'E' or nod.symbol.symbol == 'T' or nod.symbol.symbol == "E'" or nod.symbol.symbol == 'TERM' ):
                lexeme = nod.lexeme
                lexeme = "&#38;" if lexeme == '&' else nod.lexeme # el & genera errores en dot, por eso lo pasamos en codigo HTML
                
                if nod.visited == True:                
                    dot += str(nod.symbol.id) + ' [ style=filled fillcolor=green label=< <b>' + nod.symbol.symbol + '</b> <br/> ' + str(nod.type) + ' <br/> line ' + str(nod.line) + ' > ]; \n'            
                else:
                    dot += str(nod.symbol.id) + ' [ label=< <b>' + nod.symbol.symbol + '</b> <br/>' + str(nod.type) + ' > ]; \n'            
            #########################################################
            
            else:
                dot += str(nod.symbol.id) + ' [ label=" ' + nod.symbol.symbol + ' " ]; \n'            
        
    
    print_tree_recursive(node)        
    dot += "}"

    return dot

def print_tree_recursive(node):
    global dot
    tmp = []
    for child in node.children:
        dot += str(node.symbol.id) + ' -> ' + str(child.symbol.id) + '; \n'
        tmp.append(str(child.symbol.id))
        print_tree_recursive(child)

    if len(node.children) > 0:
        dot += "{ \n"
        dot += "    rank = same; \n"
        dot += "    edge[ style=invis]; \n"
        dot += " -> ".join(tmp) + "; \n"
        dot += "    rankdir = LR; \n"
        dot += "} \n" 

def update_stack(root, node_list, syntax_table, stack, current_token):
    production = syntax_table.loc[stack[0].symbol, current_token]

    if (str(production) == "nan"):
        return False

    productions = production.split(" ")
    productions.pop(0) # eliminamos el lado izquierdo de la produccion
    productions.pop(0) # eliminamos la flecha

    # eliminamos el primer elemento de la pila, para el remplazo
    father = stack.pop(0) 
    node_father = find_in_tree (node_list, father.id)

    if productions[0] == "''": # vacio
        new_symbol = node_stack( 'e', True )
        nod_tree    = node_parser( new_symbol, None, [], node_father )
        node_father.children.insert(0, nod_tree )
        node_list.append(nod_tree)
        return True

    # print(father.id, father.symbol, father.is_terminal)
    for prod in reversed(productions):
        # insertamos en la pila
        new_symbol = node_stack( prod, False if prod.isupper() else True )
        stack.insert(0, new_symbol)

        node_tree = node_parser(new_symbol, None, [], node_father)
        node_father.children.insert(0, node_tree)
        node_list.append(node_tree)

    return True

class node_stack:
    def __init__(self, symbol, terminal):
        global counter
        self.id = counter
        self.symbol = symbol
        #self.lexeme = lexeme
        #self.noline = noline
        self.is_terminal = terminal
        counter += 1

class node_parser:
    def __init__(self, symbol, lexeme = None,  children = [], father = None, line = None):  
        self.symbol = symbol
        self.lexeme = lexeme
        self.line = line
        self.children = children
        self.father = father

        self.type = None # es para guardar el tipo de dato, lo usaremos en el analizador semantico
        self.visited = False # para saber si el nodo fue visitado, lo usaremos en el analizador semantico

syntax_table = pd.read_csv("grammar_v4.csv", index_col=0)

# insert the first elements in STACK
symbol_1 = node_stack('$', True)
symbol_2 = node_stack('MAIN', False)
stack = []
stack.insert(0, symbol_1)
stack.insert(0, symbol_2)

# insert the first element in syntax tree
root = node_parser(symbol_2)
node_list = []  # almacena todos los nodos, es pra facilitar algunod algoritmos
node_list.append(root)


def parser(tokens):
    result = False
    while True:

        if stack[0].symbol == tokens[0][0] == '$':  # if terminla are $
            result = True
            break

        if stack[0].is_terminal:            
            if stack[0].symbol == tokens[0][0]:
                #print("Terminales iguales :", tokens[0][0])
                # antes de eliminar, asigno el lexeme y no linea
                nod = find_in_tree(node_list, stack[0].id)
                nod.lexeme = tokens[0][1]
                nod.line = tokens[0][2]

                stack.pop(0)
                tokens.pop(0)
            else:
                #print("Terminales diferentes")
                result = False 
                print("Syntax error 0001 at line ", tokens[0][2]) 
                break  
        else:            
            if not update_stack(root, node_list, syntax_table, stack, tokens[0][0]):
                result = False 
                print("Syntax error 0002 at line ", tokens[0][2]) 
                break 

    return root, node_list




    