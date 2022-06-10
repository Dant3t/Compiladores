from itertools import count
from pickle import FALSE


current_function = None


class insert_table_node:
    def __init__(self, typ, table_name, columna = None):
        self.type = typ
        self.table_name = table_name
        self.columna = columna

class symbol_table_node:
    def __init__(self, identifier, typ, category, father = None, line = None):        
        self.identifier = identifier
        self.type = typ # tipo de dato
        self.category = category # funcion o variable
        self.line = line
        self.father = father # a q función pertenece

symbol_table = []

def add_symbol(identifier, typ, category, current_function):
    node_symbol = symbol_table_node(identifier, typ, category, current_function)
    symbol_table.append(node_symbol)

def find_symbol(identifier, father):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.father == father:
            return symbol


# def find_father(identifier, node):
#     for nod in node.children:
#         if nod.lexeme == identifier and nod.father.symbol.symbol == 'CREATE':
#             # for child in nod.father.children:
#             #     print(child.symbol.symbol)
#             # print(nod.father.children[4].symbol.symbol)
#             return node.father
#         # print(nod.symbol.symbol) 
#         find_father(identifier, nod)

def compare_symbol(identifier, value):
    print()

def remove_symbol(father):
    for symbol in symbol_table:
        # print(symbol_table.index(symbol))
        if symbol.father == father and symbol.father != symbol.identifier:
            symbol_delete = symbol_table.remove(symbol)
            # print('Symbolo eliminado:', symbol.identifier )
            remove_symbol(father)

exits_insert = False

def find_var_declaration(node):
    global current_function

    if node.symbol.symbol == 'CREATE':
        current_function = node.children[2].lexeme # obtenmos el nombre de la función

    # if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'CREATE':
    #     remove_symbol(current_function)  # eliminar todos los simbolos de current_function
    #     current_function = None
  
    if node.symbol.symbol == 'id':
        # preguntamos si el hermano es un type
        primer_hermano  = node.father.children[1] # si es table, nodo es tabla sino var
        
        if primer_hermano.symbol.symbol == 'TYPE':    
            # print(node.symbol.symbol, node.lexeme)

            category = 'var'

            if not find_symbol(node.lexeme, current_function):
                # Insertar en la pila
                add_symbol( node.lexeme, primer_hermano.children[0].lexeme, category, current_function )
            else:
                print('Syntax error 0006: Variable ya existente')
                exit()

        elif primer_hermano.symbol.symbol == 'tabla':
            category = 'tabla'

            # verificar que la variable no este en la pila, en caso este: error variable ya definida
            if not find_symbol(node.lexeme, current_function): # buscar si en la tabla de simbolos existe una misma variable de la misma función.
                # insertar en la pila
                add_symbol( node.lexeme, 'tabla', category, current_function )
            else:
                print('Syntax error 0005: Tabla ya existente')
                exit()

    for child in node.children:
        find_var_declaration(child)

    return symbol_table


table_values = []

# def find_values(node):
#     for node in node.children:
#         print(node.symbol.symbol)
#     find_values(node)

def exists_table (identifier, father=None):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.type == 'tabla':
            return symbol

def find_symbol_in_table(identifier, table_name):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.category == 'var' and table_name == symbol.father:
            return symbol

def column_total_table(identifier):
    count = 0
    for symbol in symbol_table:
        if symbol.identifier == identifier:
            continue

        if symbol.father == identifier:
            count+=1
    return count

def column_total_insert(node,identifier=None):
    global count
    for nod in node.children:
        if nod.symbol.symbol == 'dentro':
            count-=1

        if nod.symbol.symbol == 'id':
            count+=1
        column_total_insert(nod, identifier)

def column_total_values(identifier):
    count = 0
    for symbol in table_values:
        if symbol.table_name == identifier:
            count+=1
    return count

def add_insert(typ, table_name, columna):
    node_insert  = insert_table_node(typ, table_name, columna)
    table_values.append(node_insert) 

columna = 0
table_name = None
count = 0

def find_var_insert(node):
    global columna
    global table_name 
    global count

    if node.symbol.symbol == 'INSERT':
        table_name = node.children[2].lexeme

        if not exists_table(table_name):
            print('ERROR: TABLA NO EXISTETE')
            exit()
    
    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'INSERT':
        valores_a_insertar = column_total_values(table_name)
        columnas_tabla     = column_total_table(table_name)
        column_total_insert(node.father)
        columnas_insert    = count # column_total_insert(node)

        print(valores_a_insertar, columnas_tabla, count)

        if valores_a_insertar != columnas_tabla or valores_a_insertar != columnas_insert or columnas_tabla != columnas_insert:
            print("ERROR: SINTAX INSERT DATA")
            exit()
        count = 0

    if node.symbol.symbol == 'COLUMNAME' and node.children[0].symbol.symbol != 'comma' and node.children[0].symbol.symbol != 'e':
        # print(node.children[0].lexeme)
        if not find_symbol_in_table(node.children[0].lexeme, table_name):
            print('ERROR: COLUMNA NO EXISTENTE')
            exit()
        # print()

    if node.symbol.symbol == 'TRM':
        # table_values.append(node.children[0].symbol.symbol, table_name, columna)
        columna+=1
        add_insert(node.children[0].symbol.symbol, table_name, columna)

    for child in node.children:
        find_var_insert(child)
    
    return table_values


result = False

def func_insert_table(table_values, symbol_table):
    global result
    for symbol in symbol_table:

        if symbol.type == 'tabla':
            continue

        for value in table_values:

            if symbol.father == value.table_name:
                
                if symbol.type == value.type:
                    # print(symbol.type, value.type)
                    table_values.remove(value)
                    result = True
                    break

                else:
                    result = False
                    break

    if not result:
        print("Error: Datos no compatibles")
    else:
        print('\nInsert exitoso')