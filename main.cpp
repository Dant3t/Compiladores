#include <iostream>
#include <fstream> 
using namespace std;  
 
int main () {
    ofstream myfile1;
    myfile1.open ("./Tables/clientes.csv");
    myfile1 << "idCliente,";
    myfile1 << "NomCliente,";
    myfile1 << "DirCliente,";
    myfile1 << "idpais,";
    myfile1 << "fonoCliente,";
    myfile1 << "\n";
    myfile1 << "ALFKI"",";
    myfile1 << "Alfreds Futterkiste"",";
    myfile1 << "Obere Str. 57"",";
    myfile1 << "002"",";
    myfile1 << "030-0074321"",";
    myfile1 << "\n";
    myfile1 << "ANATR"",";
    myfile1 << "Ana Trujillo Emparedados y helados"",";
    myfile1 << "Avda. de la Constitucion 2222"",";
    myfile1 << "005"",";
    myfile1 << "(5) 555-4729"",";
    myfile1 << "\n";
    myfile1 << "ANTON"",";
    myfile1 << "Antonio Moreno Taqueria"",";
    myfile1 << "Mataderos  2312"",";
    myfile1 << "007"",";
    myfile1 << "5 555-3932"",";
    myfile1 << "\n";
    myfile1 << "AROUT"",";
    myfile1 << "Around the Horn"",";
    myfile1 << "120 Hanover Sq."",";
    myfile1 << "004"",";
    myfile1 << "(71) 555-7788"",";
    myfile1 << "\n";
    myfile1 << "BERGS"",";
    myfile1 << "Berglunds snabbksp"",";
    myfile1 << "Berguvsvagen  8"",";
    myfile1 << "006"",";
    myfile1 << "0921-12 34 65"",";
    myfile1 << "\n";
    myfile1 << "BLAUS"",";
    myfile1 << "Blauer See Delikatessen"",";
    myfile1 << "Forsterstr. 57"",";
    myfile1 << "001"",";
    myfile1 << "0621-08460"",";
    myfile1 << "\n";
    myfile1 << "BLONP"",";
    myfile1 << "Blondel p�re et fils"",";
    myfile1 << "24, place Kleber Estrasbur"",";
    myfile1 << "008"",";
    myfile1 << "88.60.15.31"",";
    myfile1 << "\n";
    myfile1 << "BOLID"",";
    myfile1 << "Bolido Comidas preparadas"",";
    myfile1 << "C Araquil, 67"",";
    myfile1 << "009"",";
    myfile1 << "91 555 91 99"",";
    myfile1 << "\n";
    myfile1 << "BONAP"",";
    myfile1 << "Bon app"",";
    myfile1 << "12, rue des Bouchers"",";
    myfile1 << "001"",";
    myfile1 << "91.24.45.41"",";
    myfile1 << "\n";
    myfile1 << "BOTTM"",";
    myfile1 << "Bottom-Dollar Markets"",";
    myfile1 << "23 Tsawassen Blvd."",";
    myfile1 << "003"",";
    myfile1 << "(604) 555-3745"",";
    myfile1 << "\n";
    myfile1 << "BSBEV"",";
    myfile1 << "B Beverages"",";
    myfile1 << "Fauntleroy Circus"",";
    myfile1 << "009"",";
    myfile1 << "(71) 555-1212"",";
    myfile1 << "\n";
    myfile1 << "CACTU"",";
    myfile1 << "Cactus Comidas para llevar"",";
    myfile1 << "Cerrito 333"",";
    myfile1 << "002"",";
    myfile1 << "(1) 135-4892"",";
    myfile1 << "\n";
    myfile1 << "CENTC"",";
    myfile1 << "Centro comercial Moctezuma"",";
    myfile1 << "Sierras de Granada 9993"",";
    myfile1 << "008"",";
    myfile1 << "(5) 555-7293"",";
    myfile1 << "\n";
    myfile1 << "CHOPS"",";
    myfile1 << "Chop-suey Chinese"",";
    myfile1 << "Hauptstr. 29"",";
    myfile1 << "001"",";
    myfile1 << "999999999"",";
    myfile1 << "\n";
    myfile1 << "COMMI"",";
    myfile1 << "Comercio Mineiro"",";
    myfile1 << "Av. dos Lusiadas, 23"",";
    myfile1 << "004"",";
    myfile1 << "999999992"",";
    myfile1 << "\n";
    myfile1 << "CONSH"",";
    myfile1 << "Consolidated Holdings"",";
    myfile1 << "Berkeley Gardens\r\n12  Brewery"",";
    myfile1 << "005"",";
    myfile1 << "(71) 555-2282"",";
    myfile1 << "\n";
    myfile1 << "DRACD"",";
    myfile1 << "Drachenblut Delikatessen"",";
    myfile1 << "Walserweg 21"",";
    myfile1 << "006"",";
    myfile1 << "0241-059428"",";
    myfile1 << "\n";
    myfile1 << "DUMON"",";
    myfile1 << "Du monde entier"",";
    myfile1 << "67, rue des Cinquante Otages"",";
    myfile1 << "007"",";
    myfile1 << "40.67.89.89"",";
    myfile1 << "\n";
    myfile1 << "EASTC"",";
    myfile1 << "Eastern Connection"",";
    myfile1 << "35 King George"",";
    myfile1 << "005"",";
    myfile1 << "(71) 555-3373"",";
    myfile1 << "\n";
    myfile1 << "ERNSH"",";
    myfile1 << "Ernst Handel"",";
    myfile1 << "Kirchgasse 6"",";
    myfile1 << "001"",";
    myfile1 << "7675-3426"",";
    myfile1 << "\n";
    myfile1 << "FAMIA"",";
    myfile1 << "Familia Arquibaldo"",";
    myfile1 << "Rua Oros, 92"",";
    myfile1 << "004"",";
    myfile1 << "(11) 555-9857"",";
    myfile1 << "\n";
    myfile1 << "FISSA"",";
    myfile1 << "FISSA Fabrica Inter. Salchichas S.A."",";
    myfile1 << "C Moralzarzal, 86"",";
    myfile1 << "003"",";
    myfile1 << "(91) 555 55 93"",";
    myfile1 << "\n";
    myfile1 << "FOLIG"",";
    myfile1 << "Folies urmandes"",";
    myfile1 << "184, chaussee de Tournai"",";
    myfile1 << "009"",";
    myfile1 << "20.16.10.17"",";
    myfile1 << "\n";
    myfile1 << "FOLKO"",";
    myfile1 << "Folk och f HB"",";
    myfile1 << "kergatan 24"",";
    myfile1 << "003"",";
    myfile1 << "12391241"",";
    myfile1 << "\n";
    myfile1 << "FRANK"",";
    myfile1 << "Frankenversand"",";
    myfile1 << "Berliner Platz 43"",";
    myfile1 << "001"",";
    myfile1 << "089-0877451"",";
    myfile1 << "\n";
    myfile1 << "FRANR"",";
    myfile1 << "France restauration"",";
    myfile1 << "54, rue Royale"",";
    myfile1 << "008"",";
    myfile1 << "40.32.21.20"",";
    myfile1 << "\n";
    myfile1 << "FRANS"",";
    myfile1 << "Franchi S.p.A."",";
    myfile1 << "Via Monte Bianco 34"",";
    myfile1 << "001"",";
    myfile1 << "011-4988261"",";
    myfile1 << "\n";
    myfile1 << "FURIB"",";
    myfile1 << "Furia Bacalhau e Frutos do Mar"",";
    myfile1 << "Jardim das rosas n. 32"",";
    myfile1 << "008"",";
    myfile1 << "(1); 354-2535"",";
    myfile1 << "\n";
    myfile1 << "GALED"",";
    myfile1 << "Galeria del gastronomo"",";
    myfile1 << "Rambla de Catalu�a, 23"",";
    myfile1 << "004"",";
    myfile1 << "(93); 203 4561"",";
    myfile1 << "\n";
    myfile1 << "DOS"",";
    myfile1 << "dos Cocina Tipica"",";
    myfile1 << "C/ Romero, 33"",";
    myfile1 << "007"",";
    myfile1 << "9999999123"",";
    myfile1 << "\n";
    myfile1 << "URL"",";
    myfile1 << "urmet Lanchonetes"",";
    myfile1 << "Av. Brasil, 442"",";
    myfile1 << "008"",";
    myfile1 << "(11); 555-9482"",";
    myfile1 << "\n";
    myfile1 << "GREAL"",";
    myfile1 << "Great Lakes Food Market"",";
    myfile1 << "2732 Baker Blvd."",";
    myfile1 << "001"",";
    myfile1 << "(503); 555-7555"",";
    myfile1 << "\n";
    myfile1 << "GROSR"",";
    myfile1 << "GROSELLA-Restaurante"",";
    myfile1 << "5� Ave. Los Palos Grandes"",";
    myfile1 << "002"",";
    myfile1 << "(2); 283-3397"",";
    myfile1 << "\n";
    myfile1 << "HANAR"",";
    myfile1 << "Hanari Carnes"",";
    myfile1 << "Rua do Pa�o, 67"",";
    myfile1 << "001"",";
    myfile1 << "(21); 555-8765"",";
    myfile1 << "\n";
    myfile1 << "HILAA"",";
    myfile1 << "HILARIoN-Abastos"",";
    myfile1 << "Carrera 22 con Ave. Carlos Soublette #8-35"",";
    myfile1 << "008"",";
    myfile1 << "(5); 555-1948"",";
    myfile1 << "\n";
    myfile1 << "HUNGC"",";
    myfile1 << "Hungry Coyote Import Store"",";
    myfile1 << "City Center Plaza\r\n516 Main St."",";
    myfile1 << "009"",";
    myfile1 << "(503); 555-2376"",";
    myfile1 << "\n";
    myfile1 << "HUN"",";
    myfile1 << "Hungry Owl All-Night Grocers"",";
    myfile1 << "8 Johnstown Road"",";
    myfile1 << "005"",";
    myfile1 << "2967 3333"",";
    myfile1 << "\n";
    myfile1 << "ISLAT"",";
    myfile1 << "Island Trading"",";
    myfile1 << "Garden House\r\nCrowther Way"",";
    myfile1 << "003"",";
    myfile1 << "9991123"",";
    myfile1 << "\n";
    myfile1 << "KOENE"",";
    myfile1 << "K�niglich Essen"",";
    myfile1 << "Maubelstr. 90"",";
    myfile1 << "007"",";
    myfile1 << "0555-09876"",";
    myfile1 << "\n";
    myfile1 << "LACOR"",";
    myfile1 << "La corne deabondance"",";
    myfile1 << "67, avenue de Europe"",";
    myfile1 << "009"",";
    myfile1 << "30.59.84.10"",";
    myfile1 << "\n";
    myfile1 << "LAMAI"",";
    myfile1 << "La maison de Asie"",";
    myfile1 << "1 rue Alsace-Lorraine"",";
    myfile1 << "002"",";
    myfile1 << "61.77.61.11"",";
    myfile1 << "\n";
    myfile1 << "LAUGB"",";
    myfile1 << "Laughing Bacchus Wine Cellars"",";
    myfile1 << "1900 Oak St."",";
    myfile1 << "007"",";
    myfile1 << "(604); 555-7293"",";
    myfile1 << "\n";
    myfile1 << "LAZYK"",";
    myfile1 << "Lazy K Kountry Store"",";
    myfile1 << "12 Orchestra Terrace"",";
    myfile1 << "005"",";
    myfile1 << "(509); 555-6221"",";
    myfile1 << "\n";
    myfile1 << "LEHMS"",";
    myfile1 << "Lehmanns Marktstand"",";
    myfile1 << "Magazinweg 7"",";
    myfile1 << "004"",";
    myfile1 << "069-0245874"",";
    myfile1 << "\n";
    myfile1 << "LETSS"",";
    myfile1 << "Lets Stop N Shop"",";
    myfile1 << "87 Polk St.\r\nSuite 5"",";
    myfile1 << "001"",";
    myfile1 << "999999995"",";
    myfile1 << "\n";
    myfile1 << "LILAS"",";
    myfile1 << "LILA-Supermercado"",";
    myfile1 << "Carrera 52 con Ave. Bolivar #65-98 Llano Lar"",";
    myfile1 << "008"",";
    myfile1 << "(9); 331-7256"",";
    myfile1 << "\n";
    myfile1 << "LINOD"",";
    myfile1 << "LINO-Delicateses"",";
    myfile1 << "Ave. 5 de Mayo Porlamar"",";
    myfile1 << "002"",";
    myfile1 << "(8); 34-93-93"",";
    myfile1 << "\n";
    myfile1 << "LONEP"",";
    myfile1 << "Lonesome Pine Restaurant"",";
    myfile1 << "89 Chiaroscuro Rd."",";
    myfile1 << "001"",";
    myfile1 << "(503); 555-9646"",";
    myfile1 << "\n";
    myfile1 << "MAGAA"",";
    myfile1 << "Magazzini Alimentari Riuniti"",";
    myfile1 << "Via Ludovico il Moro 22"",";
    myfile1 << "007"",";
    myfile1 << "035-640231"",";
    myfile1 << "\n";
    myfile1 << "MAISD"",";
    myfile1 << "Maison Dewey"",";
    myfile1 << "Rue Joseph-Bens 532"",";
    myfile1 << "003"",";
    myfile1 << "(02); 201 24 68"",";
    myfile1 << "\n";
    myfile1 << "MEREP"",";
    myfile1 << "M�re Paillarde"",";
    myfile1 << "43 rue St. Laurent"",";
    myfile1 << "006"",";
    myfile1 << "(514); 555-8055"",";
    myfile1 << "\n";
    myfile1 << "MORGK"",";
    myfile1 << "Morgenstern Gesundkost"",";
    myfile1 << "Heerstr. 22"",";
    myfile1 << "009"",";
    myfile1 << "999999992"",";
    myfile1 << "\n";
    myfile1 << "NORTS"",";
    myfile1 << "North/South"",";
    myfile1 << "South House\r\n300 Queensbridge"",";
    myfile1 << "005"",";
    myfile1 << "(71); 555-2530"",";
    myfile1 << "\n";
    myfile1 << "OCEAN"",";
    myfile1 << "Oceano Atlantico Ltda."",";
    myfile1 << "Ing. Gustavo Moncada 8585\r\nPiso 20-A"",";
    myfile1 << "001"",";
    myfile1 << "(1); 135-5535"",";
    myfile1 << "\n";
    myfile1 << "OLDWO"",";
    myfile1 << "Old World Delicatessen"",";
    myfile1 << "2743 Bering St."",";
    myfile1 << "004"",";
    myfile1 << "(907); 555-2880"",";
    myfile1 << "\n";
    myfile1 << "OTTIK"",";
    myfile1 << "Ottilies K�seladen"",";
    myfile1 << "Mehrheimerstr. 369"",";
    myfile1 << "003"",";
    myfile1 << "0221-0765721"",";
    myfile1 << "\n";
    myfile1 << "PARIS"",";
    myfile1 << "Paris specialites"",";
    myfile1 << "265, boulevard Charonne"",";
    myfile1 << "008"",";
    myfile1 << "(1); 42.34.22.77"",";
    myfile1 << "\n";
    myfile1 << "PERIC"",";
    myfile1 << "Pericles Comidas clasicas"",";
    myfile1 << "Calle Dr. Jorge Cash 321"",";
    myfile1 << "003"",";
    myfile1 << "(5); 545-3745"",";
    myfile1 << "\n";
    myfile1 << "PICCO"",";
    myfile1 << "Piccolo und mehr"",";
    myfile1 << "Geislweg 14"",";
    myfile1 << "002"",";
    myfile1 << "6562-9723"",";
    myfile1 << "\n";
    myfile1 << "PRINI"",";
    myfile1 << "Princesa Isabel Vinhos"",";
    myfile1 << "Estrada da sa�de n. 58"",";
    myfile1 << "004"",";
    myfile1 << "00123914"",";
    myfile1 << "\n";
    myfile1 << "QUEDE"",";
    myfile1 << "Que Delicia"",";
    myfile1 << "Rua da Panificadora, 12"",";
    myfile1 << "004"",";
    myfile1 << "(21); 555-4545"",";
    myfile1 << "\n";
    myfile1 << "QUEEN"",";
    myfile1 << "Queen Cozinha"",";
    myfile1 << "Alameda dos Can�rios, 891"",";
    myfile1 << "009"",";
    myfile1 << "38473242"",";
    myfile1 << "\n";
    myfile1 << "QUICK"",";
    myfile1 << "QUICK-Stop"",";
    myfile1 << "Taucherstra�e 10"",";
    myfile1 << "006"",";
    myfile1 << "1293123"",";
    myfile1 << "\n";
    myfile1 << "RANCH"",";
    myfile1 << "Rancho grande"",";
    myfile1 << "Av. del Libertador 900"",";
    myfile1 << "001"",";
    myfile1 << "(1); 123-5556"",";
    myfile1 << "\n";
    myfile1 << "RATTC"",";
    myfile1 << "Rattlesnake Canyon Grocery"",";
    myfile1 << "2817 Milton Dr."",";
    myfile1 << "001"",";
    myfile1 << "(505); 555-3620"",";
    myfile1 << "\n";
    myfile1 << "REGGC"",";
    myfile1 << "Reggiani Caseifici"",";
    myfile1 << "Strada Provinciale 124"",";
    myfile1 << "003"",";
    myfile1 << "0522-556722"",";
    myfile1 << "\n";
    myfile1 << "RICAR"",";
    myfile1 << "Ricardo Adocicados"",";
    myfile1 << "Av. Copacabana, 267"",";
    myfile1 << "007"",";
    myfile1 << "478234723"",";
    myfile1 << "\n";
    myfile1 << "RICSU"",";
    myfile1 << "Richter Supermarkt"",";
    myfile1 << "Grenzacherweg 237"",";
    myfile1 << "003"",";
    myfile1 << "923747234"",";
    myfile1 << "\n";
    myfile1 << "ROMEY"",";
    myfile1 << "Romero y tomillo"",";
    myfile1 << "Gran Via, 1"",";
    myfile1 << "009"",";
    myfile1 << "(91); 745 6210"",";
    myfile1 << "\n";
    myfile1 << "SANTG"",";
    myfile1 << "Sante urmet"",";
    myfile1 << "Erling Skakkes gate 78"",";
    myfile1 << "002"",";
    myfile1 << "07-98 92 47"",";
    myfile1 << "\n";
    myfile1 << "SAVEA"",";
    myfile1 << "Save-a-lot Markets"",";
    myfile1 << "187 Suffolk Ln."",";
    myfile1 << "005"",";
    myfile1 << "(208); 555-8097"",";
    myfile1 << "\n";
    myfile1 << "SEVES"",";
    myfile1 << "Seven Seas Imports"",";
    myfile1 << "90 Wadhurst Rd."",";
    myfile1 << "008"",";
    myfile1 << "(71); 555-5646"",";
    myfile1 << "\n";
    myfile1 << "SIMOB"",";
    myfile1 << "Simons bistro"",";
    myfile1 << "Vinb�ltet 34"",";
    myfile1 << "006"",";
    myfile1 << "31 13 35 57"",";
    myfile1 << "\n";
    myfile1 << "SPECD"",";
    myfile1 << "Specialites du monde"",";
    myfile1 << "25, rue Lauriston"",";
    myfile1 << "003"",";
    myfile1 << "(1); 47.55.60.20"",";
    myfile1 << "\n";
    myfile1 << "SPLIR"",";
    myfile1 << "Split Rail Beer & Ale"",";
    myfile1 << "P.O. Box 555"",";
    myfile1 << "004"",";
    myfile1 << "(307); 555-6525"",";
    myfile1 << "\n";
    myfile1 << "SUPRD"",";
    myfile1 << "Supr�mes delices"",";
    myfile1 << "Boulevard Tirou, 255"",";
    myfile1 << "009"",";
    myfile1 << "(071); 23 67 22 21"",";
    myfile1 << "\n";
    myfile1 << "THEBI"",";
    myfile1 << "The Big Cheese"",";
    myfile1 << "89 Jefferson Way\r\nSuite 2"",";
    myfile1 << "003"",";
    myfile1 << "123415"",";
    myfile1 << "\n";
    myfile1 << "THECR"",";
    myfile1 << "The Cracker Box"",";
    myfile1 << "55 Grizzly Peak Rd."",";
    myfile1 << "007"",";
    myfile1 << "(406); 555-8083"",";
    myfile1 << "\n";
    myfile1 << "TOMSP"",";
    myfile1 << "Toms Spezialit�ten"",";
    myfile1 << "Luisenstr. 48"",";
    myfile1 << "004"",";
    myfile1 << "0251-035695"",";
    myfile1 << "\n";
    myfile1 << "TORTU"",";
    myfile1 << "Tortuga Restaurante"",";
    myfile1 << "Avda. Azteca 123"",";
    myfile1 << "006"",";
    myfile1 << "12312"",";
    myfile1 << "\n";
    myfile1 << "TRADH"",";
    myfile1 << "Tradi��o Hipermercados"",";
    myfile1 << "Av. In�s de Castro, 414"",";
    myfile1 << "009"",";
    myfile1 << "(11); 555-2168"",";
    myfile1 << "\n";
    myfile1 << "TRAIH"",";
    myfile1 << "Trails Head urmet Provisioners"",";
    myfile1 << "722 DaVinci Blvd."",";
    myfile1 << "001"",";
    myfile1 << "(206); 555-2174"",";
    myfile1 << "\n";
    myfile1 << "VAFFE"",";
    myfile1 << "Vaffeljernet"",";
    myfile1 << "Smagsl�get 45"",";
    myfile1 << "003"",";
    myfile1 << "86 22 33 44"",";
    myfile1 << "\n";
    myfile1 << "VICTE"",";
    myfile1 << "Victuailles en stock"",";
    myfile1 << "2, rue du Commerce"",";
    myfile1 << "007"",";
    myfile1 << "78.32.54.87"",";
    myfile1 << "\n";
    myfile1 << "VINET"",";
    myfile1 << "Vins et alcools Chevalier"",";
    myfile1 << "59 rue de lAbbaye"",";
    myfile1 << "005"",";
    myfile1 << "26.47.15.11"",";
    myfile1 << "\n";
    myfile1 << "WANDK"",";
    myfile1 << "Die Wandernde Kuh"",";
    myfile1 << "Adenauerallee 900"",";
    myfile1 << "008"",";
    myfile1 << "0711-035428"",";
    myfile1 << "\n";
    myfile1 << "WARTH"",";
    myfile1 << "Wartian Herkku"",";
    myfile1 << "Torikatu 38"",";
    myfile1 << "002"",";
    myfile1 << "981-443655"",";
    myfile1 << "\n";
    myfile1 << "WELLI"",";
    myfile1 << "Wellington Importadora"",";
    myfile1 << "Rua do Mercado, 12"",";
    myfile1 << "005"",";
    myfile1 << "91823-123"",";
    myfile1 << "\n";
    myfile1 << "WHITC"",";
    myfile1 << "White Clover Markets"",";
    myfile1 << "305 - 14th Ave. S.\r\nSuite 3B"",";
    myfile1 << "003"",";
    myfile1 << "(206); 555-4115"",";
    myfile1 << "\n";
    myfile1 << "WILMK"",";
    myfile1 << "Wilman Kala"",";
    myfile1 << "Keskuskatu 45"",";
    myfile1 << "007"",";
    myfile1 << "90-224 8858"",";
    myfile1 << "\n";
    myfile1 << "WOLZA"",";
    myfile1 << "Wolski  Zajazd"",";
    myfile1 << "ul. Filtrowa 68"",";
    myfile1 << "002"",";
    myfile1 << "(26); 642-7012"",";
    myfile1 << "\n";
    myfile1 << "\n";
    myfile1 << "\n";
    myfile1 << "\n";
    myfile1 << "\n";
    myfile1.close(); 

    ofstream myfile2;
    myfile2.open ("./Tables/producto.csv");
    myfile2 << "idproducto,";
    myfile2 << "nombreProducto,";
    myfile2 << "precioProducto,";
    myfile2 << "\n";
    myfile2 << "1,";
    myfile2 << "Queso"",";
    myfile2 << "2,";
    myfile2 << "\n";
    myfile2 << "2,";
    myfile2 << "Pescado"",";
    myfile2 << "12,";
    myfile2 << "\n";
    myfile2 << "3,";
    myfile2 << "Carne"",";
    myfile2 << "7,";
    myfile2 << "\n";
    myfile2 << "4,";
    myfile2 << "Yogurt"",";
    myfile2 << "9,";
    myfile2 << "\n";
    myfile2 << "5,";
    myfile2 << "Leche"",";
    myfile2 << "6,";
    myfile2 << "\n";
    myfile2 << "6,";
    myfile2 << "Papa"",";
    myfile2 << "3,";
    myfile2 << "\n";
    myfile2 << "7,";
    myfile2 << "Zanahoria"",";
    myfile2 << "414,";
    myfile2 << "\n";
    myfile2 << "8,";
    myfile2 << "Cerveza"",";
    myfile2 << "33,";
    myfile2 << "\n";
    myfile2 << "9,";
    myfile2 << "Caja"",";
    myfile2 << "12,";
    myfile2 << "\n";
    myfile2 << "\n";
    return 0;
}
