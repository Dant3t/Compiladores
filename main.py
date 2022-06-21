import lexer
import LL1
import symbol
import generateCode
import insert

# if __name__ == '__main__':
    
file = 'input.txt'
tokens = lexer.tokenize(file)

# print(tokens)

root, node_list = LL1.parser(tokens)
dot =  LL1.print_tree(root, node_list, info = False)
# print(dot)

symbol_table         = symbol.find_var_declaration(root)
table_generate_code  = insert.find_insert_var(root, symbol_table)

# for nod in table_generate_code:
#     print(nod.father, nod.identifier, nod.typ)
#     print(nod.value)

# for value in values_insert:
#     print(value)
#     continue
# value_table = symbol.find_var_insert(root)

generateCode.generarCode(symbol_table, table_generate_code)
# symbol.func_insert_table(value_table, symbol_table)

for symbol in symbol_table:
    # print(symbol.identifier, symbol.type, symbol.category, symbol.father)
    continue

