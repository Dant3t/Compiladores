#include <iostream>
#include <fstream> 
using namespace std;  

int main () {
    ofstream myfile1;
    myfile1.open ("./Tables/clientes.csv");
    myfile1 << "id = 4\n";
    myfile1 << "id = 13\n";
    myfile1 << "numero = 1\n";
    myfile1 << "numero = 2\n";
    myfile1 << "activo = verdadero\n";
    myfile1 << "activo = falso\n";
    myfile1.close(); 

    ofstream myfile2;
    myfile2.open ("./Tables/user.csv");
    myfile2 << "id = 23\n";
    myfile2 << "comment = ""Este es un comentario""\n";
    return 0;
}
