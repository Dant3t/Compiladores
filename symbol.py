
current_function = None

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

def remove_symbol(father):
    for symbol in symbol_table:
        # print(symbol_table.index(symbol))
        if symbol.father == father and symbol.father != symbol.identifier:
            symbol_delete = symbol_table.remove(symbol)
            # print('Symbolo eliminado:', symbol.identifier )
            remove_symbol(father)

def find_var_declaration(node):
    global current_function
    if node.symbol.symbol == 'CREATE':
        current_function = node.children[2].lexeme # obtenmos el nombre de la función

    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'CREATE':
        remove_symbol(current_function)  # eliminar todos los simbolos de current_function
        current_function = None
  
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

