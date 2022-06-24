import string
from tabnanny import check
from tokenize import String
from unicodedata import name
import pandas as pd
import csv
import os

from insert import column

all_table    = False
exists_where = False
name_table   = ''
columns      = []
values_condt = []

def select_table(node, symbol_table):
    global all_table, name_table, columns, exists_where, values_condt

    if node.symbol.symbol == 'SELECT':
        name_table = node.children[3].lexeme
        if node.children[1].children[0].symbol.symbol == 'times':
            all_table = True
        if node.children[4].children[0].symbol.symbol == 'donde':
            exists_where = True 

    if node.symbol.symbol == 'id' and node.father.symbol.symbol == 'CONDITIONAL': 
        values_condt.append(node.lexeme)
    
    if node.symbol.symbol == 'id' and node.father.symbol.symbol == 'CONDITION':
        values_condt.append(node.lexeme)

    if exists_where:
        if node.symbol.symbol == 'OPERATOR':
            values_condt.append(node.children[0].lexeme)
        if node.symbol.symbol == 'TRM' and (node.father.symbol.symbol == 'CONDITIONAL' or node.father.symbol.symbol == 'CONDITION'):
            values_condt.append(node.children[0].lexeme)

    if not all_table:
        if node.symbol.symbol == 'id' and node.father.symbol.symbol == 'NAMEPARAM':
            columns.append(node.lexeme)
            # print(node.lexeme)

    if node.symbol.symbol == 'dotcomma' and node.father.symbol.symbol == 'SELECT':
        if all_table:
            print_all_table(name_table, symbol_table)
            all_table = False
        elif exists_where:
            print_select_conditional(name_table)
            exists_where = False
        else:
            print_select_columns(name_table)
            exists_where = False

    for child in node.children:
        select_table(child, symbol_table)


def check_select():
    print()


def print_all_table(identifier, symbol_table):

    column = []

    for symbol in symbol_table:
        if symbol.father == identifier and symbol.category == 'var':
            column.append(symbol.identifier)

    dirc  = "./Tables/"
    file  = identifier + '.csv'
    pFile = dirc + file

    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename = os.path.join(current_dir, pFile) 

    syntax_table = pd.read_csv(pFile, usecols=column, sep=',')
    print(syntax_table)
    print("---------------------------------------------------")

def print_select_columns (identifier):
    global columns

    dirc  = "./Tables/"
    file  = identifier + '.csv'
    pFile = dirc + file

    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename = os.path.join(current_dir, pFile) 

    syntax_table = pd.read_csv(pFile, usecols=columns, sep=',')
    print(syntax_table)
    print("---------------------------------------------------")

    for i in range(len(columns)):
        columns.pop()

def print_select_conditional(identifier):
    global values_condt, columns

    dirc  = "./Tables/"
    file  = identifier + '.csv'
    pFile = dirc + file

    # for value in values_condt:
    #     print(value)

    # current_dir = os.path.dirname(os.path.realpath(__file__)) 
    # filename = os.path.join(current_dir, pFile) 

    syntax_table = pd.read_csv(pFile, usecols=columns, sep=',')

    print(syntax_table)

    produccion   = syntax_table.loc[1, str(values_condt[0])] 
    # print(produccion)
    
    print("---------------------------------------------------")

    for i in range(len(columns)):
        columns.pop()