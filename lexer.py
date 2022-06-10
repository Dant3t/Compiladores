import ply.lex as lex

 # List of token names.   This is always required

reserved = {
   'crear'          : 'crear',
   'tabla'          : 'tabla',
   'seleccionar'    : 'seleccionar',
   'desde'          : 'desde',
   'no'             : 'no',
   'nulo'           : 'nulo',
   'unico'          : 'unico',
   'primaria'       : 'primaria',
   'clave'          : 'clave',
   'flotante'       : 'flotante',
   'serial'         : 'serial',
   'varchar'        : 'varchar',
   'eliminar'       : 'eliminar',
   'insertar'       : 'insertar',
   'dentro'         : 'dentro',
   'valores'        : 'valores',
   'entero'         : 'entero',
   'boleano'        : 'boleano'
}

tokens = [
    'number',
    'dotcomma',
    'comma',
    'lpar',
    'rpar',
    'keyword',
    'id',
    'times',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_lpar     = r'\('
t_rpar     = r'\)'
t_comma    = r'\,'
t_dotcomma = r'\;'
t_times    = r'\*'

t_ignore   = ' \t'

# t_keyword    = r'\b(AÑADIR|DESPUÉS|TODO|ALTERAR|NADA|COMO|ASCENDENTE|AUTO_INCREMENTAR|INICIAR|EMPEZAR|ROMPER|EN_CASCADA|RESTRICCIÓN|CONTINUA|DECLARAR|POR_DEFECTO|DESC|DESCRIBIR|HACER|DOBLE|SOLTAR|ELSE(IF)?|FIN|MOTOR|ENUM|EXISTE|SALIR|ARCHIVO|PRIMERO|FLOTANTE|FOR(EACH_ROW)?|FORÁNEO|FUNCIÓN|GLOBAL|GRUPO|IF|INDEX|INTERNAMENTE|INSERTAR|DENTRO_DE|ITERAR|UNIR|CLAVES?|ÚLTIMO|IZQUIERDA|LÍMITE|BUCLE|TEXTO|MODIFICAR|MES|SOBRE|ORDENAR|REFERENCIAS|RESTRINGIR|DERECHA|FILA|ESTADO|INDEFINIDO|UNICO|ACTUALIZAR|UTILIZAR|VALORES)\b'

def t_entero(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    return t

def t_boleano(t):
    r'verdadero | falso '
    return t

def t_id(t):
    r'\b[a-zA-Z_]+\w*\b'   
    t.type = reserved.get(t.value,'id')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def tokenize(file):
    # Open file and read
    f = open (file,'r')
    data = f.read()

    # print(data)

    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(data)
    tokens = []

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        #print(tok)
        tokens.append([tok.type, tok.value, tok.lineno])
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)

    f.close()

    tokens.append(['$', None, None])
    
    return tokens
 