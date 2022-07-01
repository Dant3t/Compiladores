from multiprocessing.sharedctypes import Value
import os
import string

#include <iostream> 
#include <fstream> 
# using namespace std; 

# int main () { 
#  ofstream myfile; 
#  myfile.open ("User.csv");  
#  myfile.close(); 

#  ofstream myfile; 
#  myfile.open ("Task.csv");  
#  myfile.close(); 

#  return 0; 
# }

def symbol_exist_on_table(table_symbol, name_table):
    for symbol in table_symbol:
        if symbol.father == name_table:
            return True
    return False

def insert_values (file, symbol_table, table_generate_code, index_table, name_table):
    # tabla_de_valores = table_generate_code.copy()

    for symbol in symbol_table:
        for value in table_generate_code:
            # if not value.visitado: 
            if symbol.identifier == value.identifier and name_table == value.father and symbol.father == value.father:
                if value.typ == "varchar":
                    # valor = item.value
                    file.write("    myfile" + str(index_table) + " << " + str(value.value) + "\",\";" + os.linesep)
                    # tabla_de_valores.remove(value)
                    table_generate_code.remove(value)
                    # value.visitado = True
                    break
                else:
                    file.write("    myfile" + str(index_table) + " << \"" + str(value.value) + ",\"" + ";" + os.linesep)
                    # tabla_de_valores.remove(value)
                    table_generate_code.remove(value)
                    # value.visitado = True
                    break
        # insert_values (file, symbol_table, table_generate_code, index_table, name_table)

def generarCode(symbol_table, table_generate_code = []):
    name_table  = symbol_table[0].identifier
    index_table = 1
    contador    = 0
    
    file = open("main.cpp", "w")
    file.write("#include <iostream>" + os.linesep)
    file.write("#include <fstream> " + os.linesep)
    file.write("using namespace std;  " + os.linesep)
    file.write(os.linesep)
    file.write("int main () {" + os.linesep)

    for symbol in symbol_table:
        if symbol.identifier != name_table and symbol.category == 'tabla':
            file.write("")
            file.write("    myfile" + str(index_table) + " << " + "\"\\n\"" + ";" + os.linesep)
            file.write("    myfile" + str(index_table) + ".close(); " + os.linesep)
            file.write(os.linesep)
            index_table+=1
            contador = 0
            
        if symbol.category == 'tabla':
            name_table = symbol.identifier
            file.write("    ofstream myfile" + str(index_table) + ";" + os.linesep )
            file.write("    myfile" + str(index_table) + ".open (\"" + "./Tables/" + name_table + ".csv\");" + os.linesep);
            continue
            
        for column in symbol_table:
            if column.father == name_table and contador == 0 and column.category == 'var':
                file.write("    myfile" + str(index_table) + " << \"" + column.identifier + ",\"" + ";" + os.linesep)
                continue
                
        file.write("    myfile" + str(index_table) + " << " + "\"\\n\"" + ";" + os.linesep)
          
        insert_values(file, symbol_table, table_generate_code, index_table, name_table)
       
        while symbol_exist_on_table(table_generate_code, name_table):
            file.write("    myfile" + str(index_table) + " << " + "\"\\n\"" + ";" + os.linesep)
            insert_values(file, symbol_table, table_generate_code, index_table, name_table)
        contador += 1

    # file.write(os.linesep)
    file.write("    return 0;" + os.linesep)
    file.write("}" + os.linesep)

    file.close() 