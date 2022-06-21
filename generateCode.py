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

def generarCode(symbol_table, table_generate_code = []):
    name_table  = symbol_table[0].identifier
    index_table = 1
    
    file = open("main.cpp", "w")
    file.write("#include <iostream>" + os.linesep)
    file.write("#include <fstream> " + os.linesep)
    file.write("using namespace std;  " + os.linesep)
    file.write(os.linesep)
    file.write("int main () {" + os.linesep)

    for symbol in symbol_table:
        if symbol.identifier != name_table and symbol.category == 'tabla':
            file.write("")
            file.write("    myfile" + str(index_table) + ".close(); " + os.linesep)
            file.write(os.linesep)
            index_table+=1
            
        if symbol.category == 'tabla':
            name_table = symbol.identifier
            file.write("    ofstream myfile" + str(index_table) + ";" + os.linesep )
            file.write("    myfile" + str(index_table) + ".open (\"" + "./Tables/" + name_table + ".csv\");" + os.linesep);
            continue
            
        if symbol.category == 'var' and symbol.father == name_table:
            valor = ''
            for item in table_generate_code:
                if item.father == name_table and item.identifier == symbol.identifier and item.typ != "varchar":
                    file.write("    myfile" + str(index_table) + " << \"" + symbol.identifier + " = " + str(item.value) + "\\n\"" + ";" + os.linesep )
                    continue

                if item.typ == "varchar" and item.father == name_table and item.identifier == symbol.identifier:
                    # valor = item.value

                    file.write("    myfile" + str(index_table) + " << \"" + symbol.identifier + " = \"" + str(item.value) + "\"\\n\"" + ";" + os.linesep)
                    table_generate_code.remove(item)
                    continue


    # file.write(os.linesep)
    file.write("    return 0;" + os.linesep)
    file.write("}" + os.linesep)

    file.close()