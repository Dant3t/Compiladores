class column:
    def __init__(self, idenfifier, typ, values = []):
        self.identifier = idenfifier
        self.typ        = typ
        self.values     = values

class table:
    def __init__(self, identifier, columns = []):
        self.identifier  = identifier
        self.columns     = columns


# def exists_table (identifier, symbol_table):
#     for symbol in symbol_table:
#         if symbol.identifier == identifier and symbol.type == 'tabla':
#             return symbol

def find_symbol_in_table(identifier, table_name, symbol_table):
    for symbol in symbol_table:
        if symbol.identifier == identifier and symbol.category == 'var' and table_name == symbol.father:
            return symbol

def find_type_value(type_value = []):
    typ = type_value[0]
    
    for item in type_value:
        # print(item)
        if item != typ:
            print("ERROR: DATOS NO COMPATIBLES - FIND_TYPE_VALUE")
            exit() 

    for i in range(len(type_value)):
        type_value.pop(0)
    
    return typ

def check_insert_values(name_table, values_insert, params_insert, symbol_table):
    colums       = 0
    values_table = []
    for symbol in symbol_table:
        # print(symbol.type)
        if symbol.category == 'var' and symbol.father == name_table:
            values_table.append(symbol)
            colums+=1

    visited   = set()
    params_id = {param for param in params_insert if param in visited or (visited.add(param) or False)}
    # print(params_id) 
    # print(len(params_id)) 

    if len(values_insert) == len(params_insert) == colums and len(params_id) == 0:
        pass
    else:
        print("ERROR: INSERT PARAMS")
        exit()

    params_id  = params_insert.copy()
    last_param = params_id.pop()

    for param in params_insert:
        # print(param, len(values_table))
        for value in values_table:
            # print("Buscando en tabla de valores")
            # print(value.identifier)
            if param == value.identifier:
                # print(param, value.identifier, values_insert[0], value.type)
                if values_insert[0] == value.type:
                    # params_insert.pop(0)
                    values_insert.pop(0)
                    values_table.remove(value)
                else:
                    print("ERROR - INSERT CHECK: DATOS NO COMPATIBLES")
                    exit()

    for i in range(len(params_insert)):
        params_insert.pop(0)

    # print("INSERT EXITOSO")

table_generate_code = []

class node_generate_code:
    def __init__(self, father, identifier, typ, value):
        self.father     = father
        self.identifier = identifier
        self.typ        = typ
        self.value      = value

def func_plus(father, identifier, typ, values = []):
    global table_generate_code

    sum_total = 0

    if typ == 'entero':
        for value in values:
            sum_total+=int(value)

    new_node = node_generate_code(father, identifier, typ, sum_total)
    table_generate_code.append(new_node)

    for i in range(len(values)):
        values.pop(0)

def add_node_table_generate_code(father, identifier, typ, values = []):
    global table_generate_code

    new_node = node_generate_code(father, identifier, typ, values[0])
    table_generate_code.append(new_node)

    for i in range(len(values)):
        values.pop(0)

name_table        = ''
values_insert     = []
params_insert     = []
type_value        = []

data_insert       = []
index_colum       = 0
symbol_plus       = False

def find_insert_var(node, symbol_table):
    global name_table, values_insert, params_insert, data_insert, index_colum, table_generate_code
    global symbol_plus

    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'INSERT':
        # print(name_table)
        check_insert_values(name_table, values_insert, params_insert, symbol_table)
        index_colum = 0
        # for i in params_insert:
        #     print(i)

    if node.symbol.symbol == 'INSERT':
        name_table = node.children[2].lexeme # obtenmos el nombre de la tabla
    
        # if not exists_table(name_table, symbol_table):
        #     print("NO EXISTE LA TABLA")
        #     exit()

    if node.symbol.symbol == 'plus':
        symbol_plus = True


    if node.symbol.symbol == 'TRM':
        if node.children[0].symbol.symbol == 'number':
            type_value.append('entero')
            data_insert.append(node.children[0].lexeme)
        if node.children[0].symbol.symbol == 'bool':
            type_value.append('booleano')
            data_insert.append(node.children[0].lexeme)
        if node.children[0].symbol.symbol == 'string':
            type_value.append('varchar')
            data_insert.append(node.children[0].lexeme)

    if len(type_value) > 0:
        if node.symbol.symbol == 'comma' or node.symbol.symbol == 'e' and node.father.symbol.symbol == 'VALUE':
            typ = find_type_value(type_value)

            if symbol_plus:
                func_plus(name_table, params_insert[index_colum], typ, data_insert)
                symbol_plus = False
            else:
                if index_colum == len(params_insert):
                    print("ERROR: INSERT PARAMS - INDEX LIST")
                    exit()
                else:
                    add_node_table_generate_code(name_table, params_insert[index_colum], typ, data_insert)

            values_insert.append(typ)
            index_colum+=1

    if node.symbol.symbol == 'COLUMNAME' and node.children[0].symbol.symbol != 'comma' and node.children[0].symbol.symbol != 'e':
        # print(node.children[0].lexeme)
        if not find_symbol_in_table(node.children[0].lexeme, name_table, symbol_table):
            print('ERROR: COLUMNA NO EXISTENTE')
            exit()
        else:
            params_insert.append(node.children[0].lexeme)
    
    for child in node.children:
        find_insert_var(child, symbol_table)

    return table_generate_code