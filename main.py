import lexer
import LL1
import symbol

# if __name__ == '__main__':
    
file = 'input.txt'
tokens = lexer.tokenize(file)

# print(tokens)

root, node_list = LL1.parser(tokens)
dot =  LL1.print_tree(root, node_list, info = False)
# print(dot)

symbol_table = symbol.find_var_declaration(root)
value_table = symbol.find_var_insert(root)

# symbol.func_insert_table(value_table, symbol_table)

for symbol in symbol_table:
    # print(symbol.identifier, symbol.type, symbol.category, symbol.father)
    continue

