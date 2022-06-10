from glob import glob
from itertools import count
from pickle import FALSE


current_function = None


class insert_table_node:
    def __init__(self, identifier, table_name, id_insert = None, typ = None, columna = None):
        self.identifier = identifier
        self.table_name = table_name
        self.id         = id_insert

        self.type       = typ
        self.columna    = columna

    def set_type(self, typ, id_insert = None):
        self.type       = typ
        self.id         = id_insert

class symbol_table_node:
    def __init__(self, identifier, typ, category, father = None, line = None):        
        self.identifier  = identifier
        self.type        = typ # tipo de dato
        self.category    = category # funcion o variable
        self.line        = line
        self.father      = father # a q función pertenece

symbol_table = []

def add_symbol(identifier, typ, category, current_function):
    node_symbol = symbol_table_node(identifier, typ, category, current_function)
    symbol_table.append(node_symbol)

def find_symbol(identifier, father):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.father == father:
            return symbol

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

    if node.symbol.symbol == 'CREATE' or node.symbol.symbol == 'INSERT':
        current_function = node.children[2].lexeme # obtenmos el nombre de la función

    # if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'CREATE':
    #     remove_symbol(current_function)  # eliminar todos los simbolos de current_function
    #     current_function = None
   
    if node.symbol.symbol == 'id' and node.father.symbol.symbol == 'COLUMNAME':
        # if node.father.father.father.symbol.symbol == "INSERT":
        #     # add_identifier_insert(node.father.father.father.children[2].lexeme)
        add_identifier_insert(node.lexeme, current_function)

    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'INSERT':
        if not exists_table(current_function):
            print("ERROR: TABLA NO EXISTENTE")
            exit()
  
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

def add_identifier_insert(identifier, table_name):
    node_insert  = insert_table_node(identifier, table_name)
    table_values.append(node_insert) 

def exists_table (identifier, father=None):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.type == 'tabla':
            return symbol

def find_symbol_in_table(identifier, table_name):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.category == 'var' and table_name == symbol.father:
            return symbol

def column_total_table(identifier):
    global columnas_tabla
    for symbol in symbol_table:
        if symbol.identifier == identifier:
            continue

        if symbol.father == identifier:
            columnas_tabla+=1

def column_total_insert(node,identifier=None):
    global columnas_insert
    for nod in node.children:
        if nod.symbol.symbol == 'dentro':
            columnas_insert-=1

        if nod.symbol.symbol == 'id':
            columnas_insert+=1
        column_total_insert(nod, identifier)

def column_total_values(identifier):
    global valores_a_insertar 
    for symbol in table_values:
        if symbol.type == None:
            continue
        if symbol.table_name == identifier:
            # table_values.remove(symbol)
            valores_a_insertar+=1

def add_insert(typ, table_name, columna):
    for value in table_values:
        if value.table_name == table_name and value.type == None:
            # print(typ)
            value.set_type(typ)

            return
columna = 0
table_name = None

columnas_insert    = 0
valores_a_insertar = 0
columnas_tabla     = 0

def find_var_insert(node):
    global columna
    global table_name 
    global columnas_insert, columnas_tabla, valores_a_insertar

    if node.symbol.symbol == 'INSERT':
        table_name = node.children[2].lexeme

        if not exists_table(table_name):
            print('ERROR: TABLA NO EXISTETE')
            exit()
    
    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'INSERT':
        # valores_a_insertar = column_total_values(table_name)
        # columnas_tabla     = column_total_table(table_name)
        column_total_values(table_name)
        column_total_table(table_name)
        column_total_insert(node.father)
        # columnas_insert    = count # column_total_insert(node)

        # print(valores_a_insertar, columnas_tabla, columnas_insert)

        if valores_a_insertar != columnas_tabla or valores_a_insertar != columnas_insert or columnas_tabla != columnas_insert:
            print("ERROR: SINTAX DEMACIADAS O MUY POCAS COLUMNAS")
            exit()
        
        columnas_insert    = 0
        valores_a_insertar = 0
        columnas_tabla     = 0

        # func_insert_table(table_values, symbol_table)

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

            if symbol.father == value.table_name and symbol.identifier == value.identifier:
                
                if symbol.type == value.type:
                    # print(symbol.type, value.type)
                    # print(symbol.identifier, value.identifier)
                    table_values.remove(value)
                    result = True
                    break

                else:
                    print("-----------------------------------")
                    print(symbol.type, value.type)
                    print(symbol.identifier, value.identifier)
                    table_values.remove(value)
                    result = False
                    if not result:
                        print("ERROR: DATOS NO COMPATIBLES")
                        exit()
                    break

    if result:
        print('INSERT EXITOSO')