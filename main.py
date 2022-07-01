import lexer
import LL1
import symbol
import generateCode
import insert
import seleccionar as select

# if __name__ == '__main__':
    
file = 'input1.txt'
tokens = lexer.tokenize(file)

#print(tokens)

root, node_list = LL1.parser(tokens)
dot =  LL1.print_tree(root, node_list, info = False)
#print(dot)

symbol_table         = symbol.find_var_declaration(root)
table_generate_code  = insert.find_insert_var(root, symbol_table)

generateCode.generarCode(symbol_table, table_generate_code)
select.select_table(root, symbol_table) # Comenta esta parte, una vez que corrar el main.cpp y se creen los archivos .csv lo descomentas xd me olvide arreglar esto 

for symbol in symbol_table:
    #print(symbol.identifier, symbol.type, symbol.category, symbol.father)
    continue

