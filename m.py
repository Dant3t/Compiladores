import ll1
import lex_micro_c

file_name = "ex1.c"

# lexer
tokens = lex_micro_c.get_tokens(file_name)
tokens.append(['$', None, None])

root, node_list = ll1.parser(tokens)

dot = ll1.print_tree(root, node_list, info = False)
#print(dot)

current_function = 'main'

class symbol_table_node:
  def __init__(self, identifier, typ, category, father = 'main', line = None):        
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



def find_var_declaration(node):
  global current_function
  if node.symbol.symbol == 'FUNCTION':
    current_function = node.children[2].lexeme # obtenmos el nombre de la función

  if node.symbol.symbol == 'rkey' and node.father.symbol.symbol == 'FUNCTION':
    # remove_symbol()  # eliminar todos los simbolos de current_function
    current_function = 'main'
    
  
  if node.symbol.symbol == 'id':
    # preguntamos si el hermano izquierdo es un type
    primer_hermano = node.father.children[0]
    segundo_hermano = node.father.children[1] # si es una función, aqui el node es function
    if primer_hermano.symbol.symbol == 'TYPE':    
      #print(node.symbol.symbol, node.lexeme)

      if segundo_hermano.symbol.symbol == 'function':  
        category = 'function'
      else:
        category = 'var'
      # verificar que la variable no este en la pila, en caso este: error variable ya definida
      #find_symbol() # buscar si en la tabla de simbolos existe una misma variable de la misma función.
      # insertar en la pila
      
      add_symbol( node.lexeme, primer_hermano.children[0].lexeme, category, current_function )
      
  for child in node.children:
    find_var_declaration(child)

find_var_declaration(root)

for symbol in symbol_table:
  print(symbol.identifier, symbol.type, symbol.category, symbol.father) 